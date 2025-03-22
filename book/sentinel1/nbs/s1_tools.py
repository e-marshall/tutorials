import numpy as np
import matplotlib.pyplot as plt
import markdown
import os
import pandas as pd
import pathlib
import re
import xarray as xr


# --------------------------------------------------------------------
# --------------------- Read ASF VRT Functions -----------------
# Function to extract path for target files from each scene
def extract_fnames(data_path: str, scene_name: str, variable: str):
    # Make list of files within each scene directory in data directory
    scene_files_ls = os.listdir(os.path.join(data_path, scene_name))

    if variable in ["vv", "vh"]:
        scene_files = [fname for fname in scene_files_ls if fname.endswith(f"_{variable.upper()}.tif")]

    elif variable == "ls_map":
        scene_files = [fname for fname in scene_files_ls if fname.endswith("_ls_map.tif")]

    elif variable == "readme":
        scene_files = [file for file in scene_files_ls if file.endswith("README.md.txt")]

    return scene_files


def make_filepath_lists(asf_s1_data_path: str, variable: str):
    """For a single variable (vv, vh, ls_map or readme), make list of
    full filepath for each file in time series. Also return dates to ensure
    extraction happens in correct order for each variable
    Return tuple with form (filepaths list, dates list)"""
    scenes_ls = os.listdir(asf_s1_data_path)

    fpaths, dates_ls = [], []

    for element in range(len(scenes_ls)):
        # Extract filenames of each file of interest
        files_of_interest = extract_fnames(asf_s1_data_path, scenes_ls[element], variable)
        # Make full path with filename for each variable
        path = os.path.join(asf_s1_data_path, scenes_ls[element], files_of_interest[0])
        # extract dates to make sure dates are identical across variable lists
        date = pathlib.Path(path).stem.split("_")[2]

        dates_ls.append(date)
        fpaths.append(path)

    return (fpaths, dates_ls)


def create_filenames_dict(rtc_path, variables_ls):
    keys, filepaths, dates = [], [], []
    for variable in variables_ls:
        keys.append(variable)

        filespaths_list, dates_list = make_filepath_lists(rtc_path, variable)
        filepaths.append(filespaths_list)
        dates.append(dates_list)

    # make dict of variable names (keys) and associated filepaths
    filepaths_dict = dict(zip(keys, filepaths))

    # make sure that dates are identical across all lists
    assert all(lst == dates[0] for lst in dates) == True
    # make sure length of each variable list is the same
    assert len(list(set([len(v) for k, v in filepaths_dict.items()]))) == 1

    # make dict of variable names (keys) and associated filepaths
    filepaths_dict = dict(zip(keys, filepaths))
    return filepaths_dict


# ---------------------------------------------------------------------
# ----------------------- Metadata Wrangling Functions-----------------
def parse_fname_metadata(input_fname: str) -> dict:
    """Function to extract information from filename and separate into expected variables based on a defined schema."""
    # Define schema
    schema = {
        "sensor": (3, r"S1[A-B]"),  # schema for sensor
        "beam_mode": (2, r"[A-Z]{2}"),  # schema for beam mode
        "acq_date": (15, r"[0-9]{8}T[0-9]{6}"),  # schema for acquisition date
        "pol_orbit": (3, r"[A-Z]{3}"),  # schema for polarization + orbit type
        "terrain_correction_pixel_spacing": (
            5,
            r"RTC[0-9]{2}",
        ),  # schema for terrain correction pixel spacing
        "processing_software": (
            1,
            r"[A-Z]{1}",
        ),  # schema for processing software (G = Gamma)
        "output_info": (6, r"[a-z]{6}"),  # schema for output info
        "product_id": (4, r"[A-Z0-9]{4}"),  # schema for product id
        "prod_type": ((2, 6), (r"[A-Z]{2}", r"ls_map")),  # schema for polarization type
    }

    # Remove prefixs
    input_fname = input_fname.split("/")[-1]
    # Remove file extension if present
    input_fname = input_fname.removesuffix(".tif")
    # Split filename string into parts
    parts = input_fname.split("_")

    # l-s map objects have an extra '_' in the filename. Remove/combine parts so that it matches schema
    if parts[-1] == "map":
        parts = parts[:-1]
        parts[-1] = parts[-1] + "_map"

    # Check that number of parts matches expected schema
    if len(parts) != len(schema):
        raise ValueError(f"Input filename does not match schema of expected format: {parts}")

    # Create dict to store parsed data
    parsed_data = {}

    # Iterate through parts and schema
    for part, (name, (length_options, pattern_options)) in zip(parts, schema.items()):
        # In the schema we defined, items have an int for length or a tuple (when there is more than one possible lenght)
        # Make the int lengths into tuples
        if isinstance(length_options, int):
            length_options = (length_options,)
        # Same as above for patterns
        if isinstance(pattern_options, str):
            pattern_options = (pattern_options,)

        # Check that each length of each part matches expected length from schema
        if len(part) not in length_options:
            raise ValueError(f"Part {part} does not have expected length {len(part)}")
        # Check that each part matches expected pattern from schema
        if not any(re.fullmatch(pattern, part) for pattern in pattern_options):
            raise ValueError(f"Part {part} does not match expected patterns {pattern_options}")

        # Special handling of a part (pol orbit) that has 3 types of metadata
        if name == "pol_orbit":
            parsed_data.update(
                {
                    "polarization_type": part[:1],  # Single (S) or Dual (D) pol
                    "primary_polarization": part[1:2],  # Primary polarization (H or V)
                    "orbit_type": part[-1],  # Precise (p), Restituted (r) or Original predicted (o)
                }
            )
        # Format string acquisition date as a datetime time stamp
        elif name == "acq_date":
            parsed_data[name] = pd.to_datetime(part, format="%Y%m%dT%H%M%S")
        # Expand multiple variables stored in output_info string part
        elif name == "output_info":
            output_info_keys = [
                "output_type",
                "output_unit",
                "unmasked_or_watermasked",
                "notfiltered_or_filtered",
                "area_or_clipped",
                "deadreckoning_or_demmatch",
            ]

            output_info_values = [part[0], part[1], part[2], part[3], part[4], part[-1]]

            parsed_data.update(dict(zip(output_info_keys, output_info_values)))

        else:
            parsed_data[name] = part

    # Because we have already addressed product type in the variable names
    prod_type = parsed_data.pop("prod_type")
    return parsed_data


def transpose_metadata_dict_list(input_ls: list) -> dict:
    df_ls = []
    # Iterate through list
    for element in range(len(input_ls)):
        # Create a dataframe of each dict in the list
        item_df = pd.DataFrame(input_ls[element], index=[0])
        df_ls.append(item_df)
    # Combine dfs row-wise into one df
    attr_df = pd.concat(df_ls)
    # Separate out each column in df to its own dict
    attrs_dict = {col: attr_df[col].tolist() for col in attr_df.columns}
    # Acq_dates are handled separately since we will use it as an index
    acq_date_ls = attrs_dict.pop("acq_date")
    return (attrs_dict, acq_date_ls)


def create_da(value_name: str, values_ls: list, dim_name: str, dim_values: list, desc: str = None) -> xr.DataArray:
    """Given a list of metadata values, create a 1-d xr.DataArray with values
    as data that exists along a specified dimension (here, hardcoded to be
    acq_date). Optionally, add description of metadata as attr.
    Returns a xr.DataArray"""
    da = xr.DataArray(
        data=values_ls,
        dims=[dim_name],
        coords={dim_name: dim_values},
        name=value_name,
    )
    if desc is not None:
        da.attrs = {"description": desc}
    return da


def create_metadata_ds(dict_of_attrs: dict, list_of_acq_dates: list) -> xr.Dataset:
    da_ls = []
    for key in dict_of_attrs.keys():
        da = create_da(key, dict_of_attrs[key], "acq_date", list_of_acq_dates)
        da_ls.append(da)

    coord_ds = xr.combine_by_coords(da_ls)
    coord_ds = coord_ds.sortby("acq_date")
    return coord_ds


def make_coord_data(readme_fpaths_ls):
    """takes a list of the filepaths to every read me, extracts the granule ID.
    From granule ID, extracts acquisition date and data take ID.
    Returns a tuple of lists of acquisition dates and data take IDs."""

    # Make a list of all granules in time series
    granule_ls = [extract_granule_id(readme_fpaths_ls[element]) for element in range(len(readme_fpaths_ls))]
    # Define a schema for aquisition date
    schema = {
        "mission_identifier": (3, r"S1[A-B]"),  # schema for sensor
        "mode_beam_identifier": (2, r"[A-Z]{2}"),  # schema for beam mode
        "esa_product_type": (3, r"[A-Z]{3}"),  # schema for ESA product type
        "proc_lvl_class_pol": (4, r"[A-Z0-9]{{4}}"),
        "acq_start": (15, r"[0-9]{8}T[0-9]{6}"),  # schema for acquisition dat
        "acq_stop": (15, r"[0-9]{8}T[0-9]{6}"),  # schema for acquisition dat
        "orbit_num": (6, r"[0-9]{6}"),  # schema for orbit number
        "data_take_id": (6, "A-Z0-9{6}"),  # schema for data take id
    }

    # Extract relevant metadata from granule ID
    all_granules_parsed_data = []
    for granule in granule_ls:
        # need to account for double under score
        parts = [s for s in granule.split("_") if len(s) > 0]
        # parts = granule.split("_")
        single_granule_parsed_data = {}
        for part, (name, (length, pattern)) in zip(parts, schema.items()):
            if name == "acq_start":
                single_granule_parsed_data["acq_start"] = pd.to_datetime(part, format="%Y%m%dT%H%M%S")
            elif name == "orbit_num":
                single_granule_parsed_data[name] = part
            elif name == "data_take_id":
                single_granule_parsed_data[name] = part
        all_granules_parsed_data.append(single_granule_parsed_data)

    acq_dates = [granule["acq_start"] for granule in all_granules_parsed_data]
    abs_orbit_no = [granule["orbit_num"] for granule in all_granules_parsed_data]
    data_take_ids = [granule["data_take_id"] for granule in all_granules_parsed_data]

    return (acq_dates, abs_orbit_no, data_take_ids)


def extract_granule_id(filepath):
    """takes a filepath to the readme associated with an S1 scene and returns the source granule id used to generate the RTC imagery"""

    # Use markdown package to read text from README
    md = markdown.Markdown(extensions=["meta"])
    # Extract text from file
    data = pathlib.Path(filepath).read_text()
    # this text precedes granule ID in readme
    pre_gran_str = "The source granule used to generate the products contained in this folder is:\n"
    split = data.split(pre_gran_str)
    # isolate the granule id
    gran_id = split[1][:67]

    return gran_id


# metadata wrangling processor
def metadata_processor(vv_path: str, vh_path: str, ls_path: str, timeseries_type: str = "full"):
    cwd = pathlib.Path.cwd()
    tutorial2_dir = pathlib.Path(cwd).parent

    # Read VRTs
    ds_vv = xr.open_dataset(vv_path, chunks="auto").squeeze()
    ds_vh = xr.open_dataset(vh_path, chunks="auto").squeeze()
    ds_ls = xr.open_dataset(ls_path, chunks="auto").squeeze()
    # Rename vars
    ds_vv = ds_vv.rename({"band_data": "vv"})
    ds_vh = ds_vh.rename({"band_data": "vh"})
    ds_ls = ds_ls.rename({"band_data": "ls"})
    # make file paths lists for each variable

    s1_asf_data = pathlib.Path(f"../data/raster_data/{timeseries_type}_timeseries/asf_rtcs")
    # Make file path lists for vv, vh, ls
    variables_ls = ["vv", "vh", "ls_map", "readme"]
    filepaths_dict = create_filenames_dict(s1_asf_data, variables_ls)
    filepaths_vv, filepaths_vh, filepaths_ls, filepaths_rm = filepaths_dict.values()

    acq_dates_vh = [
        parse_fname_metadata(filepaths_vh[file])["acq_date"].strftime("%m/%d/%YT%H%M%S")
        for file in range(len(filepaths_vh))
    ]
    acq_dates_vv = [
        parse_fname_metadata(filepaths_vv[file])["acq_date"].strftime("%m/%d/%YT%H%M%S")
        for file in range(len(filepaths_vv))
    ]
    acq_dates_ls = [
        parse_fname_metadata(filepaths_ls[file])["acq_date"].strftime("%m/%d/%YT%H%M%S")
        for file in range(len(filepaths_ls))
    ]
    # Make sure they are identical
    assert acq_dates_vv == acq_dates_vh == acq_dates_ls, "Acquisition dates lists for VH, VV and L-S Map do not match"
    # Assign acquisition dates to band dimension and format as datetime
    ds_vv = ds_vv.assign_coords({"band": pd.to_datetime(acq_dates_vv, format="%m/%d/%YT%H%M%S")}).rename(
        {"band": "acq_date"}
    )
    ds_vh = ds_vh.assign_coords({"band": pd.to_datetime(acq_dates_vh, format="%m/%d/%YT%H%M%S")}).rename(
        {"band": "acq_date"}
    )
    ds_ls = ds_ls.assign_coords({"band": pd.to_datetime(acq_dates_ls, format="%m/%d/%YT%H%M%S")}).rename(
        {"band": "acq_date"}
    )
    # combine variables into one cube
    ds = xr.combine_by_coords([ds_vv, ds_vh, ds_ls])
    # Sort in chronological order
    ds = ds.sortby("acq_date")

    # make lists of filename metadata for each geotiff file type (vv,vh,ls)
    meta_attrs_list_vv = [parse_fname_metadata(filepaths_vv[file]) for file in range(len(filepaths_vv))]

    meta_attrs_list_vh = [parse_fname_metadata(filepaths_vh[file]) for file in range(len(filepaths_vh))]

    meta_attrs_list_ls = [parse_fname_metadata(filepaths_ls[file]) for file in range(len(filepaths_ls))]
    # make sure all identical
    assert (
        meta_attrs_list_ls == meta_attrs_list_vh == meta_attrs_list_vv
    ), "Lists of metadata dicts should be identical for all variables"

    # Transpose attr dict lists
    attr_dict, acq_dt_list = transpose_metadata_dict_list(meta_attrs_list_vv)
    # Create xr.DAs of metadata
    coord_ds = create_metadata_ds(attr_dict, acq_dt_list)
    # Assign coordinate variables
    coord_ds = coord_ds.assign_coords({k: v for k, v in dict(coord_ds.data_vars).items()})
    # Combine data  cube and metadata cube
    ds_w_metadata = xr.merge([ds, coord_ds])
    # Move some coordinate variables to be attrs
    # Make list of coords that are along time dimension
    coords_along_time_dim = [coord for coord in ds_w_metadata._coord_names if "acq_date" in ds_w_metadata[coord].dims]
    dynamic_attrs = []
    static_attr_dict = {}
    for i in coords_along_time_dim:
        if i != "acq_date":
            # find coordinate array variables that have more than
            # one unique element along time dimension
            if len(set(ds_w_metadata.coords[i].data.tolist())) > 1:
                dynamic_attrs.append(i)
            else:
                static_attr_dict[i] = ds_w_metadata.coords[i].data[0]
    # Drop static coords
    ds_w_metadata = ds_w_metadata.drop_vars(list(static_attr_dict.keys()))
    # Assign them as attrs
    ds_w_metadata.attrs = static_attr_dict
    # Adding metadata from readme
    acquisition_dates, abs_orbit_ls, data_take_ids_ls = make_coord_data(filepaths_rm)

    # Create xr.DA of data take IDs
    data_take_id_da = create_da(
        value_name="data_take_id",
        values_ls=data_take_ids_ls,
        dim_name="acq_date",
        dim_values=acquisition_dates,
        desc="ESA Mission data take ID",
    )
    # Sort
    data_take_id_da = data_take_id_da.sortby("acq_date")
    # add data take DA as coordinate variable of data cube
    ds_w_metadata.coords["data_take_ID"] = data_take_id_da

    # repeat for abs orbit
    abs_orbit_da = create_da(
        value_name="abs_orbit_num",
        values_ls=abs_orbit_ls,
        dim_name="acq_date",
        dim_values=acquisition_dates,
        desc="Absolute orbit number",
    )
    abs_orbit_da = abs_orbit_da.sortby("acq_date")
    ds_w_metadata.coords["abs_orbit_num"] = abs_orbit_da

    # Set layover shadow map as coordinate variable
    ds_w_metadata = ds_w_metadata.set_coords("ls")
    return ds_w_metadata


# --------------------------------------------------------------------
# ---------------------------utility functions -----------------------


def points2coords(pt_ls: list) -> list:  # should be [xmin, ymin, xmax, ymax]
    """
    Convert a list of points to a list of coordinates.
    Parameters
    ----------
    pt_ls : list
        A list of points in the format [xmin, ymin, xmax, ymax].
    Returns
    -------
    list
        A list of coordinates in the format [(xmin, ymin), (xmin, ymax), (xmax, ymax), (xmax, ymin), (xmin, ymin)].
    """

    coords_ls = [
        (pt_ls[0], pt_ls[1]),
        (pt_ls[0], pt_ls[3]),
        (pt_ls[2], pt_ls[3]),
        (pt_ls[2], pt_ls[1]),
        (pt_ls[0], pt_ls[1]),
    ]
    return coords_ls


def power_to_db(input_arr: np.array) -> np.array:
    """
    Convert power values to decibel (dB) scale.

    Parameters
    ----------
    input_arr : np.array
        Input array containing power values.

    Returns
    -------
    np.array
        Output array with values converted to decibel (dB) scale.
    """
    return 10 * np.log10(np.abs(input_arr))
