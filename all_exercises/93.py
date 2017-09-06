#Count files with a .py extension in root1 directory and its subdirectories
#This solution works for the previous exercise as well with one file in a directory

"""
案, 還是它寫的好一點.
"""
import glob

file_list = glob.glob("subdirs/**/*.py", recursive=True)
print(len(file_list))
