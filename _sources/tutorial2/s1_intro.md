# Introduction

## Overview

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


## Learning goals

This tutorial focuses on two datasets processed from the same source satellite imagery. By the end of this tutorial you should know how to:

- Create VRT objects based on locally-downloaded files to be able to more-easily read and work with very large files in memory,  
- Use Xarray operations to organize data objects so that they sensibly store data about the target physical observable and metadata about that observable,  
- Write Xarray data to disk as Zarr data cubes,  
- Query cloud object storage catalogs that follow STAC metadata specification and use associated tools to read data into memory,  
- Use Xarray operations to align objects with similar spatial footprints but different spatial resolutions
- Use Xarray plotting methods to visualize SAR backscatter variability over spatial and temporal dimensions.  

### Software

For instructions on setting up a computing environment needed for this tutorial, see [Software](../intro/software.md).


### Data

:::{attention}
If you're not familiar with SAR data, head to the [tutorial data page](../background/tutorial_data.md) and check out the resources listed there. 

For more background on the data used in this tutorial, head to [Tutorial Data](../background/tutorial_data.md).