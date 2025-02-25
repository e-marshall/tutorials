# Software and computing environment

On this page you'll find information about the computing environment and datasets that will be used in both of the tutorials in this book.

## Running tutorial materials locally

There are two options for creating a software environment, we recommend using [pixi](https://pixi.sh/latest/) to create a consistent environment on different operating systems. If you have pixi installed, simply run the following commands to open either the itslive or sentinel-1 Jupyter notebooks:

```
cd cloud-open-source-geospatial-datacube-workflows
pixi run itslive
pixi run sentinel1
```

**To use conda/mamba follow these steps:**

1. Clone this book's GitHub repository:
```git clone https://github.com/e-marshall/cloud-open-source-geospatial-datacube-workflows.git```

2. Navigate into the `book` sub-directory:
```cd cloud-open-source-geospatial-datacube-workflows/book```

3. Create and activate a conda environment from the `environment.yml` file located in the repo:
```conda env create -f .binder/environment.yaml```

4. Start Jupyterlab and navigate to the directories containing the jupyter notebooks (`itslive_nbs` and `s1_nbs`):
```jupyterlab```

## todo
- shorten name of repo and env/env file probably
- This file has versions pinned but not builds, may need to make more generic? Also maybe should provide lock files.
- update required packages below, some not necessary.


## Required software packages

Below is a list of all packages imported throughout the notebooks:

```python
import adlfs #check this may not be needed
import cf_xarray
import contextily as cx
import geopandas as gpd
import hvplot.pandas
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import pathlib
import planetary_computer
import pystac
import pystac_client
from pystac_client import Client
import requests
import rioxarray as rio
import s3fs
import scipy.stats
import stackstac
from shapely.geometry import Point, Polygon
from typing import Union
import warnings
import xarray as xr




from datetime import datetime #only used in appendix, maybe have those separate
import rich.table #only used once, necessary to make users import?
import time #dont think this is necessary but double check
import glob #don't think this is necessary but double check

from IPython.display import Image
```

Both tutorials also uses functions that are stored in scripts associated with each dataset. You can find these scripts here: [`itslivetools.py`](../itslive_nbs/itslivetools.py) and [`s1_tools.py`](../s1_nbs/s1_tools.py).

