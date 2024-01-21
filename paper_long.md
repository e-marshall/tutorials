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
affiliation: [Earthmover](https://earthmover.io/)
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

Earth system science is in the midst of a ‘tool-driven revolution’ facilitated by the increasing availability of complex, large, cloud-optimized datasets and computational resources for their storage, ingestion, and processing (Gentemann et al., 2021; Mathieu et al., 2021; Ramachandran et al., 2020 & Wagemann et al., 2021). These developments impact how scientific questions are formulated (data-driven discovery) and investigated (data-intensive processing and analysis) (Mathieu et al., 2017). Such disruptive changes engender both exciting opportunities and substantial challenges in the transition to open, cloud-based science: they alter “the realm of possible questions and our ability to answer them” (Gentemann et al., 2020) while also leading “to a paradigm shift of how and where data is stored as well as how users access, process and use the data (Wagemann et al., 2021). At a practical level, these changes imply the need for existing and new users to acquire at least some new knowledge spanning a number of areas, including data storage repositories, cloud computing platforms, data formats, and novel software tools that facilitate data processing and analysis. 

Recent research on the transition to data-intensive, cloud-based science highlights the need for community infrastructure and knowledge development to accompany technological advances in order to realize the benefit of these transformations (Gentemann et al., 2021; Guo et al., 2017; Mathieu et al., 2017; Radoˇ caj et al., 2020; Ramachandran et al., 2020 & Wagemann et al., 2021). The European Space Agency's (ESA) Earth Observation Open Science Program identifies the development of skills needed to transform large datasets into useful information as a key challenge in maximizing the benefit of earth observation data (Mathieu et al., 2017). This report highlights the need for "a radical shift in education and training" and the development of educational resources that leverage new technologies to be flexible, participatory, and personalized (Mathieu et al., 2017). Another study that focused on the use of remote sensing data to accelerate conservation science surveyed practitioners across institutional settings on the adoption of large remote sensing datasets in their research (Palumbo et al., 2017). They found that the complexity of the data relative to standard GIS data and the need for advanced computational and storage resources led to limited investment in capacity development and consequent limited incorporation of these datasets into scientific workflows. 

The authors offer suggestions for remote sensing data capacity building, emphasizing the importance of applied examples that use open-source software tools. In addition, they identify specific criteria for remote sensing data training resources, stating they “should provide (1) understanding of basic remote sensing (RS) principles and RS-derived information, (2) knowledge about how to access and use these data and products … (3) information about how the accuracy and resolution of the original raw data may affect a particular study and (4) basic principles of RS data analysis (e.g. time-series) and data formats (raster and vector datasets)” (Palumbo et al., 2017). 

Scientific research is not exempt from the same histories and systems of bias and marginalization that exist across society as a whole [Gatt, 2023 & Sultana, 2023]. This has led to a body of scientific knowledge that largely reflects the perspectives of the global North at the expense of voices and knowledge from the global South and indigenous cultures globally [Bjurstrom & Polk, 2011; Corbera et al., 2015; Gatt, 2023 & Sultana, 2023]. While computational resources may be a democratizing agent in progress toward broadening scientific participation, the economic and institutional realities of securing data storage and computational resources mean that they don’t independently imply this outcome: “while computers have undoubtedly advanced science, they have also perpetuated and strengthened some inequalities” (Gentemann et al., 2020). Maximizing the scientific and public benefits of earth observation datasets requires the reduction of barriers to participation in scientific research.

This work aims to contribute community resources that address the above-identified challenges and help analysts engage in data-driven scientific discovery using cloud-based data and open-source tools. Our tutorials feature publicly available satellite imagery datasets with global coverage that include commonly used sensors such as optical and synthetic aperture radar data and different levels of processing (a level-1 and a derived dataset). We include thorough discussions of specific data formats and demonstrate access patterns for two of the most popular cloud infrastructure platforms (Amazon Web Services and Microsoft Planetary Computer), as well as public cloud computational resources for remote sensing data processing at Alaska Satellite Facility. In addition, we discuss remote sensing principles and considerations when evaluating and interpreting data, such as resolution and possible distortions. Text and code examples within the modules focus on connecting an understanding of the physical meaning of the data with its semantic representation and developing the user's capacity to critically evaluate complex data. The code examples contained within these tutorials highlight popular, robust, and well-maintained open-source tools and software, with a strong focus on the Python module Xarray, which is designed for working with n-dimensional array objects and well-suited to geospatial applications [cite Xarray]. In addition, we use technology such as Jupyter Books, Jupyter notebooks, and binder instances to make these tutorials accessible, participatory, and flexible [Cite Jupyter …]. 

# Module Summary & Description 

This work consists of two Jupyter Books tutorials that focus on using the Python package Xarray to work with satellite remote sensing data and cloud infrastructure. Each tutorial focuses on different remote sensing datasets (ITS_LIVE ice velocity data and Sentinel-1 RTC imagery) and cloud resources (Amazon Web Services (AWS) and Microsoft Planetary Computer). The Sentinel-1 tutorial also demonstrates working with and compares two different Sentinel-1 RTC datasets: RTC imagery generated using the cloud-processing resources of Alaska Satellite Facility (ASF) and imagery processed and hosted by Microsoft Planetary Computer.

The tutorials are designed to be accessible to users with various experiences and backgrounds. Emphasis is placed on discussing how to interact with and examine complex, cloud-optimized datasets, rather than simply providing example code snippets. Toward this goal, the tutorials are organized into Jupyter Notebook chapters separated by topic (data access and organization, dataset inspection, and exploratory analysis), and with two types of explicit learning objectives articulated at the start of each chapter: high-level science goals and specific techniques related to Xarray and Python. Throughout the tutorials, we provide links to additional learning resources and documentation that users may find beneficial.

While developing the notebooks, we emphasize narrative, explanatory text to explain concepts and coding steps along the way, with the goal of avoiding 'jargon-y' language that could be a barrier to participation for some users. Similarly, we made an effort to include not only 'working code' but, at both conceptual and coding contexts, mistakes and steps that didn't work, along with how to work through and resolve these issues. We believe that learning to evaluate different conceptual approaches and understand and resolve specific errors and issues is a critical step to capacity building that is often overlooked in educational resources and example workflows that 'simply' work.

By structuring these tutorials as heavily narrative and with examples of working through errors and links to outside resources, the hope is that these resources can be helpful in various settings. Portions of one tutorial are currently being developed into a lab exercise for students in an undergraduate course on quantitative methods in physical geography at the University of Utah. The tutorial focusing on Sentinel-1 RTC data has also been used in an active remote sensing course at the University of Utah. At the same time, these materials aim to reduce barriers such as institutional affiliation to engaging in the scientific process: the tutorials' emphasis on explanatory text and additional learning resources makes them accessible to learning users outside of the traditional setting of an instructional course. The tutorials' emphasis on the responsibility of the data user to understand the nuances and limitations of different datasets makes them valuable resources to independent learners and students who may not be affiliated with a course. The modular nature of the tutorials means that it will be efficient for users to identify specific areas that may be useful to them. Taken in full, the tutorials guide a novice user through each step required for developing a scientific workflow, from data access to exploratory analysis. We intentionally do not include complete analytical scientific workflows but instead, focus on accessibility and giving users the tools to guide their own exploration and analysis of complex and exciting datasets.

## Tutorial 1: ITS_LIVE
The Inter-mission Time Series of Land Ice Velocity and Elevation (ITS_LIVE) is a dataset of global ice velocity measurements derived from displacement between pairs of satellite images generated by feature tracking algorithms. The dataset ingests Landsat 7,8,9, and Sentinel-1 & 2 image pairs and produces low-latency ice surface velocity data. It is available for access and download in multiple forms; this tutorial accesses the data stored as Zarr data cubes in s3 (Amazon Simple Storage Service) buckets on AWS (Amazon Web Services).
Users are provided instructions outlining two ways to follow along with the tutorial material. One option is configuring a local computing environment following a provided environment.yml file. Alternatively, the tutorial has a preconfigured JupyterLab environment hosted on www.mybinder.org that enables users to run the tutorial in the cloud with no local computational resources required.

## Tutorial 2: Sentinel-1 RTC imagery
Sentinel-1 is a synthetic aperture radar (SAR) sensor operated by the European Space Agency (ESA) that collects imaging data in C-band (~ 5 cm). Because Sentinel-1 has a side-looking viewing geometry, the data must undergo transformations and corrections to remove the effects of distortions due to surface topography and various radiometric characteristics and enable analysis in traditional geocoded coordinates. This tutorial focuses on Sentinel-1 imagery that has already had the corrections (radiometric terrain correction, RTC) applied. SAR datasets can be very large and unwieldy, and the RTC step can be computationally intensive. We focus on two publicly available Sentinel-1 RTC datasets: 1) Microsoft Planetary Computer processed and hosted global Sentinel-1 RTC dataset for 2019-2021 stored as cloud-optimized GeoTIFFs (COGs), and 2) Alaska Satellite Facility (ASF) hosted raw Sentinel-1 SLC and GRD images with on-demand cloud processing resources for RTC and other processing needs. Imagery processed by ASF is available as COGs, though in this tutorial, we demonstrate working with the dataset as locally downloaded GeoTIFFs.
Due to the authentication requirements of Microsoft Planetary Computer and NASA Earthdata, no binder instance is available for this tutorial. The tutorial contains instructions to install a local computing environment and download the dataset of ASF-processed Sentinel-1 RTC images hosted on Zenodo. Alternatively, users can download and run the tutorial using their credentials.

## Tutorial Development Background
These tutorials were initially developed while Emma Marshall worked at the National Center for Atmospheric Research (NCAR) as an intern in the SIParCS (Summer Internships in Parallel Computational Sciences) program during the summer of 2022 and in the academic semester following the internship. The work was also supported by a NASA ROSES solicitation in the Open Source Tools, Frameworks, and Libraries Program. The co-authors on this submission were internship mentors during the SIParCS program and serve as contributors and maintainers of the Xarray project in the open-source community. Each co-author was heavily involved in the design and execution of the tutorials, contributing to both the conceptual framing and technical development of both resources.

## Tutorial repositories and material
Tutorials: https://e-marshall.github.io/sentinel1_rtc/intro.html https://e-marshall.github.io/itslive/intro.html  
Tutorial repositories: https://github.com/e-marshall/sentinel1_rtc https://github.com/e-marshall/itslive  
ASF-processed Sentinel-1 RTC imagery used in tutorial: https://zenodo.org/record/7236413#.Y1rNi37MJ-0  

# References

Bjurström, A. & Polk, M. Physical and economic bias in climate change research: a scientometric study of IPCC Third Assessment Report. Climatic Change 108, 1–22 (2011).  
Corbera, E., Calvet-Mir, L., Hughes, H. & Paterson, M. Patterns of authorship in the IPCC Working Group III report. Nature Clim Change 6, 94–99 (2016).  
Gatt, C. Decolonizing scholarship? Plural onto/epistemologies and the right to science. Front. Sociol. 8, 1297747 (2023).  
Gentemann, C. L. et al. Science Storms the Cloud. AGU Advances 2, e2020AV000354 (2021).  
Guo, H. Big Earth data: A new frontier in Earth and information sciences. Big Earth Data 1, 4–20 (2017).  
Mathieu, P.-P. et al. The ESA’s Earth Observation Open Science Program [Space Agencies]. IEEE Geosci. Remote Sens. Mag. 5, 86–96 (2017).  
Palumbo, I. et al. Building capacity in remote sensing for conservation: present and future challenges. Remote Sens Ecol Conserv 3, 21–29 (2017).  
Radočaj, D., Obhođaš, J., Jurišić, M. & Gašparović, M. Global Open Data Remote Sensing Satellite Missions for Land Monitoring and Conservation: A Review. Land 9, 402 (2020).  
Ramachandran, R., Bugbee, K. & Murphy, K. From Open Data to Open Science. Earth Space Sci 8, (2021).  
Sultana, F. The unbearable heaviness of climate coloniality. Political Geography 99, 102638 (2022).  
Wagemann, J., Siemen, S., Seeger, B. & Bendix, J. A user perspective on future cloud-based services for Big Earth data. International Journal of Digital Earth 14, 1758–1774 (2021).  
