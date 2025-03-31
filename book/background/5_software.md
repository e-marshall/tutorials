# 2.5 Software and computing environment

On this page you'll find information about the computing environment that will be used in both of the tutorials in this book. We provide instructions for Running locally (on laptop), or on a hosted JupyterHub in AWS us-west-2.

## *Running tutorial materials locally*

There are two options for creating a software environment: [pixi](https://pixi.sh/latest/) or [mamba](https://mamba.readthedocs.io/en/latest/) / [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html). We recommend using pixi to create a consistent environment on different operating systems. If you have pixi installed, follow the steps below, otherwise, follow the steps for conda/mamba below.

### To use pixi
1. Clone the book's GitHub repository:   
    ```git clone https://github.com/e-marshall/cloud-open-source-geospatial-datacube-workflows.git```

2. Navigate into the repo environment:
```cd cloud-open-source-geospatial-datacube-workflows```

3. There is a small data cube included in the repo that is used in the tutorials. We don't want git to track this so we tell it to ignore this file path.
```git update-index --assume-unchanged book/itslive/data/raster_data/regional_glacier_velocity_vector_cube.zarr/.```

4. Execute `pixi run` for each tutorial:
```pixi run itslive```
```pixi run sentinel1```

Note that the first `pixi run` will download specific versions of all required Python libraries to a hidden directory `./.pixi`. Subsequent runs activate that environment and execute code within it. You can also run `pixi shell` to "activate" the environment (set paths to executables and auxiliary files) and `exit` to deactivate it. 

### To use conda/mamba

1. Clone this book's GitHub repository:  
```git clone https://github.com/e-marshall/cloud-open-source-geospatial-datacube-workflows.git```

2. Navigate into the `book` sub-directory:  
```cd cloud-open-source-geospatial-datacube-workflows/book```

3. Create and activate a conda environment from the `environment.yml` file located in the repo:  
```conda env create -f environment.yml```

4. There is a small data cube included in the repo that is used in the tutorials. We don't want git to track this so we tell it to ignore this file path.
```git update-index --assume-unchanged book/itslive/data/raster_data/regional_glacier_velocity_vector_cube.zarr/.```

5. Start Jupyterlab and navigate to the directories containing the Jupyter notebooks (`itslive/nbs` and `s1/nbs`):  
```jupyterlab```

Both tutorials use functions that are stored in scripts associated with each dataset. You can find these scripts here: [`itslive_tools.py`](../itslive/nbs/itslive_tools.py) and [`s1_tools.py`](../sentinel1/nbs/s1_tools.py).


## *Running tutorial materials on a hosted JupyterHub*

Many NASA datasets including ITS_LIVE are hosted in the AWS us-west-2 data center. While these tutorial notebooks are designed to be run on any computer, if you intend to modify the notebooks and access data directly it is desirable to run computations in the same data center. A convenient way access a computer in AWS us-west-2 is to use a hosted JupyterHub platform such as one of the following:

- https://docs.openveda.cloud/user-guide/scientific-computing/
- https://opensarlab-docs.asf.alaska.edu
- https://book.cryointhecloud.com/content/Getting_Started.html

On these systems you can install software environment in the same way described above, but you must make the default JupyterLab interface aware of your environment. In Jupyter terminology you must specify a 'kernel'. Unfortunately there is not an automatic and uniform way of doing this, but a few manual steps can be followed:

1. Create a kernel specification subfolder under your home directory:
```
mkdir -p /home/jovyan/.local/share/jupyter/kernels/pixi/
```

2. Use a text editor to add the following JSON to a `kernel.json` file in the directory we created above (`/home/jovyan/.local/share/jupyter/kernels/pixi/kernel.json`):
```
{
 "argv": [
  "/home/jovyan/.pixi/bin/pixi",
  "run",
  "python",
  "-m",
  "ipykernel_launcher",
  "-f",
  "{connection_file}"
 ],
 "display_name": "Pixi (default)",
 "language": "python",
 "metadata": {
  "debugger": true
 }
}
```

Once created you should see this kernel listed in the output of `jupyter kernelspec list`:
```
Available kernels:
  python3    /srv/conda/envs/notebook/share/jupyter/kernels/python3
  pixi       /home/jovyan/.local/share/jupyter/kernels/pixi
```

Finally, you may need to reload your web browser in order to see 'Pixi (default)' as an optional kernel to select when you open one of the Jupyter Notebooks in this repository. With 'Pixi (default)' as the selected kernel code in the notebook will use the environment defined in your `.pixi` folder!




