# 1.2 Learning objectives
By the end of this book, you will have familiarity with and have seen examples demonstrating the following concepts and operations: 

## *Data cubes and array data structures*
- Understanding fundamental structures of data cubes and how to organize earth observation datasets within this data model
- Using [Xarray](https://xarray.dev/) label-based indexing and selection to manipulate and organize multi-dimensional data objects
- Performing dimensional computations and visualizations with Xarray
- Visualizing and querying vector datasets with [GeoPandas](https://geopandas.org/en/stable/)
- Using [Xvec](https://xvec.readthedocs.io/en/stable/) to create and use vector datasets, combining the functionality of Xarray and GeoPandas 
- Aligning and comparing two objects with different spatial resolutions

## *Working with large datasets*
- How to read very large local data into memory using GDAL virtual format files ([VRT](https://gdal.org/en/stable/drivers/raster/vrt.html)) 
- Parallelizing local data reads with Xarray `open_mfdataset()`
- Using [Dask](https://www.dask.org/) to parallelize workflows in order to work with larger-than-memory data

## *Reading and writing data*
- Reading raster data from cloud object storage
- Handling geospatial metadata and geospatial operations involving array data using Xarray and [RioXarray](https://corteva.github.io/rioxarray/stable/index.html)
- Understanding [STAC](https://stacspec.org/en) metadata specification and how to use it to query and read data from cloud object storage
- Reading and writing [Zarr](https://zarr.readthedocs.io/en/stable/) data cubes with Xarray

