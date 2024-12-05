import glob
from pathlib import Path
import os


def find_dir(dir_name, search_path="."):
    pattern = f"{search_path}/**/{dir_name}"
    results = glob.glob(pattern, recursive=True)
    return results


def consolidate_files(folder_name, target_file):
    # get path to the selected folder
    home_dir = str(Path.home())
    dir_path = find_dir(folder_name, home_dir)

    # list all py files in the source directory
    files = os.listdir(dir_path[1])
    py_files_list = [file for file in files if file.endswith(".py")]

    # copy the contents of all py files into a single txt file
    with open(target_file, "a+") as output_file:
        output_file.truncate(0)
        for py_file in py_files_list:
            with open(f"{dir_path[1]}/{py_file}", "r") as input_file:
                contents = input_file.read()
                output_file.write("\n" + "=" * 20 + "\n")
                output_file.write(f"FILE:{py_file}" + "\n\n")
                output_file.write(contents)


consolidate_files("Client-Server-App", "full.cr.txt")