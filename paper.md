---
title: 'Educational resources to accelerate analysis of remote sensing data using cloud resources with Xarray'
tags: 
- Python
- remote sensing 
- earth science
- cryosphere
- Xarray
- cloud-hosted data
authors:
- name: Emma Marshall
orcid: 0000-0001-6348-977X
affiliation: University of Utah
- name: Deepak Cherian
orcid:  0000-0002-6861-8734 
affiliation: National Center for Atmospheric Research
- name: Scott Henderson
orcid: 0000-0003-0624-4965
affiliation: University of Washington
- name: Jessica Scheick
orcid: 0000-0002-3421-4459
affiliation: University of New Hampshire
date: 05 March 2023
bibliography: paper.bib 

---


# Statement of need

Earth system science is in the midst of a 'tool-driven revolution' facilitated by both the increasing availability of complex, large datasets and computational resources to ingest these datasets (Gentemann et al., 2021, Wagemann et al., 2021). These changes impact both the way scientific questions are formulated (data-driven discovery) and investigated (data-intensive processing and analytical methods). Recent projects highlight the need for community infrastructure and capacity building that accompanies technological advances in order to realize the full benefit of these transformations (Gentemann et al., 2021, Wagemann et al., 2021).

This submission contributes educational resources that will help scientists and students engage in the scientific process making use of large, complex, cloud-based datasets and open-source computational tools. The goal of this work is to demonstrate access and use patterns for various types of gridded, remote sensing datasets and discuss various approaches to these steps of a scientific workflow. We demonstrate this tooling in the Python computing language, focusing on the use of the Python module Xarray, which is designed for working with n-dimensional array objects with labeled indices.

# Summary

This work consists of two tutorials, in the form of Jupyter Books, that focus on using the Python package Xarray to work with satellite remote sensing data and cloud infrastructure. Each tutorial focuses on different remote sensing datasets (ITS_LIVE ice velocity data and Sentinel-1 RTC imagery) and cloud resources (Amazon Web Services (AWS) and Microsoft Planetary Computer). The Sentinel-1 tutorial also demonstrates working with and compares two different Sentinel-1 RTC datasets: RTC imagery generated using the cloud-processing resources of Alaska Satellite Facility (ASF) and imagery processed and hosted by Microsoft Planetary Computer.

The tutorials are designed to be accessible to users with a range of experience. Emphasis is placed on discussing how to interact with and examine complex, cloud-optimized datasets, rather than simply providing example code snippets. Toward this goal, the tutorials are organized into Jupyter Notebook chapters separated by topic (data access and organization, dataset inspection, and exploratory analysis). At the beginning of each notebook, two types of learning goals are articulated: high level science goals and specific techniques related to Xarray and Python. Additional, related resources are also linked.

While developing the notebooks, we placed an emphasis on narrative, explanatory text to explain concepts and coding steps along the way, with the goal of avoiding 'jargon-y' language that could be a barrier to participation for some users. Similarly, we made an effort to not only include 'working code' but, at both a conceptual and a coding level, to include mistakes and steps that didn't work, along with how to work through and resolve these issues. We believe that learning how to evaluate different conceptual approaches, as well as how to understand and resolve specific errors and issues, is a critical step to capacity building that is often overlooked in educational resources and example workflows that simply work.

By structuring these tutorials as heavily narrative and with examples of working through errors and links to outside resources, the hope is that these resources can be useful in a variety of settings. Portions of one tutorial are currently being developed into a lab exercise for students in an undergraduate course on quantitative methods in physical geography at the University of Utah. At the same time, an objective of these materials is to reduce barriers to engaging in the scientific process. The tutorials' emphasis on explanatory text and additional learning resources, given the responsibility of the data user to understand the nuances and limitations of different datasets, makes them valuable resources to independent learners and students who may not be affiliated with a course. The modular nature of the tutorials means that it will be efficient for users to identify specific areas that may be useful to them. Taken in full, the tutorials guide a novice user through each step required for developing a scientific workflow, from data access to exploratory analysis. We intentionally do not include a complete analytical scientific workflow, but instead focus on accessibility and giving users the tools to guide their own exploration and analysis of complex and exciting datasets.

### Tutorial 1: ITS_LIVE

The Inter-mission Time Series of Land Ice Velocity and Elevation (ITS_LIVE) is a dataset of global ice velocity measurements derived from displacement between pairs of satellite images generated by feature tracking algorithms. The dataset ingests Landsat 7,8,9 and Sentinel-1 & 2 image pairs and produces low-latency ice surface velocity data. It is available for access and download in multiple forms; this tutorial accesses the data stored as Zarr data cubes in s3 buckets on AWS.

Users are provided instructions outlining two ways to follow along with the tutorial material. One option is to configure a local computational environment following a provided environment.yml file. Alternatively, the tutorial has a preconfigured JupyterLab environment hosted on www.mybinder.org that enables users to run the tutorial in the cloud with no local computational resources required. 

### Tutorial 2: Sentinel-1 RTC imagery

Sentinel-1 is a synthetic aperture radar (SAR) sensor operated by the European Space Agency (ESA) that collects imaging data in C-band (~ 5 cm). Because Sentinel-1 has a side-looking viewing geometry, that data must undergo transformations and corrections in order for it to be analyzed in traditional geocoded coordinates and for the effects of distortions due to surface topography and various radiometric characteristics to be removed. This tutorial focuses on Sentinel-1 imagery that has already had the corrections (called radiometric terrain correction, RTC) applied to it. SAR datasets can be very large and unwieldy, and the RTC step can be a very computationally intensive process. We focus on two publicly available Sentinel-1 RTC datasets: 1) Microsoft Planetary Computer processed and hosted global Sentinel-1 RTC dataset for 2019-2021 stored as cloud-optimized GeoTIFFs (COGs); and 2) Alaska Satellite Facility (ASF) hosted raw Sentinel-1 SLC and GRD images with on-demand cloud processing resources for RTC and other processing needs. Imagery processed by ASF is available as COGs, though in this tutorial we demonstrate working with the dataset as locally-downloaded GeoTIFFs. 

Due to the authentication requirements of Microsoft Planetary Computer and NASA Earthdata, there is no binder instance available for this tutorial. The tutorial contains instructions to install a local computing environment as well as to download the dataset of ASF-processed Sentinel-1 RTC images that are hosted on Zenodo. Alternatively, the user can download the tutorial and run it using their own credentials.

## Tutorial Development Background

These tutorials were initially developed while Emma Marshall worked at the National Center for Atmospheric Research (NCAR) as an intern in the SIParCS (Summer Internships in Parallel Computational Sciences) program, and during the semester following the internship. The work was also supported by a NASA ROSES solicitation in the Open Source Tools, Frameworks and Libraries Program. The co-authors on this submission were internship mentors during the SIParCS program and serve as contributors and maintainers of the Xarray project in the open-source community. Each co-author was heavily involved in design and execution of the development, contributing to both the conceptual framing and technical development of both resources. 

## Tutorial repositories and material

Tutorials:
https://e-marshall.github.io/sentinel1_rtc/intro.html
https://e-marshall.github.io/itslive/intro.html 

Tutorial repositories:
https://github.com/e-marshall/sentinel1_rtc
https://github.com/e-marshall/itslive

ASF-processed Sentinel-1 RTC imagery used in tutorial: https://zenodo.org/record/7236413#.Y1rNi37MJ-0 

## References

- [From open data to open science, Earth and Space Science (2020)](https://agupubs.onlinelibrary.wiley.com/doi/epdf/10.1029/2020EA001562)
- [Science storms the cloud, AGU Advances (2021)](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2020AV000354)
- [A user perspective on future cloud-based services for Big Earth data, International Journal of Digital Earth (2021)](https://www.tandfonline.com/doi/full/10.1080/17538947.2021.1982031)
- *insert software refs*


