# Tutorials summary

- brief overview of different topics addressed in tutorials and links to relevant notebooks 

## Reading and writing data
In this book, we worked through tutorials accessing two satellite remote sensing datasets, preparing them for analysis and performing exploratory data analysis and visualization. Data used in the tutorials include Zarr datacubes and cloud-optimized GeoTIFFs (COGs) accessed from cloud object stores such as AWS S3 asand Microsoft Planetary Computer and GeoTIFF files read from local storage by creating a virtual representation of the data on disk. We also wrote `xr.Dataset` objects to disk as Zarr data cubes for later reuse. 

### Specific topics
- Reading Zarr data cubes stored in S3 buckets with Xarray (ITS_LIVE tutorial, [notebook 1](../tutorial1/nbs/1_accessing_itslive_s3_data.ipynb)).  
- Creating GDAL VRT objects from lists of GeoTIFF files (Sentinel-1 tutorial, [notebook 1](../tutorial2/nbs/1_read_asf_data.ipynb)).  
- Using tools such as [PySTAC]() and [stackstac]() to query and read data from Microsoft Planetary Computer (Sentinel-1 tutorial, [notebook 4](../tutorial2/nbs/4_read_pc_data.ipynb)).  
- Formatting encoding of `xr.Dataset` objects so that files can be written to disk (ITS_LIVE tutorial, [notebook 3](../tutorial1/nbs/3_combining_raster_vector_data.ipynb)).  
- Using [cf_xarray]() and [Xvec]() to read and write vector data cubes to disk (ITS_LIV Etutorial, [notebook 5](../tutorial1/nbs/5_exploratory_data_analysis_group.ipynb)).  


### Examples in notebooks

## Larger-than-memory data
- Chunking strategies for reading data into memory
- Re-chunking along given dimensions
- Using `.compute()` and `.persist()` ... 

## Joining raster and vector data
- Clip raster with vector
- Create vector dataframe by sampling raster data cube with geometries

## Leveraging metadata conventions
- cf_xarray
- PySTAC, stackstac...

## Making analysis-ready data cubes
Many sections in this book focused on connecting observations from satellite imagery such as SAR backscatter and ice velocity estimates to metadata that is necessary to inerpret the observations. This process, often called 'data tidying', requires a detailed understanding of one's data and the Xarray data model.

## Data visualization
- Xarray FacetGrid plotting
- Interactive visualizations with hvplot
- Using geopandas to make interactive map-based visualizations of vector data cubes...

