# Learning objectives
By the end of this book, you will have familiarity with and have seen examples demonstrating the following concepts and operations: 

## Data cubes and array data structures
- Understanding fundamental structures of data cubes and how to organize earth observation datasets within this data model
- Using Xarray label-based indexing and selection to manipulate and organize multi-dimensional data objects
- Performing dimensional computations and visualizations with Xarray
- Visualizing and querying vector datasets with GeoPandas
- Using Xvec to create and use vector datasets, combining the functionality of Xarray and GeoPandas 
- Aligning and comparing two objects with different spatial resolutions

## Working with large datasets
- How to read very large local data into memory using Gdal VRT 
- Parallelizing local data reads with Xarray `open_mfdataset()`
- Using dask to parallelize workflows in order to work with larger-than-memory data

## Reading and writing data
- Reading raster data from cloud object storage
- Handling geospatial metadata and geospatial operations involving array data using Xarray and Rioxarray
- Understanding STAC metadata specification and how to use it to query and read data from cloud object storage
- Reading and writing Zarr data cubes with Xarray

