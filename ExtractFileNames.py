import os # Import the os module to read the directory
import sys # Import the sys module to read the first python script parameter
import time # Import the time module to check the cache file time
# import PixyzMaterialLibrary

import tkinter as tk # Import the tkinter module to show the directory selection dialog
from tkinter import filedialog # Import the filedialog module to show the directory selection dialog

root = tk.Tk() # Create the root window
root.withdraw() # Hide the root window

cache_file = "materials.cache" # File containing cached material names
cache_valid_time = 7 * 24 * 60 * 60 # 7 days in seconds (604800s)

material_ignore_file = "materials.ignore" # File containing material names to ignore
material_ignore = [] # List of material names to ignore

mat_files = [] # List of material files

### Material Ignore File ###
# 1. Check if materials.ignore file exists
# 2. If it does, read the file and add the material names to the material_ignore list
# 3. If it does not, create the file
if os.path.exists(material_ignore_file): # check if materials.ignore file exists
    with open(material_ignore_file, "r") as f:
        material_ignore = f.read().splitlines()
else: # create materials.ignore file
    with open(material_ignore_file, "w") as f:
        f.write("")

### Cache File ###
# 1. Check if cache file exists and is valid
# 2. If it does, read the file and add the material names to the mat_files list
# 3. If it does not, show the directory selection dialog
if os.path.exists(cache_file) and (time.time() - os.path.getmtime(cache_file)) < cache_valid_time: # Check if cache file exists and is valid
    with open(cache_file, "r") as f:
        chached_mat_files = f.read().splitlines()
        for mat in chached_mat_files:
            if mat not in material_ignore: # Check if material is in ignore list
                mat_files.append(mat)
else: # Cache file does not exist or is invalid
    directory = filedialog.askdirectory() # Show the directory selection dialog

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".mat"): # Check if file is a material file
                mat_name = os.path.basename(file).replace(".mat","") # Get the material name from the file name and remove the .mat extension
                if mat_name not in material_ignore: # Check if material is in ignore list
                    mat_files.append(mat_name)

    if len(mat_files) == 0: # No material files found
        print("No material files found in the directory. Please select a correct folder.")
        sys.exit()

    mat_files = list(set(mat_files)) # Remove duplicates

    with open(cache_file, "w") as f: # Write the material names to the cache file
        f.write("\n".join(mat_files))

### Add Materials ###
# 1. Check if first python script parameter is "debug"
# 2. If it is, print the material names to the console
# 3. If it is not, add the material to Pixyz Material Library using the PixyzMaterialLibrary.add_material function
for mat_file in mat_files:
    # if first python script parameter is "debug" skip line below
    if len(sys.argv) > 1 and sys.argv[1] == "debug":
        print(mat_file)
    else:
        # PixyzMaterialLibrary.add_material(mat_file)
        pass