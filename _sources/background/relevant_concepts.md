# Relevant concepts

## *Larger than memory data, parallelization and Dask*
```{glossary}
Larger than memory data
    Notebooks in this tutorial spend a considerable amount of time focusing on 'larger-than-memory' datasets and strategies for working with them 'in memory'. What does this mean? When we say memory, we're referring to the available CPU space, or RAM (wc: internal memory?) on whatever machine you're working on. When we're working with smaller datasets, the data and intermediate copies that are created during many operations don't exceed the internal memory available on our machine. However, as datasets increase in size, the memory required for many workflows can quickly scale and exceed the availability of most personal machines. This is what we mean when we refer to 'larger than memory' data. In the case of this tutorial, the dataset we'll be using is very large (several hundred gigabytes when uncompressed). With datasets this large, we need to employ different approaches that can be a bit more complicated than a straightforward operation that ingests and produces smaller amounts of data. 

Dask
    There are different ways to approach a dataset that is too large to load into memory. In this tutorial, we rely on the Python library, [Dask](https://www.dask.org/). Dask allows you to parallelize your workflows, breaking up a large job into many smaller jobs that can be executed in parallel rather than in sequence with one another. Parallelized jobs can be distributed across cores on an individual compputer, or across large, distributed compute nodes in cloud-computing environments. In this tutorial, we'll use Dask to parallelize and distribute jobs across one machine. Conveniently, Dask also has built-in integrations with many open-souce Python libraries, including Xarray; this means that we can specify and create Dask-backed Xarray objects within Xarray commands such as `xr.open_dataset()`, rather than needing to create them separately. 

    An important aspect of Dask is that it's operations are by default 'lazy'. This means that if I have an array (`arr`) and I want to perform an operation on it (let's imagine something very simple, like multiplying the array by 5), when I execute that operation in Python (`arr * 5`), as long as it is a Dask Array (or an Xarray object backed by Dask Arrays), the computation is not actually executed *yet*. Dask uses *task scheduling* to track, orchestrate, and synchronize operations. When I call `arr * 5`, rather than calculating the resulting product, Dask adds it to a **Task Graph** (add link?). A Task Graph consist of python functions and the inputs and outputs of those functions; they are used by the program to direct how jobs should be distributed and executed across available resources in order to correctly complete the desired operation. 

    So what can happen lazily and what can't? Dask will wait to evaluate a set of operations until it is explicitly instructed to do so. This can be through calling a direct method (like [`.compute()`](https://docs.dask.org/en/stable/generated/dask.dataframe.DataFrame.compute.html) or [`.persist()`](https://docs.dask.org/en/latest/generated/dask.dataframe.DataFrame.persist.html)), or an operation that cannot be accomplished lazily (like plotting an array). For more detail, check out [Dask's Managing Computation documentation](https://distributed.dask.org/en/stable/manage-computation.html).

Chunking
    Dask operates by breaking up large tasks into smaller ones. In our context, the main way this is accomplished is through [Dask Arrays](https://docs.dask.org/en/latest/array.html). If you're familiar with the Xarray data model, you'll know that the fundamental building block of a standard Xarray DataArray is a NumPy array: an `Xr.DataArray` is just a NumPy array with named dimensions and coordinates, and separate NumPy arrays describing those coordinates. 

    When we introduce Dask to an Xarray workflow, we convert the underlying `.data` objects of an Xarray object from NumPy arrays to Dask Arrays. Luckily, Dask arrays aren't too unfamiliar; a Dask Array is composed of NumPy-like arrays but with an additional specification: `chunks`. Chunks tell Dask how to break up the array into smaller parts. For example, if you have a 3-dimensional Xarray DataArray, you will specify how the object should be chunked along each dimension. 

    Choosing chunks can be complicated and have a significant impact on how fast your code runs. Typically, you want enough chunks that each individual chunk is relatively small and many chunks can fit into into memory. However, if you have too many chunks, Dask now needs to keep track of many individual tasks, meaning that more time will be spent managing the task graph compared to executing tasks. In addition, tasks should reflect the shape of yoour data and how you want to use it. If you're working with a space-time dataset but you're most interested in spatial analysis, having smaller chunks along the `x` and `y` dimensions will make spatial operations easier to parallelize. 

    Dask and Xarray have a number of resources focused on this topic. We recommend:
    - [Dask Array - Best Practices](https://docs.dask.org/en/latest/array-best-practices.html),   
    - [Dask Array Chunks](https://docs.dask.org/en/stable/array-chunks.html),  
    - [Choosing good chunk sizes](https://blog.dask.org/2021/11/02/choosing-dask-chunk-sizes) blog post,  
    - [Xarray - Parallel Computing with Dask](https://docs.xarray.dev/en/stable/user-guide/dask.html)
        - Specifically the [Chunking and Performance](https://docs.xarray.dev/en/stable/user-guide/dask.html#chunking-and-performance) section.
```
## *Importance of metadata naming and metadata naming conventions*
```{glossary}
Metadata naming

    Metadata is vital to understanding your dataset, however, because of the range of types of metadata and ways it is often stored, it can become very complicated to work with and keep track of. There are a few priorities to keep in mind when working with metadata and/or writing your own.

    1) Metadata should be added to the `attrs` of an Xarray object so that the dataset is **self-describing** (You or a future user don't need external information to be able to interpret the data).
    2) Wherever possible, metadata should follow Climate Forecast (CF) naming conventions.

Climate Forecase (CF) Metadata Conventions

    CF conventions address many of the challenges of inconsistent and non-descriptive metadata found in climate and earth observation datasets. By establishing common naming schemes for physical quantities and other attributes, these conventions facilitate collaboration, data fusion, and the development of tools for working with a range of data types. 

    From the [CF documentation](https://cfconventions.org/): 

    >The CF metadata conventions are designed to promote the processing and sharing of files created with the NetCDF API. The conventions define metadata that provide a definitive description of what the data in each variable represents, and the spatial and temporal properties of the data. This enables users of data from different sources to decide which quantities are comparable, and facilitates building applications with powerful extraction, regridding, and display capabilities. The CF convention includes a standard name table, which defines strings that identify physical quantities.

    CF metadata conventions set common expectations for metadata names and locations across datasets.  In this tutorial, we will use tools such as [cf_xarray]() that leverage CF conventions to add programmatic handling of CF metadata to Xarray objects, meaning that users can spend less time wrangling metadata. 🤩
```