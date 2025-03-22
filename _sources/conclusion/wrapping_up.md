# Wrapping up

It is a popular refrain, and a sentiment many analysts can likey relate to, "that 80% of data analysis is spent on the cleaning and preparing of data" {cite:t}`Wickham_2014_Tidy,Dasu_2003_Exploratory`. This book focuses on the data cleaning and preparation steps of an analytical workflow that ingests satellite remote sensing time series datasets. We draw on the wealth of knowledge and research that attends to this topic in order to produce tutorials that demonstrate and explain these concepts in the context of cloud-optimized, publicly available array data and the software ecosystem built around the Xarray data model in Python. 

In this chapter, you will find summaries of the concepts covered throughout the Jupyter Notebooks included in this book, a return to the introduction's [discussion of data cubes](../background/data_cubes.md) with synthesis and lessons learned from the tutorials, and a short discussion of the broader context of this book and next steps for interested readers. 

## Tutorials Summary[$\tiny \nearrow$](summary.md)

This book features two tutorials, each focuses on a different earth observation dataset and containing five notebooks that cover different steps of a typical workflow such as data access, manpiulation and organizatoin and visualization and exploratory analysis. In this section, you will find a few of the common topics throughout these notebooks and links to where they are addressed in each tutorial. 

## Data cubes revisited [$\tiny \nearrow$](datacubes_revisited.md)

Synthesizing lessons from tutorial examples to enumerate guidance and best-practices for working Xarray geospatial data cubes.

## Broader context [$\tiny \nearrow$]()

It is a popular refrain, and a sentiment many analysts can likey relate to, "that 80% of data analysis is spent on the cleaning and preparing of data" {cite:t}`Wickham_2014_Tidy,Dasu_2003_Exploratory`. This book focuses on the data cleaning and preparation steps of an analytical workflow. We draw on the wealth of knowledge and research that attends to this topic in order to produce tutorials that demonstrate and explain these topics in the context of satellite remote sensing earth observation datasets and the software ecosystem built around the Xarray data model in Python.  
This book largely focused on the beginning steps of scientific workflows where data is prepared for analysis and manipulated to support different types of analysis. 

### Open source tools and packages
In this book, we mainly focused on Xarray and several tools within the Xarray ecosystem and that integrate with Xarray to streamline data cube workflows such as:
- Xvec  
- cf_xarray   
- Dask   
- PySTAC   
- stackstac   
- GeoPandas  
- holoviz

There are many exciting open-source projects and tools related to Xarray data cubes that were not highlighted in this book. A few are:
- [XRLint](https://github.com/bcdev/xrlint)
- [LexCube](https://www.lexcube.org/)
- [xcube](https://xcube.readthedocs.io/en/latest/)
- [cubo](https://github.com/ESDS-Leipzig/cubo)
- [Open Data Cube](https://opendatacube.readthedocs.io/en/latest/index.html)

