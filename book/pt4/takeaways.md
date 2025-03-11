# Takeaways

In this book, we saw a range of real-world datasets and the steps required to prepare them for analysis. Several guiding principles for assembling and using analysis-ready data cubes in Xarray can be drawn from these examples.

We'll first return to the initial definitions of the Xarray components of data cubes before enumerating guidelines and best practices that arise from the examples in the book.

:::{admonition} Xarray components of data cubes
**Dimensions** - The shape of the semantic meaning of the dataset. Frequently, `(x, y, time)`.   
**Dimensional coordinate variables** - Arrays describing the range and resolution of the data along each dimension.  
**Non-dimensional coordinate variables** - Metadata about the physical observable that varies along one or more dimensions.  
**Data variables** - Scalar values that occupy the grid cells implied by coordinate arrays. The physical observable(s) that are the focus of the dataset.  
**Attributes** - Metadata that can be assigned to a given `xr.Dataset` or `xr.DataArray` that is ***static*** along that object's dimensions.   
:::

## Tidying Principles 
(need to first introduce tidy data if going to call it that)

Guiding question:
```
How could subsequent analysis of this data be made easier / simplified?
```

## Dimensions
Almost all data cubes will have the same generic structure of `(x, y, time)` or `(longitude, latitude, time)` dimensions. 

However, the optimal structure for a given dataset depends on its intended use-case, and there is considerable room to reshape data cubes to fit specific analytical needs. In these situations, a guiding question should be: 

```
What shape of a given dataset will help answer the question(s) I have about the data?
```

Relevant examples:
- `vv` and `vh` data variables versus `band` dimension of Sentinel-1 RTC backscatter cube:
    - If you are only interested in a single polarization, each polarization as a `data variable` is suitable/optimal (easier to perform operations on a single variable)
    - If you are interested in looking at single-pol backscatter relative to cross-pol backscatter, or vice versa / interested in backscatter across different polarizations, the different polarizations are most appropriately represented as elements of a dimension.
- Adding `source` dimension when comparing ASF and PC backscatter datasets.
    - In this example, the objective of our analysis changes from observing backscatter to observing how measurements of backscatter from two processing pipelines differ from one another. This implies a different shape of the data that is relevant to this question from `(x, y, time, band)` to `(x, y, time, band, source)`. Adding source dim let's us index combined dataset by 'source' and compare the two 'source' elements on a common grid and scale.

## Coordinate variables
- Minimum coordinate variables are those for the dimension of a dataset.
- Additional coordinate variables should be added when relevant metadata varies over dimension(s) of the dataset

Relevant examples:
- Metadata that varies over `(time)` as well as `(time, space)` dimensions in Sentinel-1 tutorial (metadata wrangling notebook).

## Attributes
- Should be assigned to `xr.Dataset` and `xr.DataArray` objects that can represent the entire data cube, coordinates or data variables of the data cube. 