# Context and motivation 
(*in progress*)  
## *Increasingly large, cloud-optimized data means new tools and approaches for data management*
In recent years, the volume of available earth observation data has ballooned, transforming both the types of scientific questions that can be asked and the fundamental ways in which analysts approach investigating these questions. These developments mean that analysts must gain new skills across a range of domains in order to work with these types of scientific data. 

In recognition of the challenges that these opportunities can pose, we developed tutorials that demonstrate scientific workflows using publicly accessible, cloud-native geospatial datasets and open-source scientific software tools. 

These tutorials focuses on the complexities inherent to working with n-dimensional, gridded ({term}`raster`) datasets and use the core stack of software packages built on and around the [Xarray](https://xarray.dev/) data model to demonstrate these steps.

## *Asking questions of complex datasets*

Scientific workflows involve asking complex questions of diverse types of data. Earth observation and related datasets often contain two types of information: measurements of a physical observable (eg. temperature) and metadata that provides auxiliary information that required in order to interpret the physical observable (time and location of measurement, information about the sensor, etc.). With increasingly complex and large volumes of earth observation data that is currently available, storing, managing and organizing these types of data can very quickly become a complex and challenging task, especially for students and early-career analysts (For more on these concepts, see [anatomy of a datacube](anatomy_of_a_data_cube.md)). 

This book provides detailed examples of scientific workflow steps that ingest complex, multi-dimensional datastets, introduce users to the landscape of popular, actively-maintained opens-source software packages for working with geospatial data in Python, and include strategies for working with larger-than memory data stored in publicly available cloud-hosted repositories. Importantly, these demonstrations are accompanied by detailed discussion of concepts involved in analyzing earth observation data such as dataset inspection, manipulation, and exploratory analysis and visualization. Overall, we emphasize the importance of understanding the structure of multi-dimensional earth observation datasets within the context of a given data model and demonstrate how such an understanding can enable more efficient and intuitive scientific workflows. 
