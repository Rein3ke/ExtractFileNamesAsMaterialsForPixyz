# author: Marvin Kullick

import os  # Import the os module to read the directory
import sys  # Import the sys module to read the first python script parameter
import time  # Import the time module to check the cache file time
import configparser  # Import the configparser module to read the materials.config file
import PixyzHelper

import tkinter as tk  # Import the tkinter module to show the directory selection dialog
from tkinter import filedialog  # Import the filedialog module to show the directory selection dialog

root = tk.Tk()  # Create the root window
root.withdraw()  # Hide the root window

materials_config_file_path = "../materials.ini"  # File containing the materials configuration

create_cache_file = True  # Create cache file
cache_file_path = "../materials.cache"  # File containing cached material names
cache_valid_time = 604800  # Cache file valid time in seconds (default: 7 days)

material_ignore_file_path = "../materials.ignore"  # File containing material names to ignore
material_ignore = []  # List of material names to ignore

mat_files = []  # List of material files


def __main__():  # Main function
    load_config()  # Check if materials.config file exists and load the configuration
    load_material_ignore_file()  # Check if materials.ignore file exists
    load_from_cache()  # Check if cache file exists and is valid
    add_materials()  # Add materials to Pixyz Material Library


def load_config():
    """Check if materials.ini file exists and load the configuration. Otherwise, create the file with default values."""

    global create_cache_file, cache_valid_time

    config = configparser.ConfigParser()  # Create the config parser object

    if not config.read(materials_config_file_path):
        config['CACHE'] = {'create_cache_file': 'True', 'cache_valid_time': '604800'}
        with open(materials_config_file_path, 'w') as configfile:
            config.write(configfile)
    else:
        config.read(materials_config_file_path)  # Read the materials.config file

        try:
            create_cache_file = config.getboolean('CACHE', 'create_cache_file')
            cache_valid_time = config.getint('CACHE', 'cache_valid_time')
        except:
            print("Invalid configuration file. Please check the materials.ini file.")
            sys.exit()
        else:
            print("Configuration loaded successfully.")


# Material Ignore File
# 1. Check if materials.ignore file exists
# 2. If it does, read the file and add the material names to the material_ignore list
# 3. If it does not, create the file
def load_material_ignore_file():
    global material_ignore

    if os.path.exists(material_ignore_file_path):  # check if materials.ignore file exists
        with open(material_ignore_file_path, "r") as f:
            material_ignore = f.read().splitlines()
    else:  # create materials.ignore file
        with open(material_ignore_file_path, "w") as f:
            f.write("")


# Cache File
# 1. Check if cache file exists and is valid
# 2. If it does, read the file and add the material names to the mat_files list
# 3. If it does not, show the directory selection dialog
def load_from_cache():
    global mat_files

    # Check if cache file exists and is valid
    if os.path.exists(cache_file_path) and (time.time() - os.path.getmtime(cache_file_path)) < cache_valid_time:

        with open(cache_file_path, "r") as f:
            cached_mat_files = f.read().splitlines()
            for mat in cached_mat_files:
                if mat not in material_ignore:  # Check if material is in ignore list
                    mat_files.append(mat)
    else:  # Cache file does not exist or is invalid
        directory = filedialog.askdirectory()  # Show the directory selection dialog

        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith(".mat"):  # Check if file is a material file
                    mat_name = os.path.basename(file).replace(".mat", "")  # Get the material name
                    if mat_name not in material_ignore:  # Check if material is in ignore list
                        mat_files.append(mat_name)

        if len(mat_files) == 0:  # No material files found
            print("No material files found in the directory. Please select a correct folder.")
            sys.exit()

        mat_files = list(set(mat_files))  # Remove duplicates

        create_cache()


# Create Cache File
def create_cache():
    if create_cache_file:  # Create cache file if create_cache_file is True
        with open(cache_file_path, "w") as f:  # Write the material names to the cache file
            f.truncate(0)  # Clear the file
            f.write("\n".join(mat_files))


# Add Materials
def add_materials():
    for mat_file in mat_files:
        # if first python script parameter is "debug" skip line below
        if len(sys.argv) > 1 and sys.argv[1] == "debug":
            print(mat_file)

        PixyzHelper.add_material(mat_file)


__main__()  # Run the main function
