import os
import sys

def scan_module(filepath):
    print("====================================== Scan module ======================================")
    target_dir = os.path.dirname(os.path.abspath(filepath))
    print("target directory", target_dir)
    return sys.path.append(target_dir)

def scan_main(filepath):
    print("====================================== Scan Main ======================================")
    target_dir = os.path.dirname(os.path.abspath(filepath))
    print("target directory", target_dir)

    for filename in os.listdir(target_dir):
        if filename.lower() == "main.py":
            return os.path.join(target_dir, filename)
    return None

# 遞迴搜尋子資料夾
# def find_main_py_recursive(root_dir):
#     for dirpath, _, filenames in os.walk(root_dir):
#         for filename in filenames:
#             if filename.lower() == "main.py":
#                 return os.path.join(dirpath, filename)
#     return None
