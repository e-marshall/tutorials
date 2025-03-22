# Notebook summaries

## ITS_LIVE Tutorial

### 1. Access data
A. Overview of ITS_LIVE data
- dimensions, variables, attrs etc.
- metadata naming conventions > CF 
B. Read ITS_LIVE data
- overview of how ITS_LIVE is stored on s3
- read into memory (create xr.dataset)
- check spatial footprint
C. Query itslive catalog
- find url for a given point
- read into memory
- visualize footprint with hvplot
### 2. Larger than memory data
A. Compare approach for reading
- chunks='auto'
- chunks={}
- time dim out of order
- read without dask
B. Organize data
- sort along time dim
- convert to dask

### 3. Handling raster and vector data
A. Read without dask
B. Incorporate vector data
- reproject 
- examine crs metadata
- visualize
- crop vector with raster
C. Combine raster and vector (Crop raster by vector)
- Write xr.Dataset to zarr
### 4. Exploratory analysis - one glacier
A. Data exploration
- load and vis
- check coverage along a dim
- break down by sensor
B. Compare different satellites
- data tree
- groupby
C. Examine velocity variability
- histograms, summary stats
- spatial velocity variablity
D. computations along time dimension
- temporal resampling 
- seasonal analysis

### 5. Exploratory analysis - many glaciers
A. Read and organize data
- chunk, resample, reproject raster data
- read, subset, reproject vector data
B. Combine raster, vector data 
- make vector data cube
- add attr data to vector cube
- write vector cube
C. Visualize data
- read into memory
- visualize velocity data (interactive)
- visualize velocity data w/ attr data

## Sentinel-1 RTC Tutorial
### 1. Read ASF data
A. Prepare to read data
- Make txt files with lists of paths for each file
- Make VRT objects
B. Read data
- look at chunking
### 2. Wrangle metadata
A. Read data, look at initial metadata
- not much metadata on read
    - Use cf_xarray
- rename variables
B. Add metadata from file name
- parse file name
- extract, format acq dates
- combine single variable data cubes
C. Time-varying metadata
- rest of info from file name
- reorganize lists of metadata dicts (Transpose dicts to the shape that Xarray expects)
- Create xr.Dataset with metadata as coord vars
- combine data xr.Dataset with metadata xr.Dataset
D. Add metadata from README
- extract granule id from readme
- build xr.DA with granule id
E. add 3-d metadata
### 3. Exploratory analysis
A. Read and prepare data
- format metadata, clip by vector
B. layover shadow mask
- use this raster data to interpret physical observable 
C. orbital direction
- assign orbital direction as coord variable
D. duplicate time steps
- id duplicate time steps
- look at them
- drop them
E. Data visualization
- mean backscatter over time
    - unlinked colorscales when plotting vv, vh as variables
    - can 'link' them automatically by creating a `'band'` dim 
        - ie. data cube has one variable ('backscatter'), vv and vh are both elements along the `'band'` dim
- Seasonal backscatter variability 
- backscatter time series
### 4. Read Microsoft PC S1 data
A. Connect to PC
- explore stac metadata
B. Read data w/ Xarray
- dask distributed
- stackstac
- inspect dataset 
C. visualize dataset 
- ascending and descending passes
- variability over time
- seasonal variability
### 5. Compare datasets
a. read + prepare
- read data
- check crs
b. ensure direct comparison
- check that orbit numbers match
- spatial resolution differences
- mask missing data
c. combine objects
- expand dims
- combine_by_coords
d. visualize

