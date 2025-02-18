# Software and computing environment

On this page you'll find information about the computing environment and datasets that will be used in both of the tutorials in this book.

## Running tutorial materials locally

To run the notebooks contained in this tutorial on your local machine, follow these steps:

1. Clone this book's GitHub repository:  
```git clone https://github.com/e-marshall/geospatial_datacube_analysis.git```

2. Navigate into the `book` sub-directory:  
```cd geospatial_datacube_analysis/book```

3. Create and activate a conda environment from the `environment.yml` file located in the repo:  
```conda env create -f environment.yml```
```conda activate geosptial_datacube_analysis_env```

4. Start Jupyterlab and navigate to the directories containing the jupyter notebooks (`itslive_nbs` and `s1_nbs`):  
```jupyterlab```



create the `itslivetools_env` conda environment (`conda env create -f environment-unpinned.yml`) based on the `environment.yml` file [here](https://github.com/e-marshall/mynewbook/blob/master/environment.yml). This should work on any platform (linux, osx, windows) and will install the latest versions of all dependencies.

Alternatively, the code repository for this tutorial (https://github.com/e-marshall/itslive) also contains "lock" files for Linux (conda-linux-64.lock.yml) and MacOS (conda-osx-64.lock.yml) that pin exact versions of all required python packages for a [reproducible computing environment](https://mybinder.readthedocs.io/en/latest/tutorials/reproducibility.html).

## Required software packages

The `environment.yml` file referenced above will install all of the required packages in a conda virtual environment. Below is a list of all packages imported throughout the notebooks:

```python
import cf_xarray
import contextily as cx
import geopandas as gpd
import hvplot.pandas
import matplotlib.pyplot as plt
import numpy as np
import rioxarray as rio
import s3fs
import scipy.stats
from shapely.geometry import Point, Polygon
from typing import Union
import warnings
import xarray as xr

import os
import tempfile
import requests
import markdown
import pathlib


import xarray as xr
import rioxarray as rio
import geopandas as gpd
from shapely.geometry import Polygon

import planetary_computer
import adlfs
import pystac_client
from pystac_client import Client
import stackstac
import pystac


import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np
import pandas as pd
import rich.table
import time
import glob

from IPython.display import Image
```

Both tutorials also uses functions that are stored in scripts associated with each dataset. You can find these scripts here: [`itslivetools.py`](../itslive_nbs/itslivetools.py) and [`s1_tools.py`](../s1_nbs/s1_tools.py).

