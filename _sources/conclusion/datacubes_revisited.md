# 5.3 Data Cubes Revisited

In this book, we saw a range of real-world datasets and the steps required to prepare them for analysis. Several guiding principles for assembling and using analysis-ready data cubes in Xarray can be drawn from these examples.

Let's first return to the Xarray building blocks described in the background [section](../background/2_data_cubes.md); we can now provide more-detailed definitions of what they are and how they should be used:

:::{admonition} Dissecting data cubes
**[Dimensions](https://docs.xarray.dev/en/latest/user-guide/terminology.html#term-Dimension)** - What do the axes of the data represent? This should be the set of dimensions. Frequently, `(x, y, time)`. Dimensions are orthogonal to each other.  
**[Dimensional coordinate variables](https://docs.xarray.dev/en/latest/user-guide/terminology.html#term-Dimension-coordinate)** - Typically 1-d arrays describing the range and resolution of the data along each dimension. Think of this as axes tick labels on a plot.
**[Non-dimensional coordinate variables](https://docs.xarray.dev/en/latest/user-guide/terminology.html#term-Non-dimension-coordinate)** - Metadata about the physical observable that varies along one or more dimensions. These can be 1-d up to n-d where n is the length of `.dims`.  
**[Data variables](https://docs.xarray.dev/en/latest/user-guide/terminology.html#term-Variable)** - Physical observable(s) whose values are known at every point on the grid formed by the dimensions. 
**Attributes** - Metadata that can be assigned to a given `xr.Dataset` or `xr.DataArray` that is ***invariant*** along that object's dimensions.   
:::

{{break}}

## Tidying guidelines for Xarray
At the beginning of the book, we also discussed 'tidy data' as its defined for tabular data. Now that we've worked through a number of examples preparing n-dimensional array data for analysis, we can enumerate a few best practices that apply in most cases when tidying data with Xarray. The guiding question when thinking about *how* to tidy data is always:

**How can this data be structured to simplify subsequent analysis?**

Keep in mind that one organization of the data need not make all analyses equally ergonomic. We must be open to transforming the data between equivalent representations, depending on the task at hand.

Here are a few guidelines:
::::{tab-set} 
:::{tab-item} Variables
### Data variables
These are the measurements or estimates of your dataset. If there are multiple independent measurements in the dataset, they should be stored as data variables in a `xr.Dataset`, if the data are univariate, use a [`xr.DataArray`](https://docs.xarray.dev/en/stable/generated/xarray.DataArray.html)
|   |  | 
| :-----------:|:---------- |
| **Guiding Question** | What physical observable(s) is my dataset measuring?|

#### Relevant examples
In [Sentinel-1, notebook 3 - Exploratory analysis of ASF data](../sentinel1/nbs/3_asf_exploratory_analysis.ipynb), we saw examples of treating multiple backscatter polarizations as data variables versus a single variable along a `band` dimension. We can convert between the two representations using `Dataset.to_array` and `DataArray.to_dataset`.

|   |  | 
| :-----------:|:---------- |
| **Takeaway** | Data variables should be independent of one another.|


:::

:::{tab-item} Dimensions

### Dimensions
Many earth observation data cubes have the same core structure of `(x,y,time)` or `(longitude, latitude, time)` dimensions. However, the optimal structure for a given dataset depends on its intended use-case, and there is considerable room to reshape data cubes to fit specific analytical needs.   
In these situations, a guiding question could be:   
|   |  | 
| :-----------:|:---------- |
| **Guiding Question** | What 'shape' will help me answer the questions I have about this dataset?|

#### Relevant examples

##### 1. Expanding dimensions v. adding variables 
- Formatting the Sentinel-1 backscatter cube to have `vv` and `vh` data variables versus `band` dimension with the following coordinate array: `('band', ['vh','vv'])` ([*Sentinel-1 tutorial, notebook 3 - exploratory analysis of ASF data*](../sentinel1/nbs/3_asf_exploratory_analysis.ipynb)).
    - If you are only interested in a single polarization of the dataset or looking at backscatter from different polarizations independent of one another, treating backscatter from each polarization as a  __data variable_ is suitable and maybe even optimal; it can be simpler to perform operations on a single variable rather than an entire dimension.   
    - If you are interested in examining backscatter across different polarizations, the different polarizations are most appropriately represented as elements of a dimension. 

|   |  | 
| :-----------:|:---------- |
| **Takeaway** | Structure your datacube's dimensions so that data variables are independent of one another. |  

```{tip}
If you are working with a dataset where information about how the variables relate to one another is included in the variable name (e.g. a year, or a band wavelength), this is a sign that there should be an additional dimension.
```

##### 2. Compare two datasets by combining them into a single cube with an additional dimension
- To compare data from different satellites within the ITS_LIVE dataset, we create a new data cube with a `'sensor'` dimension ([*ITS_LIVE tutorial, notebook 4 - exploratory analysis of a single glacier*](../itslive/nbs/4_exploratory_data_analysis_single.ipynb)*).
- Adding `source` dimension when comparing ASF and PC backscatter datasets ([*Sentinel-1 tutorial, notebook 5 - comparing backscatter datasets*](../sentinel1/nbs/5_comparing_s1_rtc_datasets.ipynb)).  
    - In this example, the goal of our analysis changes from observing backscatter to observing how measurements of backscatter from two processing pipelines differ from one another. This implies a different shape of the data that is relevant to this question; the appropriate dimensions change from `(x, y, time, band)` to `(x, y, time, band, source)`. 
    - Adding a source dimension let's us index the combined dataset by 'source' and compare the two 'source' elements on a common grid and scale.   

|   |  | 
| :-----------:|:---------- |
| **Takeaway** | Consider either concatenating two cubes along a new dimension, or splitting a dimension in to multiple cubes. One approach may be more ergonomic compared to the other depending on the problem at hand. |

:::
:::{tab-item} Coordinates

## Dimensional & non-dimensional coordinate variables
A dataset must have a **dimensional coordinate** variable for each dimension in `ds.dims`. Additional **non-dimensional coordinate variables** should be added when relevant metadata varies over dimension(s) of the dataset.  
|   |  | 
| :-----------:|:---------- |
| **Guiding Question** | What are the dimensions of the dataset? What information (separate from the measurement variable) varies over those dimensions? |

#### Relevant examples
##### 1. Handling time-varying metadata
- Metadata that varies over `(time)` should be stored as coordinate variables along the `time` dimension (e.g. whether a scene was taken during an ascending or descending pass).
- Metadata that varies over `time`, `x`, and `y` should be coordinate variables that exist along those dimensions.
    - *[Sentinel-1 tutorial, metadata wrangling notebook](../sentinel1/nbs/2_wrangle_metadata.ipynb)*

|   |  | 
| :-----------:|:---------- |
| **Takeaway** | Assign metadata that varies along a given dimension as a non-dimensional coordinate of that dimension.
|

:::
:::{tab-item} Attributes
### Attributes
`attrs` can be assigned to the dataset as a whole or any of the `xr.DataArray` objects within it. Many fields have their own conventions for attribute metadata, e.g. Climate & Forecast Conventions (CF).

|   |  | 
| :-----------:|:---------- |
| **Guiding Question** | Does a piece of attribute information apply to this *entire* object (e.g. a data variable, a coordinate variable, or a dataset)? If so, it should be stored as an attribute of that object. Attributes must conform to an existing standard if possible.|

and 

|   |  | 
| :-----------:|:---------- |
| **Guiding Question** | What tools exist that can help perform the operations that I need to with this dataset? How must attribute data be stored to use them? |
#### Relevant examples
##### 1. Attributes must conform to accepted metadata conventions like CF and STAC in order to take advantage of tools built off these specifications 

- Using `cf_xarray` with appropriately-formatted metadata enables more streamlined access to and interpretation of metadata (*[ITS_LIVE tutorial, data access notebook](../itslive/nbs/1_accessing_itslive_s3_data.ipynb)*)
- Having appropriate CF metadata enables reading and writing vector data cubes to disk
(*[ITS_LIVE tutorial, exploratory analysis of a group of glaciers notebook](../itslive/nbs/5_exploratory_data_analysis_group.ipynb)*)

|   |  | 
| :-----------:|:---------- |
| **Takeaway** | Wherever possible, use metadata that conforms to existing conventions.
|

:::
:::{tab-item} Collections
### Collections
Independent objects should be represented as unique `xr.Datasets` (if multivariate) or `xr.DataArrays` (if univariate). If you are working with a collection of independent objects but would like to organize, keep track of, and work with them in relation to one another, use [`xr.DataTree`](https://docs.xarray.dev/en/stable/generated/xarray.DataTree.html) to assign hierarchical relationships among objects. 

#### Relevant examples
##### 1. Apply a function to every object in a collection with `xr.DataTree.map_over_datasets()`
- Using `xr.DataTree` to apply a function to each dataset within a a collection in order to make a new datacube that includes all objects along an expanded dimension (*[ITS_LIVE tutorial, notebook 4 - exploratory analysis of a single glacier notebook](../itslive/nbs/4_exploratory_data_analysis_single.ipynb)).*

##### 2. If you're working with a collection of objects that can be defined by vector geometries, a vector data cube may be an appropriate way to represent the data 
- Use [Xvec](https://xvec.readthedocs.io/en/stable/) to build a vector data cube that has a `'geometry'` dimension; each element of the geometry dimension is a cube that varies over the other dimensions of the cube (frequently `time`) (*[ITS_LIVE tutorial, exploratory analysis of a group of glaciers notebook](../itslive/nbs/5_exploratory_data_analysis_group.ipynb).*)
:::
::::
