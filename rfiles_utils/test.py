import os
import shutil
from variables import from_dir, to_dir

subpaths = []
subdirs = []
subfiles = []
filepaths = []
dir_info = []

for subpath, subdir, file in os.walk(from_dir):
    subpaths.append(subpath)
    subdirs.extend(subdir)
    subfiles.append(file)
    filepaths.append(subpath)

if len(subpaths) == len(subfiles):
    indexed_subpaths = enumerate(subpaths)
    subpaths_and_file_names = [(subpath, subfiles[index]) for index, subpath in indexed_subpaths]

# for 

print(f"{subpaths_and_file_names}")
# print(len(subpaths)[subpath, subfile[subpath]] for subpath in subpaths
# print(len(subfiles))
# dir_info = [subpaths, subdirs, subfiles, filepaths]

# print(dir_info)