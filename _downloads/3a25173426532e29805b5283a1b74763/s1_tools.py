import numpy as np
import matplotlib.pyplot as plt


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