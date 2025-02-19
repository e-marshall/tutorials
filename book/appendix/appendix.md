# Appendix

While developing this book, we encountered different examples that didn't always fit into the overall scope of the tutorials, but still may be useful to others. 

## 1.1. Troubleshooting geometry types (ITS_LIVE tutorial)

- [Appendix 1.1 notebook](appendix_1_1_handle_mult_geom_types.ipynb)


In the first tutorial, while making an [interactive visualization of vector dataframes](../itslive_nbs/3_combining_raster_vector_data.ipynb), we encountered a warning. The notebook below includes a step-by-step demonstration of troubleshooting this warning, identifying its source and resolving it. 


## 1.2 Reading a stack of files with `xr.open_mfdataset()` (Sentinel-1 tutorial)
- [Appendix 1.2 noteobok](appendix_1_2_read_w_xropen_mfdataset.ipynb)

Xarray's `xr.open_mfdataset()` [function](https://docs.xarray.dev/en/stable/generated/xarray.open_mfdataset.html) allows the user to read in and combine multiple files at once to produce a single `xr.DataArray` object. I first used this to read in the geotiff files for each ASF-processed scene of Sentinel-1 RTC imagery. The `xr.open_mfdataset()` function takes a preprocess argument which allows you to write a function that specifies how each raster file is read in so that the structure and metadata of the returned object is correct. This gives you a lot of flexibility and makes reading in a large stack of files very smooth.

However, for this dataset, I found that the `xr.open_mfdataset()` function wasn't a great fit. The raster stack all covered a common area of interest, but each file did not have the exact same spatial footprint. This created problems when specifying a chunking strategy, because the chunking was defined off of the first file in the stack, but would not be appropriate for files further down in the stack with different borders. The processing would work fine for all lazy steps, but a memory 'blow-up' would occur when I tried to perform a step that required computation. I initially thought I had bypassed this issue by clipping the returned dataset to the spatial extent of my area of interest (much smaller), but soon realized that this process encountered memory issues as well. 

```{note}
The stack I used contains multiple scenes that cover the same area of interest (multiple viewing geometries). If you wanted to select only scenes from a single viewing geometry at the expense of a denser time series, `xr.open_mfdataset()` might work a bit better (I didn't try this, so I cannot say for sure)
```

Ultimately, I decided to use the approach of creating GDAL VRT objects, and reading those in with `rioxarray.open_rasterio()` to organize the data as xarray objects. This worked much better from a memory perspective but created much more work with organizing metadata and structuring the dataset in an analysis-ready format. The `xr.open_mfdataset()` function seems like a much more efficient approach if your dataset is well-aligned with its parameters (ie. a spatially uniform stack). While it did not end up being the best tool for this task, I decided to include the notebook with the `xr.open_mfdataset()` approach anyway, in case it is useful to see a demonstration of this function. I learned a lot about how to structure a `preprocess` function and many other steps working on this example. 

In addition to the documentation linked above, some other useful resources for `xr.open_mfdataset()` are: 

1. [Stack overflow discussion](https://stackoverflow.com/questions/51709266/using-xarray-to-open-a-multi-file-dataset-when-both-the-files-and-dataset-have-a) on passing `preprocess` arguments to `xr.open_mfdataset()`  
    *tl;dr*: Write a preprocess function to handle any formatting that should happen to **individual files** *before* they are concatenated within `xr.open_mfdataset()`. The preprocess function should ingest and produce a single `xr.DataArray` or `xr.Dataset` object.   
2. [Github discussion](https://github.com/pydata/xarray/issues/2550) on how to access filename information of a Xarray object within the preprocess function.   
    *tl;dr*: To access an object's filename within preprocess, call `ds['var'].encoding['source']`. However, use this with caution and be sure to test it. 
:::{note}
Check that i'm interpreting the solution on this thread correctly?
:::