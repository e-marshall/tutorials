# Introduction

## Overview

This tutorial contains jupyter notebooks demonstrating various steps of a typical scientific workflow including accessing, processing and visualizing remote sensing data. The structure is as follows:

**1) Data access**  
- Access ITS_LIVE data stored as Zarr data cubes in an AWS S3 bucket.  

**2) Reading and working with a larger-than-memory dataset**  
- Illustrate different strategies for manipulating and organizing a large dataset using [Xarray](https://docs.xarray.dev/en/stable/), [Zarr](https://zarr.dev/), and [Dask](https://www.dask.org/). 

**3) Working with raster and vector data**  
- Parse geographic metadata with [cf_xarray](https://cf-xarray.readthedocs.io/en/latest/).  
- Handle projections and coordinate reference system information with [GeoPandas](https://geopandas.org/en/stable/), [Rioxarray](https://corteva.github.io/rioxarray/stable/index.html) and [PyProj](https://pyproj4.github.io/pyproj/stable/).  
- Spatial subset of vector data with [GeoPandas](https://geopandas.org/en/stable/).    
- Spatial subset of raster data using vector data with [Rioxarray](https://corteva.github.io/rioxarray/stable/index.html).  

**4) Initial inspection and analysis of velocity data for a single glacier**
- Handle projections and coordinate reference system information with [GeoPandas](https://geopandas.org/en/stable/), [Rioxarray](https://corteva.github.io/rioxarray/stable/index.html) and [PyProj](https://pyproj4.github.io/pyproj/stable/).  
- Visualize raster and vector with background maps data using [Xarray](https://docs.xarray.dev/en/stable/), [GeoPandas](https://geopandas.org/en/stable/), and [Contextily](https://contextily.readthedocs.io/en/latest/).  
- Calculate and examine data coverage along a given dimension using Xarray label-based indexing and selection.  
- Use available metadata to interpret and organize dataset,  
     - Use [`xr.DataTree`](https://xarray-datatree.readthedocs.io/en/latest/data-structures.html) or [`groupby()`](https://docs.xarray.dev/en/stable/user-guide/groupby.html) to separate dataset using metadata,  
- Use Xarray and [`scipy.stats`](https://docs.scipy.org/doc/scipy/reference/stats.html) to calculate and visualize summary statistics along a given dimension.  
- Perform dimensional computations, reductions and visualizations using Xarray [`resample()`](https://docs.xarray.dev/en/stable/generated/xarray.Dataset.resample.html), [`groupby()`](https://docs.xarray.dev/en/stable/user-guide/groupby.html) and [`FacetGrid`](https://docs.xarray.dev/en/latest/generated/xarray.plot.FacetGrid.html).  

**5) Exploratory analysis and visualization of multiple glaciers**
- Combine raster and vector data into a multi-dimensional vector data cube using [Xvec](https://xvec.readthedocs.io/).  
- Read and write vector data cubes to disk using Xvec methods that rely on [cf_xarray](https://cf-xarray.readthedocs.io/en/latest/) to encode and decode metadata.  
- Interactive  visualization of vector data cube using Xvec and GeoPandas.  
- Use Xarray plotting tools to visualize data from a vector data cube.  

## Relevant concepts

TODO - notes on this section
- too long / too much detail?
- maybe add a figure showing how jobs distributed to workers
- maybe add a figure illustrating chunks ? 
- should this go elsewhere - maybe an 'important concepts' in the intro section for book as a whole

### Larger than memory data
Notebooks in this tutorial spend a considerable amount of time focusing on 'larger-than-memory' datasets and strategies for working with them 'in memory'. What does this mean? When we say memory, we're referring to the available CPU space, or RAM (wc: internal memory?) on whatever machine you're working on. When we're working with smaller datasets, the data and intermediate copies that are created during many operations don't exceed the internal memory available on our machine. However, as datasets increase in size, the memory required for many workflows can quickly scale and exceed the availability of most personal machines. This is what we mean when we refer to 'larger than memory' data. In the case of this tutorial, the dataset we'll be using is very large (several hundred gigabytes when uncompressed). With datasets this large, we need to employ different approaches that can be a bit more complicated than a straightforward operation that ingests and produces smaller amounts of data. 

### Dask
There are different ways to approach a dataset that is too large to load into memory. In this tutorial, we rely on the Python library, [Dask](https://www.dask.org/). Dask allows you to parallelize your workflows, breaking up a large job into many smaller jobs that can be executed in parallel rather than in sequence with one another. Parallelized jobs can be distributed across cores on an individual compputer, or across large, distributed compute nodes in cloud-computing environments. In this tutorial, we'll use Dask to parallelize and distribute jobs across one machine. Conveniently, Dask also has built-in integrations with many open-souce Python libraries, including Xarray; this means that we can specify and create Dask-backed Xarray objects within Xarray commands such as `xr.open_dataset()`, rather than needing to create them separately. 

An important aspect of Dask is that it's operations are by default 'lazy'. This means that if I have an array (`arr`) and I want to perform an operation on it (let's imagine something very simple, like multiplying the array by 5), when I execute that operation in Python (`arr * 5`), as long as it is a Dask Array (or an Xarray object backed by Dask Arrays), the computation is not actually executed *yet*. Dask uses *task scheduling* to track, orchestrate, and synchronize operations. When I call `arr * 5`, rather than calculating the resulting product, Dask adds it to a **Task Graph** (add link?). A Task Graph consist of python functions and the inputs and outputs of those functions; they are used by the program to direct how jobs should be distributed and executed across available resources in order to correctly complete the desired operation. 

So what can happen lazily and what can't? Dask will wait to evaluate a set of operations until it is explicitly instructed to do so. This can be through calling a direct method (like [`.compute()`](https://docs.dask.org/en/stable/generated/dask.dataframe.DataFrame.compute.html) or [`.persist()`](https://docs.dask.org/en/latest/generated/dask.dataframe.DataFrame.persist.html)), or an operation that cannot be accomplished lazily (like plotting an array). For more detail, check out [Dask's Managing Computation documentation](https://distributed.dask.org/en/stable/manage-computation.html).

### Chunking
Dask operates by breaking up large tasks into smaller ones. In our context, the main way this is accomplished is through [Dask Arrays](https://docs.dask.org/en/latest/array.html). If you're familiar with the Xarray data model, you'll know that the fundamental building block of a standard Xarray DataArray is a NumPy array: an `Xr.DataArray` is just a NumPy array with named dimensions and coordinates, and separate NumPy arrays describing those coordinates. 

When we introduce Dask to an Xarray workflow, we convert the underlying `.data` objects of an Xarray object from NumPy arrays to Dask Arrays. Luckily, Dask arrays aren't too unfamiliar; a Dask Array is composed of NumPy-like arrays but with an additional specification: `chunks`. Chunks tell Dask how to break up the array into smaller parts. For example, if you have a 3-dimensional Xarray DataArray, you will specify how the object should be chunked along each dimension. 

Choosing chunks can be complicated and have a significant impact on how fast your code runs. Typically, you want enough chunks that each individual chunk is relatively small and many chunks can fit into into memory. However, if you have too many chunks, Dask now needs to keep track of many individual tasks, meaning that more time will be spent managing the task graph compared to executing tasks. In addition, tasks should reflect the shape of yoour data and how you want to use it. If you're working with a space-time dataset but you're most interested in spatial analysis, having smaller chunks along the `x` and `y` dimensions will make spatial operations easier to parallelize. 

Dask and Xarray have a number of resources focused on this topic. We recommend:
- [Dask Array - Best Practices](https://docs.dask.org/en/latest/array-best-practices.html),   
- [Dask Array Chunks](https://docs.dask.org/en/stable/array-chunks.html),  
- [Choosing good chunk sizes](https://blog.dask.org/2021/11/02/choosing-dask-chunk-sizes) blog post,  
- [Xarray - Parallel Computing with Dask](https://docs.xarray.dev/en/stable/user-guide/dask.html)
    - Specifically the [Chunking and Performance](https://docs.xarray.dev/en/stable/user-guide/dask.html#chunking-and-performance) section.

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

Head to [1. Accessing cloud-hosted ITS_LIVE data](1_accessing_itslive_s3_data.ipynb) to get started! 
