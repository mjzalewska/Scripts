import glob
from pathlib import Path
import os


def find_dir(dir_name, search_path="."):
    pattern = f"{search_path}/**/{dir_name}"
    results = glob.glob(pattern, recursive=True)
    return results


home_dir = Path.home()
dir_path = find_dir("Client-Server-App", home_dir)
files = os.listdir(dir_path[0])
py_files_list = [file for file in files if file.endswith(".py")]

with open("full.cr.txt", "a+") as output_file:
    for py_file in py_files_list:
        with open(f"{dir_path[0]}/{py_file}", "r") as input_file:
            contents = input_file.read()
            output_file.write("\n" + "=" * 20 + "\n")
            output_file.write(f"FILE:{py_file}" + "\n\n")
            output_file.write(contents)
