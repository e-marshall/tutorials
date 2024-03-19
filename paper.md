---
title: "Educational resources to accelerate analysis of remote sensing data using cloud resources with Xarray"
tags:
  - Python
  - remote sensing
  - earth science
  - cryosphere
  - Xarray
  - cloud-hosted data
authors:
  - name: Emma Marshall
    orcid: "0000-0001-6348-977X"
    affiliation: "University of Utah"
  - name: Deepak Cherian
    orcid: "0000-0002-6861-8734"
    affiliation: "[Earthmover PBC](https://earthmover.io/)"
  - name: Scott Henderson
    orcid: "0000-0003-0624-4965"
    affiliation: "University of Washington"
  - name: Jessica Scheick
    orcid: "0000-0002-3421-4459"
    affiliation: "University of New Hampshire"
date: "05 March 2023"
bibliography: "paper.bib"
---

# Educational resources to accelerate the analysis of remote sensing data using cloud resources with Xarray

## Summary
Advancements in cloud computing, remote sensing, and engineering are transforming earth system science into an increasingly data-intensive field, requiring students and scientists to learn a broad range of new skills related to scientific programming, data management, and cloud infrastructure [@Gentemann et al:2021, @Mathieu et al:2021, @Ramachandran et al:2020, @Wagemann et al: 2021]. This submission contains educational modules designed to reduce barriers to interacting with large, complex, cloud-hosted remote sensing datasets using open-source computational tools and software. The goal of these materials is to demonstrate and promote the rigorous investigation of n-dimensional multi-sensor satellite imagery datasets through scientific programming. The tutorials in this submission feature publicly available satellite imagery with global coverage and commonly used sensors such as optical and synthetic aperture radar data with different levels of processing. We include thorough discussions of specific data formats and demonstrate access patterns for two popular cloud infrastructure platforms (Amazon Web Services and Microsoft Planetary Computer) as well as public cloud computational resources for remote sensing data processing at Alaska Satellite Facility (ASF). 

## Statement of Need
The ‘data-driven revolution’ underway in earth system sciences impacts how scientific questions are formed and investigated [@Gentemann et al:2021, @Mathieu et al:2021, @Ramachandran et al:2020, @Wagemann et al: 2021]. Such disruptive changes engender both exciting opportunities and substantial challenges in the transition to open, cloud-based science: they alter “the realm of possible questions and our ability to answer them” [@Gentemann et al:2020) and lead “to a paradigm shift of how and where data is stored as well as how users access, process and use the data [@Gil et al: 2016; @Wagemann et al:2021]. At a practical level, these changes imply a need to educate new and existing users on topics including data storage repositories, cloud computing platforms, data formats, and novel software. 

Research on the transition to data-intensive, cloud-based science highlights the need for knowledge development to accompany technological advances in order to realize the benefit of these transformations [@Gentemann et al:2021; @Guo et al:2017; @Mathieu et al:2017; @Palumbo et al:2017; @Radoˇcaj et al:2020; @Ramachandran et al:2020 & @Wagemann et al:2021]. Mathieu et al. and Palumbo et al.,  identify characteristics of effective educational resources surrounding these new technologies:  
- Discussion of the underlying remote sensing principles that shape remote sensing data and their interpretation (ie. resolution, accuracy, and signal noise),  
- Practical content about the steps required  to access and use remote sensing data stored in common data formats,  
- Demonstration of basic approaches to remote sensing data analysis such as time series analysis and,  
- Resources that are flexible, participatory, and personalized [ @Mathieu et al:2017; @Palumbo et al:2017].  
The educational modules presented in this submission address the above-identified challenges and incorporate these guidelines and principles identified in Diataxis [@Procida] in order to help analysts engage in data-driven scientific discovery using cloud-based data and open-source tools.

## Content
We present two tutorials focusing on different publicly available satellite imagery datasets that cover a range of data providers, imaging sensor types, and processing levels. Both types of satellite imagery featured in these tutorials are 1) large in volume, 2) accessed as cloud-optimized data types and making use of cloud computing resources, and 3) have associated metadata that is crucial to data management and interpretation but can be complicated to work with. 

The first tutorial focuses on Inter-mission Time Series of Land Ice Velocity and Elevation (ITS_LIVE) [@Gardner et al:2022], an ice velocity dataset composed of optical and synthetic aperture radar (SAR) imagery from Lansat 7,8 & 9  and Sentinel-1 & 2 sensors and accessed as Zarr [@Miles et al:2020] data cubes from Amazon Web Services (AWS). The second tutorial features Sentinel-1 radiometric terrain corrected (RTC) imagery. Sentinel-1 is a side-looking synthetic aperture radar sensor collecting data at C-band (~ 5cm wavelength); RTC data has undergone processing to remove the effects of geometric and radiometric distortions. Both of these datasets are novel in their volume, format, and access patterns; we believe they are indicative of future gridded remote sensing and modeled datasets, making them ideal examples for these tutorials. 

The tutorials discuss remote sensing principles and note considerations when evaluating and interpreting data, such as resolution, possible distortions, and noise. We also compare two datasets derived from the same source data but created with slightly different processing pipelines in order to illustrate the impact of dataset selection and processing decisions on analytical outcomes. 

## Instructional Design
We designed these tutorials to be accessible to users with various experiences and backgrounds. Emphasis is placed on discussing how to interact with and examine complex, cloud-optimized datasets rather than simply providing example code snippets. Toward this goal, the tutorials are organized into Jupyter Notebook chapters separated by topic (data access and organization, dataset inspection, and exploratory analysis) and with two types of explicit learning objectives articulated at the start of each chapter: high-level science goals and specific techniques related to Xarray and Python. Throughout, we link to additional learning resources and documentation that users may find beneficial. To facilitate skill building, we intentionally include errors encountered during the material development and illustrate their solutions. The code examples contained within these tutorials highlight popular, robust, and well-maintained open-source tools and software, with a strong focus on the Python module Xarray, which is designed for working with n-dimensional array objects and well-suited to geospatial applications [@Hoyer & Hamman: 2017]. In addition, we use technology such as Jupyter Books, Jupyter Notebooks, and Binder instances to make these tutorials accessible, participatory, and flexible [@Jupyter Book:2020, @Jupyter et al:2017, @Kluyver et al:2016 ]. 
Experience of use in teaching and learning situations
We aim for these resources to benefit learners in a range of settings. The ITS_LIVE tutorial has been successfully used as a lab exercise for students in an undergraduate course on quantitative methods in physical geography at the University of Utah. The tutorial focusing on Sentinel-1 RTC data has also been used in an active remote sensing course at the University of Utah. At the same time, our goal is to reduce barriers to engaging in the scientific process: the emphasis on explanatory text and additional learning resources makes the tutorials accessible to learners outside of the traditional academic setting with the in-person guidance of an instructor. This includes imparting the idea that it is the responsibility of the data user to understand the nuances and limitations of different datasets. The modular nature of the tutorials allows users to identify specific areas that may be useful to them. Taken in full, the tutorials guide a novice user through each step required for developing a scientific workflow, from data access to exploratory analysis. We intentionally do not prescribe specific conclusions, instead focusing on accessibility and giving users the tools to guide their own exploration and analysis of complex and exciting datasets.
A common sentiment of users learning to work with n-dimensional array data, particularly in earth observation applications, is difficulty experienced in the ‘data organizing’ steps of preparing a dataset for analysis (usually, coercing observations segmented in time and/or space into a data cube with x,y, and time dimensions) [@Marshall et al:2023]. The submitted tutorials place significant focus on these steps, explaining and demonstrating steps required to organize data in a way that facilitates subsequent analysis. 

## Story of the Project
The tutorials were initially developed while Emma Marshall was an intern with the Summer Internships in Parallel Computational Sciences (SIParCS) at the National Center for Atmospheric Research (NCAR). Jessica Scheick, Scott Henderson, and Deepak Cherian were internship supervisors for this project. The internship was also supported by a NASA Open Source Tools, Frameworks, and Libraries program (Award  80NSSC22K0345), with a specific focus on developing educational resources for working with cloud-hosted data using Xarray. Tutorial development continued after the conclusion of the SIParCS internship and the authors have collaborated on this project in the time since. As a graduate student researcher, Emma Marshall has had opportunities to incorporate the tutorials in teaching experiences as well as to share them with interested students outside of classroom settings. In Spring 2024, she will use the ITS_LIVE tutorial in a quantitative lab session for an undergraduate physical geography course, and she will adapt sections of both tutorials for a guest lecture on climate change and remote sensing for incarcerated students through the Salt Lake Community College Prison Education Program.

## Acknowledgments
The NCAR SIParCS program for support during the initial development of these tutorials. Professors in the Geography Department at the University of Utah for tutorial feedback and the opportunity to introduce the tutorials in classroom settings. Kevin Paul and Alan Snow for consultation during tutorial development. Alex Gardner for feedback on the use of ITS_LIVE data. Financial support from NASA Open Source Tools, Frameworks, and Libraries program and Future Investigators in Earth and Space System Science Fellowship program. Students and github users for their engagement with and feedback on these resources. 

## References
