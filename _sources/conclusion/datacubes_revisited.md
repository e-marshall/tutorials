# 5.3 Data Cubes Revisited

In this book, we saw a range of real-world datasets and the steps required to prepare them for analysis. Several guiding principles for assembling and using analysis-ready data cubes in Xarray can be drawn from these examples.

Let's first return to the Xarray building blocks described in the background [section](../background/data_cubes.md); we can now provide more-detailed definitions of what they are and how they should be used:

:::{admonition} Xarray components of data cubes
**[Dimensions](https://docs.xarray.dev/en/latest/user-guide/terminology.html#term-Dimension)** - What is the shape of the data as you understand it? This should be the set of dimensions. Frequently, `(x, y, time)`.   
**[Dimensional coordinate variables](https://docs.xarray.dev/en/latest/user-guide/terminology.html#term-Dimension-coordinate)** - 1-d arrays describing the range and resolution of the data along each dimension.  
**[Non-dimensional coordinate variables](https://docs.xarray.dev/en/latest/user-guide/terminology.html#term-Non-dimension-coordinate)** - Metadata about the physical observable that varies along one or more dimensions. These can be 1-d up to n-d where n is the length of `.dims`.  
**[Data variables](https://docs.xarray.dev/en/latest/user-guide/terminology.html#term-Variable)** - Scalar values that occupy the grid cells implied by coordinate arrays. The physical observable(s) that are the focus of the dataset.  
**Attributes** - Metadata that can be assigned to a given `xr.Dataset` or `xr.DataArray` that is ***static*** along that object's dimensions.   
:::

## 'Tidying principles' for Xarray
At the beginning of the book, we also discussed 'tidy data' as its defined for tabular data. Now that we've worked through a number of examples preparing n-d array data for analysis, we can enumerate a few best practices that apply in most cases when tidying data with Xarray. The guiding question when thinking about *how* to tidy data is always:

***What format will simplify subsequent analysis with this data?***

We'll consider what this means for different types of Xarray objects based on the examples encountered in the tutorials.

::::{tab-set}
:::{tab-item} Dimensions
Almost all data cubes have the same core structure of `(x, y, time)` or `(longitude, latitude, time)` dimensions. 

However, the optimal structure for a given dataset depends on its intended use-case, and there is considerable room to reshape data cubes to fit specific analytical needs. In these situations, a guiding question could be: 

*What shape of a given dataset will help answer the question(s) I have about the data?*


#### Relevant examples

##### Expanding dimensions v. adding variables.

- Data variables should be independent of one another.

- Formatting the Sentinel-1 backscatter cube to have `vv` and `vh` data variables versus `band` dimension with the following coordinate array: `('band', ['vh','vv'])`.
    - If you are only interested in a single polarization of the dataset or looking at backscatter from different polarizations independent of one another, treating backscatter from each polarization as a  `data variable` is suitable and maybe even optimal; it can be simpler to perform operations on a single variable rather than an entire dimension. 
    - If you are interested in examining backscatter across different polarizations, the different polarizations are most appropriately represented as elements of a dimension.
*[Sentinel-1 tutorial, notebook 3](../sentinel1/nbs/asf_exploratory_analysis.ipynb)*

##### The dimensions of a dataset depend on what you want to do with it

- Adding `source` dimension when comparing ASF and PC backscatter datasets.
    - In this example, the goal of our analysis changes from observing backscatter to observing how measurements of backscatter from two processing pipelines differ from one another. This implies a different shape of the data that is relevant to this question; the appropriate dimensions change from `(x, y, time, band)` to `(x, y, time, band, source)`. Adding a source dimension let's us index the combined dataset by 'source' and compare the two 'source' elements on a common grid and scale.
*[Sentinel-1 tutorial, notebook 4](../sentinel1/nbs/comparing_s1_rtc_datasets.ipynb)*
:::
:::{tab-item} Coordinate variables
A dataset must have a dimensional coordinate variable for each dimension in `ds.dims`. Additional coordinate variables should be added when relevant metadata varies over dimension(s) of the dataset.

#### Relevant examples
##### Assigning metadata that varies along a given dimension as a non-dimensional coordinate of that dimension.**

- Metadata that varies over `(time)` as well as `(time, space)` dimensions should be represented by coordinate arrays. 
*[Sentinel-1 tutorial, metadata wrangling notebook](../sentinel1/nbs/wrangle_metadata.ipynb)*

##### Non-dimensional coordinate variable are not indexed. To query the dataset using a coordinate, it can be more efficient to express the query in terms of a dimensional coordinate.
- It is faster to subset the dataset using `ds.sel()` than `ds.where()`. 
*[ITS_LIVE tutorial, exploratory analysis of a a single glacier notebook](../itslive/nbs/exploratory_data_analysis_single.ipynb)*
:::
:::{tab-item} Attributes
`Attrs` can be assigned to the dataset as a whole or any of the `xr.DataArray` objects within it. 

#### Relevant examples
##### Attributes must be formatted according to accepted metadata conventions like CF and STAC in order to take advantage of tools built off these specifications.
- Using `cf_xarray` with appropriately-formatted metadata enables more streamlined access to and interpretation of metadata
*[ITS_LIVE tutorial, data access notebook](../itslive/nbs/accessing_itslive_s3_data.ipynb)*

- Having appropriate CF metadata enables reading and writing vector data cubes to disk
*[ITS_LIVE tutorial, exploratory analysis of a group of glaciers notebook](../itslive/nbs/exploratory_data_analysis_group.ipynb)*
:::
:::{tab-item} Collections
Xarray DataTrees provide an API for working with a collection of Xarray objects.
#### Relevant examples
Independent objects should be represented as unique `xr.Datasets` (if multivariate) or `xr.DataArrays` (if univariate). If you are working with independent objects but would like to organize, keep track of, and work with them in relation to one another, use [`xr.DataTree`](https://docs.xarray.dev/en/stable/generated/xarray.DataTree.html) to assign hierarhical relationships among objects. 
*[ITS_LIVE tutorial, exploratory analyiss of a single glacier notebook](../itslive/nbs/exploratory_data_analysis_single.ipynb)*
- Use `xr.DataTree` to separate the dataset by satellite sensor.

When working with spatial features described by vector geometries, you can use [Xvec](https://xvec.readthedocs.io/en/stable/) to organize the data as a vector cube. This cube will have a `'geometry'` dimension that is an array of geometries, letting you work with multiple n-d features.
*[ITS_LIVE tutorial, exploratory analysis of a group of glaciers notebook](../itslive/nbs/exploratory_data_analysis_group.ipynb).*
:::
::::