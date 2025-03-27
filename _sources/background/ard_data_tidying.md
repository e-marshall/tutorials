# 2.2 Analysis-ready data & preparing data for analysis

## *Data Tidying and preparing data for analysis*

The topic of *how* to prepare data for analysis has received significant attention as an area of research in itself for at least two decades {cite}`Dasu_2003_Exploratory`. Dasu & Johnson motivate their discussion with the admonishment that a failure to adequately clean one's data will almost certainly lead to flawed results, and many emphasize the considerable amount of time, effort and experience that this process can require {cite}`Dasu_2003_Exploratory, Wickham_2014_Tidy`. In the tabular data domain, '[tidy data](https://tidyr.tidyverse.org/articles/tidy-data.html)' has emerged as a way of structuring data in order to simplify subsequent analysis. In this setting, a a tidy dataset is one where"each variable is a column, each observation is a row, and each type of observational unit is a table" {cite}`Wickham_2014_Tidy`. One way of describing such an object is that the dataset's physical layout matches its semantic meaning {cite}`Wickham_2014_Tidy`. 

In the world of multi-dimensional gridded datasets, the 'data cube' structure achieves the closest symmetry between physical layout and semantic meaning {cite}`grayDataCubeRelational1996`, and has been identified as a core element of analysis-ready earth observation data {cite}`Baumann_2019_datacube, baumann_2017_datacube` 

## *'Analysis-ready' data*
The process described above is an example of preparing data for analysis. Thanks to development and collaboration across the earth observation community, analysis-ready for earth observation has a specific, technical definition:

```{epigraph}
CEOS Analysis Ready Data (CEOS-ARD) are satellite data that have been processed to a minimum set of requirements and organized into a form that allows immediate analysis with a minimum of additional user effort and interoperability both through time and with other datasets.  
    - Committee on Earth Observation Satellites ([CEOS](https://ceos.org/ard/index.html)) Analysis-Ready Data {cite}`lewis_2018_CEOSAnalysisReady`
```

The development and increasing adoption of analysis-ready specifications for satellite imagery datasets is an exciting and transformative opportunity to increase the utilization of earth observation data. 

However, many legacy datasets still require significant effort in order to be considered 'analysis-ready'. Furthermore, for analysts, 'analysis-ready' can be a subjective and evolving label. Semantically, from a user-perspective, analysis-ready data can be thought of as data whose structure is conducive to the analysis the user would like to perform.

## *Analysis-ready data cubes & this book*
The tutorials in this book contain examples of data at various degrees of 'analysis-ready'. [Tutorial 1: ITS_LIVE](../itslive/itslive_intro.md) uses a dataset of multi-sensor observations that is already organized as a `(x,y,time)` cube with a common grid. In [Tutorial 2: Sentinel-1](../sentinel1/s1_intro.md), we will see an example of a dataset that has undergone intensive processing to make it 'analysis-ready' but requires further manipulation to arrive at the `(x,y,time)` cube format that will be easiest to work with. 

