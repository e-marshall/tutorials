---
title: "Educational resources to accelerate analysis of remote sensing data using cloud resources with Xarray"
tags:
  - Python
  - Remote Sensing
  - Earth Science
  - Geospatial data cubes
  - Cryosphere
  - Xarray
  - Cloud-optimized data
authors:
  - name: Emma Marshall
    orcid: "0000-0001-6348-977X"
    affiliation: "1"
  - name: Deepak Cherian
    orcid: "0000-0002-6861-8734"
    affiliation: "2"
  - name: Scott Henderson
    orcid: "0000-0003-0624-4965"
    affiliation: "3"
  - name: Jessica Scheick
    orcid: "0000-0002-3421-4459"
    affiliation: "4"
  - name: Richard Forster
    orcid: "0000-0003-3945-5072"
    affiliation: "1"
affiliations:
  - name: Department of Geography, University of Utah, Salt Lake City, UT, U.S.A.
    index: 1
  - name: Earthmover PBC
    index: 2
  - name: eScience Institute & Department of Earth and Space Sciences, University of Washington, Seattle, WA, U.S.A.
    index: 3
  - name: Earth Systems Research Center, University of New Hampshire, Durham, NH, U.S.A.
    index: 4
    
date: "14 March 2025"
bibliography: "paper.bib"
---

# Summary
Advances in cloud computing, remote sensing, and engineering are transforming earth system science into an increasingly data-intensive field, requiring students and scientists to learn a broad range of new skills related to scientific programming, data management, and cloud infrastructure [abernathey_2021_cloud, @gentemann_2021_science; @mathieu_2017_esas; @ramachandran_2021_open; @wagemann_2021_user]. This work contains educational modules designed to reduce barriers to interacting with large, complex, cloud-hosted remote sensing datasets using open-source computational tools and software. The goal of these materials is to demonstrate and promote the rigorous investigation of n-dimensional multi-sensor satellite imagery datasets through scientific programming. These tutorials feature publicly available satellite imagery with global coverage and commonly used sensors such as optical and synthetic aperture radar data with different levels of processing. We include thorough discussions of specific data formats and demonstrate access patterns for two popular cloud infrastructure platforms (Amazon Web Services and Microsoft Planetary Computer) as well as public cloud computational resources for remote sensing data processing at Alaska Satellite Facility (ASF).

# Statement of Need
Research on the transition to data-intensive, cloud-based science highlights the need for knowledge development to accompany technological advances in order to realize the benefit of these transformations [@abernathey_2021_cloud; @gentemann_2021_science; @guo_2017_big; @mathieu_2017_esas; @palumbo_2017_building; @radocaj_2020_global; @ramachandran_2021_open; @sudmannsBigEarthData2020; @wagemann_2021_user].

These educational modules address this need and are guided by principles identified in Diataxis [@Procida_Diataxis_documentation_framework] in order to help analysts engage in data-driven scientific discovery using cloud-based data and open-source tools.

# Content
We present two tutorials focusing on publicly available satellite imagery datasets. Both types of satellite imagery featured in these tutorials are 1) large in volume, 2) accessed as cloud-optimized data types and making use of cloud computing resources, and 3) have associated metadata that is crucial to data management and interpretation but can be complicated to work with. 

The tutorials discuss remote sensing principles and note considerations when evaluating and interpreting data, such as resolution, possible distortions, and noise. We also compare two datasets derived from the same source data but created with slightly different processing pipelines in order to illustrate the impact of dataset selection and processing decisions on analytical outcomes. Throughout both tutorials, we emphasize the steps and skills involved with multi-dimensional data cube workflows and preparing data for analysis.

# Instructional Design
We designed these tutorials to be accessible to users with various experiences and backgrounds. Emphasis is placed on discussing how to interact with and examine complex, cloud-optimized datasets rather than simply providing example code snippets. To facilitate skill-building, we include errors encountered during the development of the material and illustrate their solutions. The code examples contained within these tutorials highlight popular, robust, and well-maintained open-source tools and software, with a strong focus on the Python module Xarray, which is designed for working with n-dimensional array objects and well-suited to geospatial applications [@Hoyer_Hamman_2017]. In addition, we use technology such as Jupyter Books, Jupyter Notebooks, and GitHub to make these tutorials accessible, participatory, and flexible [@JupyterBookCommunity_2021;@Kluyver2016jupyter].

# Experience of use in teaching and learning situations
We aim for these resources to benefit learners in a range of settings. Anecdotally, we have been contacted by a number of professors and supervisors who use the tutorials when working with students. The ITS_LIVE tutorial has been successfully used as a lab exercise for students in an undergraduate course on quantitative methods in physical geography at the University of Utah. The Sentinel-1 RTC tutorial was used in an active remote sensing course at the University of Utah. At the same time, our goal is to reduce barriers to engaging in the scientific process: the emphasis on explanatory text and additional learning resources makes the tutorials accessible to learners outside of the traditional academic setting with the in-person guidance of an instructor. This includes imparting the idea that it is the responsibility of the data user to understand the nuances and limitations of different datasets. The modular nature of the tutorials allows users to identify specific areas that may be useful to them. Taken in full, the tutorials guide a novice user through each step required for developing a scientific workflow, from data access to exploratory analysis. We intentionally do not prescribe specific conclusions, instead focusing on accessibility and giving users the tools to guide their own exploration and analysis of complex and exciting datasets. 

A common sentiment of users learning to work with n-dimensional array data, particularly in earth observation applications, is difficulty experienced in the ‘data organizing’ steps of preparing a dataset for analysis (usually, coercing observations segmented in time and/or space into a data cube with x,y, and time dimensions) [@Marshall_Cherian_Henderson_2023]. The submitted tutorials place significant focus on these steps, explaining and demonstrating operations required to organize data in a way that facilitates subsequent analysis.

# Story of the Project
The tutorials were initially developed while Emma Marshall interned with the Summer Internships in Parallel Computational Sciences (SIParCS) program at the National Center for Atmospheric Research (NCAR). Jessica Scheick, Scott Henderson, and Deepak Cherian were internship supervisors for this project. The internship was also supported by a NASA Open Source Tools, Frameworks, and Libraries program (Award  80NSSC22K0345), with a specific focus on developing educational resources for working with cloud-hosted data using Xarray. Tutorial development continued after the conclusion of the SIParCS internship and the authors have collaborated on this project in the time since with Rick Forster, one of her Ph.D. supervisors, joining the project. As a graduate student researcher, Emma Marshall has had opportunities to incorporate the tutorials in teaching experiences as well as to share them with interested students outside of classroom settings.

# Acknowledgments
The NCAR SIParCS program for support during the initial development of these tutorials. Professors in the Geography Department at the University of Utah for tutorial feedback and the opportunity to introduce the tutorials in classroom settings. Kevin Paul and Alan Snow for consultation during tutorial development. Alex Gardner for feedback on the use of ITS_LIVE data. Financial support from NASA Open Source Tools, Frameworks, and Libraries program and Future Investigators in Earth and Space System Science Fellowship program. Students and Github users for their engagement with and feedback on these resources.

# References






