import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd
import pathlib
import planetary_computer
import pystac
import re
import stackstac
import xarray as xr
from pystac_client import Client
from dask.distributed import Client as daskClient

#Function to extract path for target files from each scene
def extract_fnames(data_path:str, scene_name:str) -> list:
    """return a list of files associated with a single S1 scene"""
    #Make list of files within each scene directory in data directory
    scene_files_ls = os.listdir(os.path.join(data_path, scene_name))

    # Make a list to hold README files
    rm = [file for file in scene_files_ls if file.endswith("README.md.txt")]

    # Make a list to hold tif file names for each variable
    scene_files_vv = [fname for fname in scene_files_ls if fname.endswith("_VV.tif")]
    scene_files_vh = [fname for fname in scene_files_ls if fname.endswith("_VH.tif")]
    scene_files_ls = [fname for fname in scene_files_ls if fname.endswith("_ls_map.tif")]

    return scene_files_vv, scene_files_vh, scene_files_ls, rm

def make_filename_lists(asf_s1_data_path:str):

    #Make list of all scenes in dir
    scenes_ls = os.listdir(asf_s1_data_path)

    # Make empty lists to hold file paths for different variables
    fpaths_vv, fpaths_vh, fpaths_ls, fpaths_rm = [], [], [], []

    for element in range(len(scenes_ls)):
        #Extract filenames of each file of interest
        files_of_interest = extract_fnames(asf_s1_data_path, scenes_ls[element])

        # Make full path with filename for each variable
        path_vv = os.path.join(asf_s1_data_path, scenes_ls[element], files_of_interest[0][0])
        path_vh = os.path.join(asf_s1_data_path, scenes_ls[element], files_of_interest[1][0])
        path_ls = os.path.join(asf_s1_data_path, scenes_ls[element], files_of_interest[2][0])
        path_readme = os.path.join(asf_s1_data_path, scenes_ls[element], files_of_interest[3][0])

        #add a check to ensure that the files are aligned correctly
        date_vv = pathlib.Path(path_vv).stem.split('_')[2]
        date_vh = pathlib.Path(path_vh).stem.split('_')[2]
        date_ls = pathlib.Path(path_ls).stem.split('_')[2]
        date_rm = pathlib.Path(path_readme).stem.split('_')[2]
        assert date_vh == date_vv == date_ls == date_rm, 'AssertionError: File dates do not match across variables.'

        fpaths_vv.append(path_vv)
        fpaths_vh.append(path_vh)
        fpaths_ls.append(path_ls)
        fpaths_rm.append(path_readme)

    #Check that all lists are the same length
    assert len(fpaths_vv) == len(fpaths_vh) == len(fpaths_ls) == len(fpaths_rm), (
        f"Files weren't extracted correctly. Expected all lists to be the same length, received \n"
        "{len(fpaths_vv)}, {len(fpaths_vh)}, {len(fpaths_ls)}, {len(fpaths_rm)}")
    #Check that all lists are the same length
    assert len(fpaths_vv) == len(fpaths_vh) == len(fpaths_ls) == len(fpaths_rm), (
        "Files weren't extracted correctly or fname lists weren't made correctly"
            )
    return (fpaths_vv, fpaths_vh, fpaths_ls, fpaths_rm)

def extract_source_granule_pc(rtc_id):
    base_url = "https://planetarycomputer.microsoft.com/api/stac/v1/collections/sentinel-1-rtc/items/"
    full_url = base_url + str(rtc_id)
    stac_item = pystac.read_file(full_url)
    source_granule = stac_item.links[5].target[-62:]
    return source_granule

def make_granule_coord_pc(granule_ls):
    """this fn takes a list of granule IDs, extracts acq date for each granule, organizes this as an array that can be assigned as a coord to an xr obj"""

    acq_date = [pd.to_datetime(granule[17:25]) for granule in granule_ls]

    granule_da = xr.DataArray(
        data=granule_ls,
        dims=["time"],
        coords={"time": acq_date},
        attrs={
            "description": "source granule ID S1 GRD files used to process PC RTC images, extracted from STAC metadata"
        },
        name="granule_id",
    )

    return granule_da

class S1PC_DataCube:
    def __init__(self, time_range:str, bbox:list, epsg:int, collection:str='sentinel-1-rtc'):
        
        self.time_range = time_range
        self.bbox = bbox
        self.bbox_coords = points2coords(self.bbox)
        self.collection = collection
        self.epsg = epsg
        self.items = self.search_for_items()
        self.da = self.stack_assets()
        self.ds_pc = self.format_metadata()


    def search_for_items(self):

        catalog = Client.open("https://planetarycomputer.microsoft.com/api/stac/v1")
        search = catalog.search(collections=[self.collection], bbox=self.bbox, datetime=self.time_range)
        items = search.item_collection()
        return items

    def stack_assets(self):

        client = daskClient(processes=False)
        da = stackstac.stack(planetary_computer.sign(self.items), 
                             bounds_latlon=self.bbox, epsg = self.epsg)
        return da

    def format_metadata(self):

        da = self.da
        granule_ls = [
            extract_source_granule_pc(da.isel(time=t).id.values) for t in range(len(da.time))
                      ]
        granule_coord = make_granule_coord_pc(granule_ls)
        da.coords['granule_id'] = ('time', granule_coord.data)

        ds_ps = da.to_dataset(dim='band')
        return ds_pc

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


def plot_timestep(input_arr: np.array, time_step: int):
    """
    Plots VV and VH polarizations of a given dataset at a specified time step.
    Parameters
    ----------
    input_arr : np.array
        The input dataset containing the polarizations and acquisition dates.
    time_step : int
        The specific time step to plot.
    Returns
    -------
    None
        This function does not return any value. It generates and displays plots.
    Notes
    -----
    The function creates a figure with three subplots:
    - Layover-shadow mask
    - VV backscatter
    - VH backscatter
    Each subplot is titled with the acquisition date corresponding to the given time step.
    """

    date = input_arr.isel(acq_date=time_step).acq_date.dt.date.data
    fig, axs = plt.subplots(ncols=3, figsize=(24, 7))

    input_arr.isel(acq_date=time_step).ls.plot(ax=axs[0])
    power_to_db(input_arr.isel(acq_date=time_step).vv).plot(
        ax=axs[1], cmap=plt.cm.Greys_r
    )
    power_to_db(input_arr.isel(acq_date=time_step).vh).plot(
        ax=axs[2], cmap=plt.cm.Greys_r
    )
    fig.suptitle(
        f"Layover-shadow mask (L), VV (C) and VH (R) backscatter {str(input_arr.isel(acq_date=time_step).acq_date.data)[:-19]}"
    )
    axs[0].set_title(f"{date} layover-shadow map")
    axs[1].set_title(f"{date} VV backscatter")
    axs[2].set_title(f"{date} VH backscatter")

def asf_pc_sidebyside(asf_input, pc_input, timestep):
    fig, axs = plt.subplots(ncols=2, figsize=(15, 10))

    power_to_db(asf_input.vv.isel(acq_date=timestep)).plot(
        ax=axs[0], cmap=plt.cm.Greys_r, label="ASF"
    )
    power_to_db(pc_input.vv.isel(time=timestep)).plot(
        ax=axs[1], cmap=plt.cm.Greys_r, label="PC"
    )

def single_time_mean_compare(asf_input, pc_input, time):
    fig, ax = plt.subplots(figsize=(8, 8))
    power_to_db(asf_input["vv"].isel(acq_date=time).mean(dim=["x", "y"])).plot(ax=ax)
    power_to_db(pc_input["vv"].isel(time=time).mean(dim=["x", "y"])).plot(
        ax=ax, color="red"
    )