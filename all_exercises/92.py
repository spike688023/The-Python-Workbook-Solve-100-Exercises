#Count files with a .py extension inside the root1 directory]
"""
案, 完全不知道是用這個.

用help 跟dir 看到的資訊會有落差, 但, 

dir還是比較完整, 雖然很難看,都沒講解, 就沒用 三個雙引號夾住, 去解釋它, 

所以沒show 出來.
>>> dir(glob)
['__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__name__', '__package__', 'fnmatch', 'glob', 'glob0', 'glob1', 'has_magic', 'iglob', 'magic_check', 'magic_check_bytes', 'os', 're']
>>> help(glob)


要知道用法, 只能去 看檔案了.
/usr/lib/python3.2/glob.py

"""

import glob
file_list=glob.glob1("files","*.py")
print(len(file_list))
