import os
import pathlib
import papermill as pm

itslive_dir = pathlib.Path(os.getcwd(), "book/itslive/nbs")

itslive_nb_names = [
    "1_accessing_itslive_s3_data.ipynb",
    "2_larger_than_memory_data.ipynb",
    "3_combining_raster_vector_data.ipynb",
    "4_exploratory_data_analysis_single.ipynb",
    "5_exploratory_data_analysis_group.ipynb",
]
itslive_nbs = [os.path.join(itslive_dir, nb) for nb in itslive_nb_names]

# Note, this doens't work rn, doesn't allow errors. maybe would need to switch to nbconvert for htis (?)
for notebook in itslive_nbs:
    print(f"Running {notebook}...")
    pm.execute_notebook(notebook, notebook, allow_errors=True)
