import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import planetary_computer
import pystac
import stackstac
import xarray as xr
from pystac_client import Client
from dask.distributed import Client as daskClient

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