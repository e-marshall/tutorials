# 2.4 Data used in tutorials

We use many different datasets throughout these tutorials. While each tutorial is focused on a different raster time series (ITS_LIVE ice velocity data and Sentinel-1 imagery), we also use vector data to represent points of interest. 

Most of the examples in this book use data accessed programmatically from cloud-object storage. We make subset of the data available in this books Github repository to remove the need for computationally-intensive operations in the tutorials. In one example, working with Sentinel-1 data processed by Alaska Satellite Facility, we start with data downloaded locally. Users who would like to complete this processing step on their own may do so (and access the data [here](https://zenodo.org/records/15036782)), but a smaller subset of this data is stored in the repository. 

Here is a broad overview the data included in this tutorial, including how it is collected, it's potential scientific applications, and how and where it is stored and accessed in these tutorials. 

## *Inter-mission Time Series of Land Ice Velocity and Elevation (ITS_LIVE)*

| Dataset name | Produced by | Storage format | Storage location |
| :-----------:|:---------- | :------------- | :--------------- |
| ITS_LIVE | [ITS_LIVE project, NASA JPL](https://its-live.jpl.nasa.gov/) | Zarr | AWS S3|


ITS_LIVE is a dataset of ice velocity observations derived from applying a feature tracking algorithm to pairs of satellite imagery. Ice velocity refers to the down-slope movement of glaciers and ice sheets {cite}`Gardner_Scambos_2022`. Because glaciers and ice sheets are dynamic elements of our climate system, they lose or gain mass in response to changes in climate conditions such as warmer temperatures or increased snowfall, measuring variability in the speed of ice flow can help scientists better understand trends in glacier dynamics and interactions between glaciers and climate. 

```{figure} imgs/lopez06-3341335.png
---
---
Example of a ice velocity time series along centerline profile of Malaspina Glacier featuring velocity observations from a range of satellite sensors. Source: Reproduced with permission from {cite:t}`lopez_2023_itslive`.
```

Part of what is so exciting about ITS_LIVE is that it combines image pairs from a number of satellites, including imagery from optical (Landsat 4,5,7,8,9 & Sentinel-2) and synthetic aperture radar (Sentinel-1) sensors. For this reason, ITS_LIVE time series data can be quite large. Another exciting aspect of the ITS_LIVE dataset is that the image pair time series data is made available as Zarr data cubes stored in cloud object storage on Amazon Web Services (AWS), meaning that users don't need to download massive files to start working with the data! 

ITS_LIVE produces a number of data products in addition to the image pair time series that we use in this tutorial, and provides different options to access the data. Check them out [here](https://its-live.jpl.nasa.gov/#access). 

**Documentation & References**:  
Be sure to also check out the ITS_LIVE image pair velocities [documentation](http://its-live-data.jpl.nasa.gov.s3.amazonaws.com/documentation/ITS_LIVE-Landsat-Scene-Pair-Velocities-v01.pdf) and papers on the ITS_LIVE processing methodology:
- [Autonomous Repeat Image Feature Tracking (autoRIFT) and its application for tracking ice displacement](https://www.mdpi.com/2072-4292/13/4/749). {cite}`lei_2021_AutonomousRepeatImage`
- [Processing methodology for the ITS_LIVE Sentinel-1 ice velocity products](https://doi.org/10.5194/essd-14-5111-2022). {cite}`Lei_2022_Processing`

**Further reading on ice velocities**: 
- [NASA/USGS Provide Global View of Speed of Ice](https://www.jpl.nasa.gov/news/nasausgs-provide-global-view-of-speed-of-ice/)


## *Sentinel-1 Radiometric Terrain Corrected (RTC) imagery*

Part 2 focuses on Sentinel-1 Radiometric Terrain Corrected imagery. Sentinel-1 is a dataset of synthetic aperture radar (SAR) imagery collected from sensors located on satellites operated by the Sentinel satellites operated by the European Space Agency (ESA). SAR data is exciting because doesn't require solar illumination like passive optical systems and, at the wavelength where Sentinel-1 imagery is collected, it is minimally impacted by atmospheric water vapor, meaning that Sentinel-1 can acquire clear images of Earth's surface even during cloudy and nighttime conditions. SAR imagery has a wide range of scientific applications including monitoring land surface deformation related to seismic activities, tracking flooding extents following extreme weather events, and mapping deforestation and characterizing biomass. 

:::{tip}
For an in-depth example of how SAR backscatter data can be used to map flooding extent, check out this [notebook](https://projectpythia.org/eo-datascience-cookbook/notebooks/tutorials/floodmapping.html) in the [Project Pythia Earth Observation Data Science Cookbook](https://projectpythia.org/eo-datascience-cookbook/README.html).
:::

Because SAR imagery is collected from a side-looking sensor, it can contain distortions related to the viewing geometry of the sensor and the surface topography of the area being imaged. This tutorial focuses on RTC imagery, which is SAR data that has undergone processing to remove the above-mentioned distortions. 

Multiple algorithms perform radiometric terrain correction, and it is important to understand the components of whichever dataset you use and their relative benefits and tradeoffs. This book will demonstrate working with two different (but similar) datasets of Sentinel-1 RTC imagery: one produced by Alaska Satellite Facility and one produced by Microsoft Planetary Computer, shown below. Processing of SAR imagery can be very computationally intensive, both of these options leverage cloud-hosted computational resources to make processed SAR imagery available to users, reducing the need for individual users to perform complicated, resource and time-intensive processing. 


:::{important} 
If you are unfamiliar with the principles of synthetic aperture radar (SAR) imaging and processing, we *strongly* recommend pausing this tutorial and checking out some of the very thorough and detailed SAR resources that are publicly available such as the [SAR Handbook](https://gis1.servirglobal.net/TrainingMaterials/SAR/SARHB_FullRes.pdf) by NASA SERVIR (specifically Ch.2), NASA EarthData Earth Observation Data Basics ([SAR](https://www.earthdata.nasa.gov/learn/earth-observation-data-basics/sar), [SAR Image Interpretation](https://www.earthdata.nasa.gov/learn/earth-observation-data-basics/sar/image-interpretation), [Types of SAR Products](https://www.earthdata.nasa.gov/learn/earth-observation-data-basics/types-sar-products)), ASF's [Introduction to SAR](https://hyp3-docs.asf.alaska.edu/guides/introduction_to_sar/) and [ASF Sentinel-1 RTC Product Guide](https://hyp3-docs.asf.alaska.edu/guides/rtc_product_guide/). 

We provide a very brief overview of RTC processing below but it is not intended to replace the aforementioned resources.
:::

```{figure} imgs/SARticle_first-fig_redone-06.jpg
---
height: 250 px
figclass: margin-caption
name: SAR diagram
---
Schematic of observation geometry used to form a SAR image.  
Credit: [NASA EarthData / NASA SAR Handbook](https://www.earthdata.nasa.gov/learn/earth-observation-data-basics/sar).
```

SAR data is collected in slant range, which is the viewing geometry of the side-looking sensor and has two dimensions: range and azimuth. These are the along-track and across-track directions of the imaged swath. As data is transformed from radar coordinates (slant range) to geocoded coordinates, the spaces represented by individual pixels in the two coordinate systems do not always align, and distortions can arise due to certain viewing angle geometries and surface topography features. In addition, radiometric distortion can arise due to scattering responses from multiple scattering features within a single pixel. Radiometric terrain correction is a processing step that accounts for these distortions and the transformation from radar to geocoded coordinates that prepares SAR data for analysis.

### Sentinel-1 RTC datasets
::::{tab-set}
:::{tab-item} Alaska Satellite Facility


| Dataset name | Producer | Storage format | Storage location |
| :-----------:|:---------- | :------------- | :--------------- |
| Sentinel-1 RTC | [Alaska Satellite Facility](https://asf.alaska.edu/) | COG (locally as GeoTIFF) | Local |
 

We use Sentinel-1 RTC imagery processed by Alaska Satellite Facility's Hybrid Pluggable Processing Pipeline (**HyP3**) {cite}`hogenson_2024_10903242`. This is a processing platform that allows users to perform processing steps necessary for analysis-ready SAR data through ASF. 

From the [ASF HyP3 Documentation](https://hyp3-docs.asf.alaska.edu/): 
HyP3 is a service for processing Synthetic Aperture Radar (SAR) imagery that addresses many common issues for users of SAR data:  
- Most SAR datasets require at least some processing to remove distortions before they are analysis-ready  
- SAR processing is computing-intensive  
- Software for SAR processing is complicated to use and/or prohibitively expensive  
- Producing analysis-ready SAR data has a steep learning curve that acts as a barrier to entry  

HyP3 solves these problems by providing a free service where people can request SAR processing on-demand. These processing requests are picked up by automated systems, which handle the complexity of SAR processing on behalf of the user. HyP3 doesn't require users to have a lot of knowledge of SAR processing before getting started; users only need to submit the input data and set a few optional parameters if desired. With HyP3, analysis-ready products are just a few clicks away.


The data in this tutorial was processed using HyP3 {cite}`andrew_johnston_2022_6629125` and then published via Zenodo [here](https://zenodo.org/records/7236413#.Y1rNi37MJ-0). For more on how to use HyP3 for your own data processing needs, check out their [tutorials page](https://hyp3-docs.asf.alaska.edu/tutorials/). 
:::

:::{tab-item} Microsoft Planetary Computer

| Dataset name | Producer | Storage format | Storage location |
| :-----------:|:---------- | :------------- | :--------------- |
| Sentinel-1 RTC | [Microsoft Planetary Computer](https://planetarycomputer.microsoft.com/) | Cloud-optimized GeoTIFF (COG) | Microsoft Azure |

In contrast to ASF's HyP3 SAR data processing service, Microsoft Planetary Computer hosts an already-processed global Sentinel-1 RTC dataset, which we will use in this tutorial. Read more about Planetary Computer's Sentinel-1 RTC product [here](https://planetarycomputer.microsoft.com/dataset/sentinel-1-rtc).
:::

::::

Further reading on SAR data and Sentinel-1: 
- [ESA Sentinel-1 documentation](https://sentinel.esa.int/web/sentinel/user-guides/sentinel-1-sar/overview)
- [ASF Introduction to SAR](https://hyp3-docs.asf.alaska.edu/guides/introduction_to_sar/)
- [NASA Earth Observation Data Basics - SAR](https://www.earthdata.nasa.gov/learn/earth-observation-data-basics/sar#toc-resources)
- [University of Alaska Fairbanks - Microwave Remote Sensing](https://radar.community.uaf.edu/)
- Mathematical tutorial on SAR {cite}`cheney_SAR_2001`, publicly available via NASA [EarthData](https://www.earthdata.nasa.gov/s3fs-public/2024-06/sar%20mathematical%20tutorial.pdf)

## *Vector data*

### Randolph Glacier Inventory version 7 (RGI7) glacier outlines 

| Dataset name | Producer | Storage format | Storage location |
| :-----------:|:---------- | :------------- | :--------------- |
| Randolph Glacier Inventory | [RGI Consortium](https://www.glims.org/RGI/) | Shapefile | NSIDC |

The Randolph Glacier Inventory (RGI) is a community-driven public dataset that provides outlines and auxiliary information such as area, length and aspect of glaciers across the world {cite}`RGI_Consortium_2023`. RGI is a subset of the Global Land Ice Measurements from Space ([GLIMS](https://www.glims.org/)) initiative and RGI data is hosted by the National Snow and Ice Data Center ([NSIDC](https://nsidc.org/data/nsidc-0770/versions/7)). Read more about the RGI project [here](http://www.glims.org/rgi_user_guide/01_introduction.html).


:::{admonition} RGI data used in this tutorial
The link above brings you to the NSIDC data access point for all RGI data. The examples in this tutorial focus areas of interest in High Mountain Asia. We have made available the subset of RGI data covering only these regions that is used in the tutorials in case users would like to use that instead. It is stored as a [GeoParquet](https://geoparquet.org/) file in the repository associated with these tutorials.
:::