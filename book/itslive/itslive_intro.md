# Introduction

::::{tab-set}
:::{tab-item} Overview
This tutorial contains jupyter notebooks demonstrating various steps of a typical scientific workflow including accessing, processing and visualizing remote sensing data. The structure is as follows:

**[1) Data access](nbs/1_accessing_itslive_s3_data.ipynb)**
- Access ITS_LIVE data stored as Zarr data cubes in an AWS S3 bucket.  

**[2) Reading and working with a larger-than-memory dataset](nbs/2_larger_than_memory_data.ipynb)**  
- Illustrate different strategies for manipulating and organizing a large dataset using [Xarray](https://docs.xarray.dev/en/stable/), [Zarr](https://zarr.dev/), and [Dask](https://www.dask.org/). 

**[3) Working with raster and vector data](nbs/3_combining_raster_vector_data.ipynb)**  
- Parse geographic metadata with [cf_xarray](https://cf-xarray.readthedocs.io/en/latest/).  
- Handle projections and coordinate reference system information with [GeoPandas](https://geopandas.org/en/stable/), [Rioxarray](https://corteva.github.io/rioxarray/stable/index.html) and [PyProj](https://pyproj4.github.io/pyproj/stable/).  
- Spatial subset of vector data with [GeoPandas](https://geopandas.org/en/stable/).    
- Spatial subset of raster data using vector data with [Rioxarray](https://corteva.github.io/rioxarray/stable/index.html).  

**[4) Initial inspection and analysis of velocity data for a single glacier](nbs/4_exploratory_data_analysis_single.ipynb)**
- Handle projections and coordinate reference system information with [GeoPandas](https://geopandas.org/en/stable/), [Rioxarray](https://corteva.github.io/rioxarray/stable/index.html) and [PyProj](https://pyproj4.github.io/pyproj/stable/).  
- Visualize raster and vector with background maps data using [Xarray](https://docs.xarray.dev/en/stable/), [GeoPandas](https://geopandas.org/en/stable/), and [Contextily](https://contextily.readthedocs.io/en/latest/).  
- Calculate and examine data coverage along a given dimension using Xarray label-based indexing and selection.  
- Use available metadata to interpret and organize dataset,  
     - Use [`xr.DataTree`](https://xarray-datatree.readthedocs.io/en/latest/data-structures.html) or [`groupby()`](https://docs.xarray.dev/en/stable/user-guide/groupby.html) to separate dataset using metadata,  
- Use Xarray and [`scipy.stats`](https://docs.scipy.org/doc/scipy/reference/stats.html) to calculate and visualize summary statistics along a given dimension.  
- Perform dimensional computations, reductions and visualizations using Xarray [`resample()`](https://docs.xarray.dev/en/stable/generated/xarray.Dataset.resample.html), [`groupby()`](https://docs.xarray.dev/en/stable/user-guide/groupby.html) and [`FacetGrid`](https://docs.xarray.dev/en/latest/generated/xarray.plot.FacetGrid.html).  

**[5) Exploratory analysis and visualization of multiple glaciers](nbs/5_exploratory_data_analysis_group.ipynb)**
- Combine raster and vector data into a multi-dimensional vector data cube using [Xvec](https://xvec.readthedocs.io/).  
- Read and write vector data cubes to disk using Xvec methods that rely on [cf_xarray](https://cf-xarray.readthedocs.io/en/latest/) to encode and decode metadata.  
- Interactive  visualization of vector data cube using Xvec and GeoPandas.  
- Use Xarray plotting tools to visualize data from a vector data cube.  
:::
:::{tab-item} Relevant Concepts

This tutorial will spend a lot of time discussing the following concepts, if they're unfamiliar to you, we recommend first heading to [Relevant Concepts](../background/6_relevant_concepts.md).

 1. {term}`Larger than memory data`

 2. {term}`Dask`

 3. {term}`Chunking`

:::
:::{tab-item} Learning goals

This tutorial demonstrates how to use xarray for scientific investigation of remote sensing data. By the end of this tutorial, you should be able to:

- Read Zarr data from AWS S3 cloud object stores,  
- Understand different approaches for working with larger-than-memory data,  
- Use GeoPandas to manipulate and visualize vector data,  
- Clip raster data by vector data objects using GeoPandas and RioXarray,  
- Parse geographic metadata with cf_xarray,  
- Build and use vector data cubes with Xvec,   
- Write multi-dimensional data to disk as Zarr data cubes and understand how different metadata storage can affect these operations. 
:::
:::{tab-item} Software

For instructions on setting up a computing environment needed for this tutorial, see [Software](../background/5_software.md).
:::
:::{tab-item} Data

For more background on the data used in this tutorial, head to [Tutorial Data](../background/4_tutorial_data.md).

::::

To get started with this tutorial, make sure you've followed the instructions on the [Software](../background/5_software.md) page for downloading the necessary material and setting up a virtual environment, then head to the first notebook.