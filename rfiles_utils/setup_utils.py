import os
import shutil
from variables import from_dir, to_dir

def get_dir_info(dir, print_info=False):
    subpaths = [] 
    subdirs = [] 
    filepaths = []
    new_filepaths = []
    dir_info = []

    for subpath, subdir, file in os.walk (dir):
        subpaths.append(subpath)
        subdirs.extend(subdir)
        filepaths.extend(file)
        print(file)

    dir_info = [subpaths, subdirs, filepaths]

    if print_info:
        print(dir_info)

    return dir_info

subpaths_list = get_dir_info(from_dir)[0]
subdirs_list = get_dir_info(from_dir)[1]
filepaths_list = get_dir_info(from_dir)[2]
# print(filepaths_list)

def copy_files_to_dir(files_to_copy = [], to_dirs = []):
    files_and_dirs = [[file, dir] for file, dir in zip(files_to_copy, to_dirs)]
    for file, dir in files_and_dirs:
        shutil.copy(file, dir)

# copy_files_to_dir(subpaths_list, filepaths_in_dir)