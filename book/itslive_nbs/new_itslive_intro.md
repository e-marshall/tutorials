# Using xarray to examine cloud-based glacier surface velocity data

## Overview

This tutorial contains jupyter notebooks demonstrating various steps of a typical scientific workflow including accessing, processing and visualizing remote sensing data. The structure is as follows:

1) **Data access**  
    - Access ITS_LIVE data stored as Zarr data cubes in an AWS S3 bucket
2) **Reading and working with a larger-than-memory dataset**  
    - Illustrate different strategies for manipulating and organizing a large dataset using [Xarray](https://docs.xarray.dev/en/stable/), [Zarr](https://zarr.dev/), and [Dask](https://www.dask.org/)
3) **Working with raster and vector data**  
    - Parse geographic metadata with [cf_xarray]()
    - Handle projections and coordinate reference system information with [GeoPandas](), [Rioxarray]() and [PyProj]()
    - Spatial subset of vector data with [GeoPandas]()  
    - Spatial subset of raster data using vector data with [Rioxarray]()  
4) **Initial inspection and analysis of velocity data for a single glacier**
    - Visualize raster and vector with background maps data using [Xarray](), [GeoPandas](), and [Contextily]()  
    - Calculate and examine data coverage along a given dimension using Xarray label-based indexing and selection
    - Use available metadata to interpret and organize dataset 
        - Use [`xr.DataTree`]() or [`groupby()`]() to separate dataset using metadata
    - Use Xarray and `scipy.stats` to calculate and visualize summary statistics along a given dimension
    - Perform dimensional computations, reductions and visualizations using Xarray `resample()`, `groupby()` and `FacetGrid`
5) **Exploratory analysis and visualization of multiple glaciers**
    - Combine raster and vector data into a multi-dimensional vector data cube (add glossary ref) using [Xvec]()
    - Read and write vector data cubes to disk using Xvec methods that rely on [cf_xarray]() to encode and decode metadata
    - Interactive  visualization of vector data cube using Xvec and GeoPandas
    - Use Xarray plotting tools to visualize data from a vector data cube

## Learning goals

This tutorial demonstrates how to use xarray for scientific investigation of remote sensing data. By the end of this tutorial, you should be able to:

- Read Zarr data from AWS S3 cloud object stores,  
- Understand different approaches for working with larger-than-memory data,  
- Use GeoPandas to manipulate and visualize vector data,  
- Clip raster data by vector data objects using GeoPandas and Rioxarray,  
- Parse geographic metadata with cf_xarray,  
- Build and use vector data cubes with Xvec,   
- Write multi-dimensional data to disk as Zarr data cubes and understand how different metadata storage can affect these operations.  

### Software

For instructions on setting up a computing environment needed for this tutorial, see [Software](../intro/software.md).

### Data

For more background on the data used in this tutorial, head to [Tutorial Data](../background/tutorial_data.md).

- Link to intro data page but also have description of itslive here in context of Xarray

Head to [1. Accessing cloud-hosted ITS_LIVE data](1_accessing_itslive_s3_data.ipynb) to get started! 
