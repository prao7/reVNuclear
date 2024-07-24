#### Author: Pradyumna Rao, <pradyumna.rao@colorado.edu>
# Reviewer: Guillaume L'Her <glher@mines.edu>
import numpy as np
import rasterio

# Define a function to import pixel data from a tif file and store it as a numpy array
def tif_to_numpy(tif_filepath):
    with rasterio.open(tif_filepath) as src:
        # Read the data from the tif file
        data = src.read()
        # If the tif file has multiple bands, combine them into a single numpy array
        if data.ndim > 2:
            data = np.dstack(data)
    return data

# Path to the uploaded tif file
tif_filepath = 'input_data/land_exclusion_data/tx_data/texas.tif'

# Call the function and get the numpy array
pixel_data = tif_to_numpy(tif_filepath)
print(pixel_data.shape)
