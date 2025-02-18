# {{intro}}

## Overview

This tutorial focuses on data from Sentinel-1, a synthetic aperture radar (SAR) dataset containing imagery collected at C-band. Specifically, we are looking at Sentinel-1 Radiometric Terrain Corrected (RTC) imagery (for more detail on this, see [tutorial data](tutorial_data.md)). We demonstrate how to access and work with two Sentinel-1 RTC datasets as well as how to set up and perform an initial comparison between the two and time series analysis of Sentinel-1 backscatter variability. These notebooks cover:  

1) Reading and working with a very large dataset (stored locally) in memory. This includes steps such as:  
    - Reconstructing metadata lost during the read step,  
    - An alternative approach and a discussion of the strengths and limitations of each approach in the context of this dataset,  
2) Subsetting a large raster object by a vector area of interest,  
3) Inspecting a dataset using available metadata and uncertainty information,  
4) Querying and reading a dataset from cloud object storage using STAC metadata specification and STAC-specific tools such as `PySTAC` and `stackstac`,  
5) Examining two datasets that measure the same physical observable and facilitating a comparison that addresses:  
    - Differing spatial resolutions,  
    - Different uncertainty characterizations,  
    - Different types of metadata storage and handling.  

## old ch pages

The first [notebook](asf_local_vrt.ipynb) (*ASF GDAL VRT approach*) demonstrates working with data that was processed by Alaska Satellite Facility through their [Hyp3 On-Demand service](https://hyp3-docs.asf.alaska.edu/v2-transition/) and downloaded locally. 

The second [notebook](asf_inspect.ipynb) (*ASF-processed RTC data inspection*) shows preliminary dataset inspection of the ASF dataset once it has been read in and organized.

the third [notebook](PC_RTC.ipynb) (*Microsoft Planetary Computer Sentinel-1 RTC Imagery*) demonstrates accessing data from Microsoft Planetary Computer's catalog. Microsoft Planetary Computer performs RTC processing of Sentinel-1 imagery similarly to ASF. It is then made available as cloud-optimized GeoTIFFs and hosted on Microsoft Planetary Computer. This notebook demonstrates using STAC tools such as `pystac` and `stackstac` to access the cloud-hosted data locally. Microsoft Planetary Computer also hosts a jupyter hub server, which you could use instead of working with the data locally. Microsoft Planetary Computer requires a subscription (which is currently free). You can find out more about getting access [here](https://planetarycomputer.developer.azure-api.net/).

The fourth and fifth notebooks demonstrate comparing the two datasets that we prepared in the earlier chapter as well as a preliminary time series analysis of backscatter variability over time. 


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

Head to (link to notebook 1) to get started! 