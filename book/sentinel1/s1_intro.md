# Introduction

::::{tab-set}
:::{tab-item} Overview
This tutorial focuses on data from Sentinel-1, a synthetic aperture radar (SAR) dataset containing imagery collected at C-band. Specifically, we are looking at Sentinel-1 Radiometric Terrain Corrected (RTC) imagery (for more detail on this, see [tutorial data](tutorial_data.md)). We demonstrate how to access and work with two Sentinel-1 RTC datasets as well as how to set up and perform an initial comparison between the two and time series analysis of Sentinel-1 backscatter variability. These notebooks cover:  

**[1) Reading locally stored data](nbs/1_read_asf_data.ipynb)**
    - Strategies for reading large volumes of data stored locally into memory using [GDAL VRT objects](https://gdal.org/en/stable/drivers/raster/vrt.html).

**[2) Metadata Wrangling](nbs/2_wrangle_metadata.ipynb)**
    - Once the data is read into memory, creating an analysis-ready cube from available data and metadata

**[3) Data insepction and exploratory analysis](nbs/3_asf_exploratory_analysis.ipynb)**
    - Exploring available metadata and how it can be used to aid interpretation of data about physical observable

**[4. Access data from cloud object storage](nbs/4_read_pc_data.ipynb)**
    - Query and access data from cloud object storage that adheres to [STAC](https://stacspec.org/en) metadata specification using tools such as [PySTAC](https://pystac.readthedocs.io/) and [stackstac](https://stackstac.readthedocs.io/en/latest/)
    :::{admonition} Important information about Microsoft Planetary Computer data
    Microsoft Planetary Computer requires a subscription (which is currently free). You can find out more about getting access [here](https://planetarycomputer.developer.azure-api.net/).
    :::

**[5. Dataset comparison](nbs/5_comparing_s1_rtc_datasets.ipynb)**
    - Aligning two datasets for comparison by addressing different spatial resolutions, differences in data coverage and metadata formatting. 
:::
:::{tab-item} Relevant Concepts

## 1. [Sentinel-1 RTC imagery](../background/tutorial_data.md#sentinel-1-radiometric-terrain-corrected-rtc-imagery)
add 
:::
:::{tab-item} Learning goals

This tutorial focuses on two datasets processed from the same source satellite imagery. By the end of this tutorial you should know how to:

- Create VRT objects based on locally-downloaded files to be able to more-easily read and work with very large files in memory,  
- Use Xarray operations to organize data objects so that they sensibly store data about the target physical observable and metadata about that observable,  
- Write Xarray data to disk as Zarr data cubes,  
- Query cloud object storage catalogs that follow STAC metadata specification and use associated tools to read data into memory,  
- Use Xarray operations to align objects with similar spatial footprints but different spatial resolutions
- Use Xarray plotting methods to visualize SAR backscatter variability over spatial and temporal dimensions.  
:::
:::{tab-item} Software

For instructions on setting up a computing environment needed for this tutorial, see [Software](../intro/software.md).

:::
:::{tab-item} Data

This tutorial focuses on Sentinel-1 RTC imagery. Sentinel-1 is a Synthetic Aperture Radar (SAR) satellite sensor that collects imagery at C-band. We'll be using data that has undergone radiometric terrain correction (RTC) processing. 

:::{attention}
If you're not familiar with SAR data, head to the [tutorial data page](../background/tutorial_data.md) and check out the resources listed there. 
:::
::::

:::{attention} 
## Different ways to use this tutorial
As mentioned in the introduction, **this tutorial uses data downloaded locally.** The full dataset is quite large. You do not need to download the full time series to follow along with this tutorial. Instead, we make the full time series available as well as a subset of the time series that will take up much less space on your computer. This is only a factor in notebooks [1](nbs/1_read_asf_data.ipynb), [2](nbs/2_wrangle_metadata.ipynb), and [3](nbs/3_asf_exploratory_analysis.ipynb). All of the data needed for notebooks [4](nbs/4_read_pc_data.ipynb) and [5](nbs/5_comparing_s1_rtc_datasets.ipynb) is in the GitHub repo. 

Here are your options:  
### a. Work with a subset of the full time series.
1) If you cloned this books GitHub repository, the data should already be downloaded in the appopriate location. If you didn't clone the repo download the files located in `../sentinel1/data/subset_timeseries/asf_rtcs/`. Make sure they are in a directory on your computer with the following relative path: `sentinel1/data/subset_timeseries/asf_rtcs`.  

2) You will use this data in notebooks 1,2, and 3. **Be sure to set** `'timeseries_type' = 'subset'` and `path_to_rtcs` **at the top of each notebook**. The notebooks will not  run correctly if you don't! Also note that the text in the notebooks will have references to the full timeseries, not the subset. 

3) If you did not clone the GitHub repo, make sure that `data/subset_timeseries` also contains the following subdirectories:
        `data/subset_timeseries/txt_files/`
        `data/subset_timeseries/vrt_files`  

### b. Work with the full time series.
If you have room on your computer, you are welcome to follow the steps in this tutorial using the full time series.   
1) Download the data [here](https://zenodo.org/records/7236413).  
2) Unzip it so that its location on your computer matches the relative path: `sentinel1/data/full_timeseries/asf_rtcs`.   
3) If you cloned the GitHub repo, you should be all set. If you didn't, make sure that `sentinel1/data/full_timeseries` also has the following subdirectories:  
        `data/full_timeseries/txt_files`  
        `data/full_timeseries/vrt_files`  
:::
