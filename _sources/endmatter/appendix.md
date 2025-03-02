# Appendix

While developing this book, we encountered different examples that didn't always fit into the overall scope of the tutorials, but still may be useful to others. 

## [1. Troubleshooting geometry types (ITS_LIVE tutorial)](nbs/1_handle_mult_geom_types.ipynb)

In the first tutorial, while making an [interactive visualization of vector dataframes](../itslive_nbs/3_combining_raster_vector_data.ipynb), we encountered a warning. This notebook includes a step-by-step demonstration of troubleshooting this warning, identifying its source and resolving it. 

## [2 Reading a stack of files with `xr.open_mfdataset()` (Sentinel-1 tutorial)](nbs/2_read_w_xropen_mfdataset.ipynb)

Xarray's `xr.open_mfdataset()` [function](https://docs.xarray.dev/en/stable/generated/xarray.open_mfdataset.html) allows the user to read in and combine multiple files at once to produce a single `xr.DataArray` object. This approach was explore when developing the [Read ASF-processed Sentinel-1 RTC data notebook](../tutorial2/nbs/1_read_asf_data.ipynb). However, `xr.open_mfdataset() didn't work well for this purpose because, while the stack of raster files used in this example covers a common area of interest, it includes several different spatial footprints. This creates problems when specifying a chunking strategy. 

`xr.open_mfdataset()` takes a 'preprocess' argument that allows the user to write a function to specify how each raster file should be read so that the structure and metadata of the returned object matches the desired format. However, because it applies the same preprocessing steps to each file, the chunking strategyy is defined off of the first file in the stack. With files that cover different spatial footprints, different chunking strategies will be required. The processing works fine for lazy steps, but a memory 'blow-up' occurs at computation time. 

For this reason, `xr.open_mfdataset()` was not an appropriate tool for this workflow. We kept this example in the book as an appendix item in case it is useful for users who would like to see an example of how to write a `preprocess` argument and how to call `xr.open_mfdataset()`. 

We found that creating and reading GDAL VRT objects worked better from a memory perspective, but it created much more work to organize metadata and prepare an analysis-ready data cube. The `xr.open_mfdataset()` function seems much more efficient approach if your dataset is well-aligned with its parameters (ie. a spatially uniform stack).

In addition to the documentation linked above, some other useful resources for `xr.open_mfdataset()` are: 

1. [Stack overflow discussion](https://stackoverflow.com/questions/51709266/using-xarray-to-open-a-multi-file-dataset-when-both-the-files-and-dataset-have-a) on passing `preprocess` arguments to `xr.open_mfdataset()`  
    *tl;dr*: Write a preprocess function to handle any formatting that should happen to **individual files** *before* they are concatenated within `xr.open_mfdataset()`. The preprocess function should ingest and produce a single `xr.DataArray` or `xr.Dataset` object.   
2. [Github discussion](https://github.com/pydata/xarray/issues/2550) on how to access filename information of a Xarray object within the preprocess function.   
    *tl;dr*: To access an object's filename within preprocess, call `ds['var'].encoding['source']`. However, use this with caution and be sure to test it. 
:::{note}
TODO that i'm interpreting the solution on this thread correctly?
:::

```{note}
If you wanted to select scenes from a single viewing geometry at the expense of a denser time series, `xr.open_mfdataset()` might work a bit better (this approach has not been tested).
```