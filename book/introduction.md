# Cloud-native geospatial data cube workflows with open-source tools


Welcome to `Cloud-native geospatial data cube workflows with open-source tools`! This book demonstrates steps of typical scientific workflows involving earth observation data with a focus on cloud-optimized data formats, larger-than memory data, and manipulating multi-dimensional datasets to prepare them for analysis.

We focus on data derived from different types of satellite imagery that are publicly available in cloud-hosted repositories such as [AWS S3](https://aws.amazon.com/s3/). The tutorials are composed of Jupyter Notebooks that demonstrate how to work with these datasets in Python using software packages from the popular [Pangeo](https://www.pangeo.io/) ecosystem that are built on and around the [Xarray](https://xarray.dev/) data model. 

The goal of this book is to reduce barriers to entry to working with earth observation data for scientific analysis. It features two stand-alone tutorials, each detailing steps involved in a typical workflow, from data access and organization to exploratory data analysis and visualization. 

Underpinning these examples is a focus on understanding the different components of n-dimensional, gridded datasets, how they relate to the tools we use to work with them (in this case, the Python package Xarray), and how a strong understanding of a scientific dataset within the context of your chosen data model can enable more efficient and intuitive analysis.

{{break}}

```{figure} background/imgs/cube.png
:width: 75%

Illustration of a Xarray 3-d data cube.
```