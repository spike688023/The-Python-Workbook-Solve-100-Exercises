"""
應該是手這個解沒錯, 每個folder都會跑下去, files的list如果為空, 

就不理它.
>>> for root, dirs, files in os.walk('files'):
...     print(root)
...     print(dirs)
...     print(files)
...
files
['subdirs']
['file3.py', 'file1.txt', 'file4.py', 'file2.txt', 'file5.txt']
files/subdirs
['level12', 'level11']
[]
files/subdirs/level12
['level121']
['6.txt']
files/subdirs/level12/level121
[]
['5.py', '3.txt', '6.py']
files/subdirs/level11
[]
['1.txt', '2.txt', '4.py']

"""

import os
import glob
all = []
for root, dirs, files in os.walk('subdirs'):
    if len(files) != 0 : all = all + glob.glob1(root,"*.py")

print(len(all))
