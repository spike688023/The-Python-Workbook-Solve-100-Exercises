"""
好拉,  這題, 應該用下面的function, 就能解決.
help(os)
    listdir(...)
        listdir([path]) -> list_of_strings

        Return a list containing the names of the entries in the directory.

            path: path of directory to list (default: '.')

        The list is in arbitrary order.  It does not include the special
        entries '.' and '..' even if they are present in the directory.
"""
import os 
list1 = [ i for i in os.listdir("files") if ".py" in i]
print(len(list1))
    

