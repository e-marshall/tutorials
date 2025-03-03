# Anatomy of a data cube 

(*in progress*)

The key object of our analyses will be a [raster data cube](https://openeo.org/documentation/1.0/datacubes.html), an n-dimensional object storing continuous measurements about some sort of physical quantity of different dimension(s). Many scientific workflows involve examining how a variable (such as temperature, windspeed, relative humidity, etc.) varies over time and/or space. Data cubes are a way of organizing geospatial data that let's us ask those types of questions. 

A very common data cube structure is a 3-dimensional object with (`x`,`y`,`time`) dimensions. This may sound quite simple, and it can be, but in practice, the amount and types of information contained within a single dataset can become complicated and unwieldy. As analysts, we accesss data (usually from providers such as Distributed Active Archive Centers ([DAACs](https://nssdc.gsfc.nasa.gov/earth/daacs.html))), and then we are responsible for organizing the data in a way that let's us ask the questions we'd like to of it. While some of these decisions can be very intuitive (eg. it makes sense to stack observations from different points in time along a time dimension), some can be less straightforward (Where and how should important metadata be stored so that it will propagate across appropriate operations and be accessible when it is needed?). 

## *Two types of information*
Fundamentally, many of these complexities can be reduced to one distinction: is a particular piece of information a physical information (the main focus, or target, of the dataset), or is it metadata that provides information that is necessary to properly interpret and handle the physical observable? Answering this question will help you understand how to situate a piece of information wtihin the broader data object. 

((insert example and diagram))
- think more about what this should look like. it could be: txt on left w/ diagram on right
...'imagine a timeseries (of NDVI, land surface temperature). it contains the following information:
- for every acquisition:
    - Acquisition date
    - X-coordinate values
    - Y-coordinate values
    - measurement for every pixel
    - a lot of important metadata
    (diagram of diff kinds of data)
- all of the information other than the measurement value is very important for understanding the measurement (imaginge if we didn't have x,y coordinate data, or geotransform metadata, ie. we couldn't locate our measurements in space...). 

^^ think about if this section should have an abstract example like above, or if it should just introduce the concept and then have a concrete illustration of data cube for each tutorial?

- alot of this is pointing at tidy data principles (eg. how should data be structured to facilitate analysis), reference that (for tabular or array data)? 

## *Open-source setting*

Luckily, there are great open-source tools out there that handle much of the complexity described above. These tools streamline the parsing and handling of metadata and many have built-in integrations with one another so that to the user, they often 'just work.' But, it takes some familiarity with these tools (and knowing they exist!) in order to take advantage of them and use them appropriately in your workflows. 

These tutorials illustrate real-world datasets and some of challenges that can be involved with working in them. Throughout the notebooks, we highlight open-source tools that facilitate and accelerate steps at all stages of a workflow, from reading data into memory; subsetting, manipulating and processing different arrays, handling complicated geographic metadata, viisualizing results and writing data to disk.


## *Recommended resources*
Link to other data cube resources...