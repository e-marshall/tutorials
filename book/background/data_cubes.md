# Data cubes

The term **data cube** is used frequently throughout this book. This page contains an introduction of ***what*** a data cube is and ***why*** it is useful. 

## *I. Anatomy of a data cube*

The key object of analysis in this book is a [raster data cube](https://openeo.org/documentation/1.0/datacubes.html). Raster data cubes are n-dimensional objects that store continuous measurements or estimates of physical quantities that exist along given dimension(s). Many scientific workflows involve examining how a variable (such as temperature, windspeed, relative humidity, etc.) varies over time and/or space. Data cubes are a way of organizing geospatial data that let us ask these questions.

A very common data cube structure is a 3-dimensional object with (`x`,`y`,`time`) dimensions ({cite:t}`baumann_2017_datacube,mahecha_2020_EarthSystemData,giuliani_2019_EarthObservationOpen,montero_2024_EarthSystemData`). While this is a relatively intuitive concept,in practice, the amount and types of information contained within a single dataset and the operations involved in managing them, can become complicated and unwieldy. As analysts, we accesss data (usually from providers such as Distributed Active Archive Centers ([DAACs](https://nssdc.gsfc.nasa.gov/earth/daacs.html))), and then we are responsible for organizing the data in a way that let's us ask questions of it. While some of these decisions are straightforward (eg. *It makes sense to stack observations from different points in time along a time dimension*), some can be more open-ended (*Where and how should important metadata be stored so that it will propagate across appropriate operations and be accessible when it is needed?*). 

### *Two types of information*
Fundamentally, many of these complexities can be reduced to one distinction: is a particular piece of information a physical observable (the main focus, or target, of the dataset), or is it metadata that provides necessary information in order to properly interpret and handle the physical observable? Answering this question will help you understand how to situate a piece of information within the broader data object. 

[^mynote1]: An image collection is a set of n images, where images contain m variables or spectral bands. Band data from one image share a common spatial footprint, acquisition date/time, and spatial reference system but may have different pixel sizes. Technically, the data of bands may come from one or more files, depending on the organization of a particular data product." {cite:p}`appel_2019_ondemand`



### *Consider an example*

We have a time series of [NDVI](https://www.usgs.gov/landsat-missions/landsat-normalized-difference-vegetation-index) imagery generated from a stack of Landsat scenes. Before a user accesses a satellite imagery dataset, it has likely already undergone many levels of processing, transformation and re-organization. For more background on these steps, see Montero et al. {cite:p}`montero_2024_EarthSystemData`, *Section 3: 'The Earth System Data Cube Life cycle'*. 

In this example, we're accessing the dataset at a common dissemination point, an 'image collection'[^mynote1]. In the image collection, each satellite image contains information such as the following:  
    - Acquisition date,  
    - X-coordinate values,  
    - Y-coordinate values,  
    - A measurement for each grid cell,  
    - Important metadata structured as key-value pairs.  

It looks something like this:
```{figure} imgs/data-04-00092-g001.png
---
---
Source: [Appel & Pebesma, 2019](https://www.mdpi.com/2306-5729/4/3/92).
```

Without coordinate information and metadata, the image data are abstract arrays, meaning that we don't know anything about the spatial or temporal location of the conditions they describe.

To use this data for scientific analysis, we need to construct it into the form of a cube. This requires a comprehensive understanding of the different pieces of information contained in the dataset and how they relate to one another in order to map the components of the dataset onto a cube structure. 

```{figure} imgs/eodcaas-mosaic-data-cube-kopp.png
---
---
Source:[EOX](https://eox.at/2021/01/earth-observation-data-cubes-as-a-service/)
```

In the context of the Xarray data model, univariate data cubes can be represented by an `xr.DataArray` or a `xr.Dataset` with one `data_variable`. Multivariate data cubes should be represented by `xr.Dataset` objects. The building blocks of `xr.DataArrays` and `xr.Datasets` are dimensions, coordinates, data variables, attribues (and indexes?). We recommend the Xarray [terminology](https://docs.xarray.dev/en/stable/user-guide/terminology.html) for a detailed overview of Xarray objects and common operations.

A data cube should be organized out of these building blocks adhering to the following rules and definitions: 

:::{admonition} Xarray components of data cubes
**Dimensions** - The shape of the semantic meaning of the dataset. Frequently, `(x, y, time)`.   
**Dimensional coordinate variables** - Arrays describing the range and resolution of the data along each dimension.  
**Non-dimensional coordinate variables** - Metadata about the physical observable that varies along one or more dimensions.  
**Data variables** - Scalar values that occupy the grid cells implied by coordinate arrays. The physical observable(s) that are the focus of the dataset.  
**Attributes** - Metadata that can be assigned to a given `xr.Dataset` or `xr.DataArray` that is ***static*** along that object's dimensions.   
:::

## *II. 'Analysis-ready' data*
The process described above is an example of preparing data for analysis. Thanks to development and collaboration across the earth observation community, analysis-ready for earth observation has a specific, technical definition:

```{epigraph}
CEOS Analysis Ready Data (CEOS-ARD) are satellite data that have been processed to a minimum set of requirements and organized into a form that allows immediate analysis with a minimum of additional user effort and interoperability both through time and with other datasets.  
    - Committee on Earth Observation Satellites ([CEOS](https://ceos.org/ard/index.html)) Analysis-Ready Data {cite}`lewis_2018_CEOSAnalysisReady`
```

The development and increasing adoption of analysis-ready specifications for satellite imagery datasets is an exciting and transformative opportunity to increase the utilization of earth observation data. 

However, many legacy datasets still require significant effort in order to be considered 'analysis-ready'. Furthermore, for analysts, 'analysis-ready' can be a subjective and evolving label. Semantically, from a user-perspective, analysis-ready data can be thought of as data whose structure is conducive to scientific analysis.

## *III. Analysis-ready data cubes & this book*
The tutorials in this book contain examples of data at various degrees of 'analysis-ready'. [Tutorial 1: ITS_LIVE](../itslive/itslive_intro.md) uses a dataset of multi-sensor observations that is already organized as a `(x,y,time)` cube with a common grid. In [Tutorial 2: Sentinel-1](../sentinel1/s1_intro.md), we will see an example of a dataset that has undergone intensive processing to make it 'analysis-ready' but requires further manipulation to arrive at the `(x,y,time)` cube format that will be easist to work with. 

### References
- {cite:t}`montero_2024_EarthSystemData`
- {cite:t}`appel_2019_ondemand`
- {cite:t}`giuliani_2019_EarthObservationOpen`
- {cite:t}`truckenbrodt_2019_Sentinel1ARD`
## Additional data cube resources
- [OpenEO - Data Cubes](https://openeo.org/documentation/1.0/datacubes.html)
- [Open Data Cube initiative](https://www.opendatacube.org/about-draft)
- [The Datacube Manifesto](http://www.earthserver.eu/tech/datacube-manifesto/The-Datacube-Manifesto.pdf)

