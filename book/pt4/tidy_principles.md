# Principles of tidy array data
(mostly rough notes, still figuring out what this should look like)

In these tutorials, we saw a range of real-world datasets and the steps that are necessary to read them into memory and prepare them for analysis. From these examples, we can come up with guidelines for what analysis-ready data cubes look like and how to make them (fix wording). 

In the context of an Xarray `xr.Dataset` or `xr.DataArray`, below descriptions of what type of information should be represented as different structures

## Data variables

The main observations of a dataset (ie. the physical observable you're interested in) should be stored as `data_vars` of an Xarray dataset. A data variable should exist along one or multiple dimensions. If there is more than one data variable (ie. an `xr.Dataset`), those data variables should be independent; if data variables are related in some way, that should likely be represented by a dimension. 

## Dimensions
Dimensions describe the main shape of the dataset. Many objects will have `x`,`y`,`time` dimensions. However, the optimal dimensions is dependent on your use-case.

### Example: 
Sentinel-1 data cube could be represented as `xr.Dataset` with `'vv'` and `'vh'` data variables, or as `xr.DataArray` with `'band'` dimension and a single `'backscatter'` variable. Both may be appropriate, an object with `x`,`y`,`time`,`band` dimensions is likely suitable if you want to compare backscatter values between each polarization. If you want to perform operations on one polarization but not the other, then storing them as data variables is likely better. 

## Metadata
Metadata should be stored as coordinate variables or attributes depending on if it is static along the dimensions of the data cube or not. 
### Example: 
metadata wrangling notebook in sentinel tutorial

## Variable, coordinate and attr names should be self describing, follow existing conventions
### Example:
- sections where we could use cf_xarray to parse metadata, 

## Wherever possible, use existing metadata conventions such as CF, STAC
example:
- 



## Open source tools and packages
In this book, we mainly focused on Xarray and several tools within the Xarray ecosystem and that integrate with Xarray to streamline data cube workflows such as:
- Xvec, cf_Xarray, Dask, PySTAC, stackstac, GeoPandas and holoviz.

There are many more exciting open-source projects and tools related to Xarray data cubes than we were able to highlight here. A few are:
- [XRLint](https://github.com/bcdev/xrlint)
- [LexCube](https://www.lexcube.org/)
- [xcube](https://xcube.readthedocs.io/en/latest/)
- [cubo](https://github.com/ESDS-Leipzig/cubo)
- [Open Data Cube](https://opendatacube.readthedocs.io/en/latest/index.html)
