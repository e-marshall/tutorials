# Introduction

::::{tab-set}
:::{tab-item} Overview
This tutorial focuses on data from Sentinel-1, a synthetic aperture radar (SAR) dataset containing imagery collected at C-band. Specifically, we are looking at Sentinel-1 Radiometric Terrain Corrected (RTC) imagery (for more detail on this, see [tutorial data](../background/4_tutorial_data.md)). We demonstrate how to access and work with two Sentinel-1 RTC datasets as well as how to set up and perform an initial comparison between the two and time series analysis of Sentinel-1 backscatter variability. These notebooks cover:  

**[1) Reading locally stored data](nbs/1_read_asf_data.ipynb)**
    - Strategies for reading large volumes of data stored locally into memory using [GDAL VRT objects](https://gdal.org/en/stable/drivers/raster/vrt.html).

**[2) Metadata Wrangling](nbs/2_wrangle_metadata.ipynb)**
    - Once the data is read into memory, creating an analysis-ready cube from available data and metadata

**[3) Data insepction and exploratory analysis](nbs/3_asf_exploratory_analysis.ipynb)**
    - Exploring available metadata and how it can be used to aid interpretation of data about physical observable

**[4. Access data from cloud object storage](nbs/4_read_pc_data.ipynb)**
    - Query and access data from cloud object storage that adheres to [STAC](https://stacspec.org/en) metadata specification using tools such as [PySTAC](https://pystac.readthedocs.io/) and [stackstac](https://stackstac.readthedocs.io/en/latest/).    
    ***Note***: Important information about Microsoft Planetary Computer data
    Microsoft Planetary Computer requires a subscription (which is currently free). You can find out more about getting access [here](https://planetarycomputer.developer.azure-api.net/).
    

**[5. Dataset comparison](nbs/5_comparing_s1_rtc_datasets.ipynb)**
    - Aligning two datasets for comparison by addressing different spatial resolutions, differences in data coverage and metadata formatting. 
:::
:::{tab-item} Relevant Concepts

 1. [Sentinel-1 RTC imagery](../background/tutorial_data.md#sentinel-1-radiometric-terrain-corrected-rtc-imagery)
 2. {term}`Spatio-temporal Asset Catalog (STAC)`
:::
:::{tab-item} Learning goals

This tutorial works with two datasets processed from the same source satellite imagery. By the end of this tutorial you should know how to:

- Create VRT objects based on locally-downloaded files to be able to more-easily read and work with very large files in memory,  
- Use Xarray operations to organize data objects so that they sensibly store data about the target physical observable and metadata about that observable,  
- Write Xarray data to disk as Zarr data cubes,  
- Query cloud object storage catalogs that follow STAC metadata specification and use associated tools to read data into memory,  
- Use Xarray operations to align objects with similar spatial footprints but different spatial resolutions
- Use Xarray plotting methods to visualize SAR backscatter variability over spatial and temporal dimensions.  
:::
:::{tab-item} Software

For instructions on setting up a computing environment needed for this tutorial, see [Software](../background/5_software.md).

:::
:::{tab-item} Data

This tutorial focuses on Sentinel-1 RTC imagery. Sentinel-1 is a Synthetic Aperture Radar (SAR) satellite sensor that collects imagery at C-band. We'll be using data that has undergone radiometric terrain correction (RTC) processing. 

:::{attention}
If you're not familiar with SAR data, head to the [tutorial data page](../background/tutorial_data.md) and check out the resources listed there. 
:::
::::

:::{attention} 
If you haven't cloned the GitHub repository for this book yet and you want to follow the code in this tutorial, you'll need to do so now. This tutorial uses data downloaded from Zenodo (details below) as well as data contained within the GitHub repository. Instructions for  cloning the repo can be found on the [Software and computing environment](../intro/software.md) page.
:::

## Different ways to use this tutorial
**This tutorial uses data downloaded locally.** The full dataset is quite large. You do not need to download the full time series to follow along with this tutorial. Instead, we make the full time series available as well as a subset of the time series that will take up much less space on your computer. This is only a factor in notebooks [1](nbs/1_read_asf_data.ipynb), [2](nbs/2_wrangle_metadata.ipynb), and [3](nbs/3_asf_exploratory_analysis.ipynb). All of the data needed for notebooks [4](nbs/4_read_pc_data.ipynb) and [5](nbs/5_comparing_s1_rtc_datasets.ipynb) is in the GitHub repo. 

{{break}}

### Dataset options

The Sentinel-1 RTC scenes processed by ASF used in this tutorial are stored in a Zenodo [record](https://zenodo.org/records/15036782). You can manually download the data and move it to the correct location or use provided code to download the necessary data programmatically. The sections below have detailed information on each option and how to download the data.

#### 1. Work with a **subset** of the time series.
This option includes 5 Sentinel-1 scenes and the downloaded data will take up ~ 3 GB on your computer. If you use this option, make sure that the `timeseries_type` variable in each notebook is set to `'subset'`. Keep in mind that the text in the notebooks refers to the full time series, so there will be discrepancies in some of the references. Notebook 3 of this tutorial involves subsetting the full spatial extent of the time series to a smaller area of interest and writing it to disk so that it can be used in notebook 5. This object is made available in the GitHub repo for this book. If you cloned the GitHub repo, you should have everything you need to execute notebook 5. 

##### Manual data download

1. Go to the Zenodo record and click the `'Download'` button for `asf_rtcs_subset.zip`. 
2. Once the download completes, extract the data from the zip file and move it to the following location: `cloud_os_geospatial_datacube_workflows/book/sentinel1/data/raster_data/subset_timeseries`.
For example, if I downloaded the zip file to my `'Downloads'` and extracted it there, its path would look something like this: 
    `/home/my_user/Downloads/asf_rtcs_subset`
And I could move it to the appropriate location like this:
    `mv /home/my_user/Downloads/asf_rtcs_subset/.  /home/my_user/Desktop/work/cloud_os_geospatial_datacube_workflows/book/sentinel1/data/raster_data/subset_timeseries/`

##### Programmatic data download

1. Go do the [Data download notebook](nbs/download_zenodo_data_curl.ipynb).
2. Execute the cell with package imports and the two cells in the 'Subset timeseries' section.
3. Wait for the data to download. 

Once the download completes, head to the first notebook to get started.

{{break}}

#### 2. Work with the **full** time series.
This option includes 103 Sentinel-1 scenes that are approximately 47 GB. If you're working on a machine with a large amount of space and would like to follow along with these steps of the tutorial you can do so but, once again, **it is not necessary to download the full time series!**. See the 'Downloading data' section below for more information and be sure to set `timeseries_type = 'full'` if you use the programmatic option. 

##### Manual data download

1. Go to the Zenodo record and click the `'Download'` button for `asf_rtcs.zip`. 
2. Once the download completes, extract the data from the zip file and move it to the following location: `cloud_os_geospatial_datacube_workflows/book/sentinel1/data/raster_data/full_timeseries`.
For example, if I downloaded the zip file to my `'Downloads'` and extracted it there, its path would look something like this: 
    `/home/my_user/Downloads/asf_rtcs`
And I could move it to the appropriate location like this:
    `mv /home/my_user/Downloads/asf_rtcs/.  /home/my_user/Desktop/work/cloud_os_geospatial_datacube_workflows/book/sentinel1/data/raster_data/full_timeseries/`

##### Programmatic data download

1. Go do the [Data download notebook](nbs/download_zenodo_data_curl.ipynb).
2. Execute the cell with package imports and the two cells in the 'Full timeseries' section.
3. Wait for the data to download. 

Once the download completes, head to the first notebook to get started.



