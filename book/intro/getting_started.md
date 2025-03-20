# Getting started

## *How to use this book*

Our goal is for this book to be useful to users across a range of backgrounds and with different needs and interests. It is designed to be a comprehensive walk-through of scientific workflows using earth observation data in Python. At the same time, we recognize some users may be interested in following individual segments and a more modular structure. Read from start to finish or check out the individual sections that interest you. To see which topics are covered in different notebooks, check out the [tutorials overview](../background/tutorials_overview.md) page.

If you're interested in a more-detailed introduction and background on data cubes and cloud-optimized geoscience, head to the [background](../background/background_root.md) section, otherwise, head straight to the tutorials.

:::{admonition} Running tutorial notebooks on your own
Head to the [software](software.md) page for detailed instructions on how to get started running the tutorial notebooks on your own.
:::

## *Data used in this book*

Most of the examples in this book use data accessed programmatically from cloud-object storage. We make subsets of the data available in this book's Github repository to remove the need for computationally-intensive operations in the tutorials. 

Several notebooks in the second tutorial use Sentinel-1 data processed by the Alaska Satellite Facility and downloaded locally. Users who would like to follow these steps on their own may do so (and access the data [here]()), but a smaller subset of the dataset is also made available [here](). For more detail on different ways to work through the Sentinel-1 tutorial, head [here](../sentinel1/s1_intro.md), and for more background on all of the datasets used in this book see [Tutorial Data](../background/tutorial_data.md).

:::{important} 
The datasets used in these tutorials can be complicated to work with and require significant background knowledge in order to understand their limitations and how best to interpret them. **It is the responsibility of the user** to understand the physical principles that underpin remote sensing datasets and how they should be used and interpreted. See the [Tutorial Data](../background/tutorial_data.md) section for detailed discussion of these datasets and links to important background information. 
:::

## *Who is this book for?*

This book is for anyone who is interested in working with earth observation data in Python! We try to provide relevant domain and background information where necessary, and we direct the reader to helpful resources that provide more robust discussions of important concepts when appropriate. 

We provide all of the resources necessary to work through the Jupyter Notebooks contained in these tutorials on your own machine. Some experience working with Python will be helpful, however the tutorials are designed to be beginner-friendly.

```{admonition} If you'd like a more thorough background on working with geospatial data in Python 
Check out [An Introduction to Earth and Environmental Data Science](https://earth-env-data-science.github.io/intro.html), which is based on a semester-long Columbia University course titled *Research Computing in Earth Science*.
```

The tutorials in this book include discussion of different types of geospatial data, especially data cubes. We include some background information, however, if these terms are new to you, we recommend checking out the following resources before getting started: 

- [**Intro to raster data**](https://datacarpentry.github.io/organization-geospatial/01-intro-raster-data.html#data-structures-raster-and-vector) - *Data Carpentry*
- [**Intro to vector data**](https://datacarpentry.github.io/organization-geospatial/02-intro-vector-data.html#about-vector-data) - *Data Carpentry*
- [**Data cubes**](https://openeo.org/documentation/1.0/datacubes.html#what-are-datacubes) - *openEO*

## *Overview of book*

### {{part1_title}}
Background on data cubes and an introduction to array-based geoscience data and how it is represented in Xarray and Python. This section provides an overview and explanations of topics that will be referenced in the applied tutorials.

### Tutorials

Each tutorial focuses on a different type of remote sensing dataset and demonstrates how to assess and work through the nuances, details and challenges that can arise from each. A common characteristic of each dataset that is emphasized throughout the notebooks is working with larger-than-memory datasets on the computational resources of a standard laptop. 

#### Part 1: {{part2_title}}
A [tutorial](../itslive/itslive_intro.md) focusing on [ITS_LIVE](https://its-live.jpl.nasa.gov/), a NASA MEASURES project and publicly accessible dataset stored in an AWS S3 repo as Zarr data cubes. 

#### Part 2: {{part3_title}}
This [tutorial](../sentinel1/s1_intro.md) focuses on another satellite dataset: [Sentinel-1](https://www.esa.int/Applications/Observing_the_Earth/Copernicus/Sentinel-1) Radiometric Terrain Corrected imagery. Sentinel-1 is a satellite-based imaging radar. More specifically, it is a synthetic aperture radar (SAR). SAR sensor look to the side rather than straight-down like conentional optical and infrared satellite sensors. This side-looking geometry causes geometric distortions that need to be addressed prior to analysis. SAR data undergoes different types of processing for different scientific applications. Part 2 demonstrates how to access this data from two publicly available, online respositories: Alaska Satellite Facility and Microsoft Planetary Computer. These notebooks demonstrate the different ways to read this data and prepare it for analysis, as well as an initial comparison of the two datasets. 

### {{part4_title}}

A summary of the lessons learned throughout the tutorials and synthesis of these ideas into suggestions and best practices for developing scientific workflows analyzing n-dimensional earth observation data. 

