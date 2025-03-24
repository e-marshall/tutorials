# 2.3 Tutorials overview

This book contains two distinct tutorials, each of which focuses on a different cloud-optimized geospatial dataset and different cloud-computing resources. Read more about the datasets used [here](tutorial_data.md).

## *Part 1: {{part2_title}}*

This tutorial focuses on a dataset of ice velocity observations derived from satellite image pairs, using a number of different satellite sensors. This dataset is accessed as Zarr data cubes from AWS S3 cloud object storage. The notebooks in this tutorial focus on:  

1) Querying a JSON catalog and reading data from cloud object storage,
2) Working with larger-than-memory data,
3) Subsettting a larger raster data cube to an area of interest using vector data,
4) Inspecting metadata and using metadata to subset and visualize the dataset,
5) Exploratory data analysis and visulization at the scale of a single glacier

## *Part 2: {{part3_title}}*

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
    