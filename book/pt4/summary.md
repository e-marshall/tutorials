# Tutorials summary

In this book, we worked through tutorials accessing two satellite remote sensing datasets, preparing them for analysis and performing exploratory data analysis and visualization. 

## Reading and writing data
Data used in the tutorials include Zarr datacubes and cloud-optimized GeoTIFFs (COGs), which were accessed from cloud object stores such as AWS S3 asand Microsoft Planetary Computer. In addition, we analyzed data from GeoTIFF files read from local storage by creating a virtual representation of the data on disk. We also wrote `xr.Dataset` objects to disk as Zarr data cubes for later reuse. 

*See: [Reading Zarr data cubes stored in S3 buckets with Xarray](../itslive/nbs/1_accessing_itslive_s3_data.ipynb), [Handling encoding information so that Xarray objects can be written to disk](../itslive/nbs/3_combining_raster_vector_data.ipynb), [Accessing data from Microsoft Planetary Computer](../sentinel1/nbs/4_read_pc_data.ipynb), [Reading and writing vector data cubes](../itslive/nbs/5_exploratory_data_analysis_group.ipynb).*

## Larger-than-memory data
We encountered many situations where memory required to perform operations on a dataset was larger than that available on a standard laptop. This prompted us to explore strategies for more efficient memory usage such as parallelization of operations and virtualization of data.

*See: [Strategies for reading data into memory](../itslive/nbs/2_larger_than_memory_data.ipynb), [Creating a virtual copy to read a larger dataset into memory](../sentinel1/nbs/1_read_asf_data.ipynb).*

## Joining raster and vector data 

In both tutorials, we started with large spatial footprints of satellite imagery represented by raster data cubes. We explored ways to:
- Efficiently view the spatial footprint of a raster data cube by creating vector data frame of the footprint,
- Clip raster data cubes by the extent of a polygon represented by a vector data frame, and
- Create vector data cubes that hold time series data for a set of spatial areas of interest represented by polygons.

*See: [Handling raster and vector data](../itslive/nbs/3_combining_raster_vector_data.ipynb) and [Creating vector data cubes](../itslive/nbs/5_exploratory_data_analysis_group.ipynb).*

## Leverage metadata conventions and related tools
We saw many examples of situations where it would have been very difficult to access, organize and understand a given dataset without the existence of open-source tools that rely on common metadata conventions. These tools such as [cf_xarray](), [PySTAC](), and [stackstac](), make metadata more discoverable, enable vector geometries to be written to and read from disk, simplify the querying of data from large cloud, object stores and facilitate reading data from cloud object stores as analysis-ready data cubes. 

*See: [Managing CRS metadata](../itslive/nbs/3_combining_raster_vector_data.ipynb), [Reading and writing vector data cubes](../itslive/nbs/4_exploratory_data_analysis_single.ipynb), [Exploring STAC metadata](../sentinel1/nbs/4_read_pc_data.ipynb), and [Reading data from Planetary Computer](../sentinel1/nbs/4_read_pc_data.ipynb).*

## Data visualization
We used a number of visualization tools in these tutorials, each of which are appropriate for different situations and use-cases. These include interactive and static visualizations and plotting tools optimized for n-d array and vector datasets. 

*See (add links to facetgrid plot notebook examples, hvplot examples and geopandas explore examples).

## Making analysis-ready data cubes
Several notebooks focused on the tasks of organizing data cubes so that they were appropriate representations of physical observables and attaching relevant metadata to relevant variables and along appropriate dimensions.

This process, often called 'data tidying,' refers to the steps required to prepare a dataset for analysis. Depending on your data and how you want to use it, it can become quite involved. Data tidying requires a detailed understanding of both the data that you want to analyze and the 'data model' of the tools you are using to work with the data. The following page contains more discussion on tidying steps for n-dimensional array datasets.


*See: [Inspection and exploratory analysis of ice velocity data](../itslive/nbs/4_exploratory_data_analysis_single.ipynb), [Wrangle metadata of a Sentinel-1 RTC dataset](../sentinel1/nbs/2_wrangle_metadata.ipynb) and [Comparing two datasets](../sentinel1/nbs/5_comparing_s1_rtc_datasets.ipynb).*


