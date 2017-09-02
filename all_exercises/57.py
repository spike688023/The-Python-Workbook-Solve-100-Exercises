#Get the file in the attachment and produce the printed output
import json
from pprint import pprint

with open("company1.json","r") as file:
    d = json.load(file)

# 用下面這行會有錯
#d = json.load("company1.json")

pprint(d)


"""
這裡可以再想一個東西，我用 open 可以把檔案導出來， 多弄個json 去load，
應該 只是為了，用json 相關func


這個func的說明寫，跟read 很像，但它能吃json 格式。
    load(fp, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)
            Deserialize ``fp`` (a ``.read()``-supporting file-like object containing
                    a JSON document) to a Python object.

這塊是想了解, 這個module 的結構, 以了解怎麼使用它:
>>> dir(json)
['JSONDecoder', 'JSONEncoder', '__all__', '__author__', '__builtins__', '__cached__', '__doc__', '__file__', '__name__', '__package__',
 '__path__', '__version__', '_default_decoder', '_default_encoder', 'decoder', 'dump', 'dumps', 'encoder', 'load', 'loads', 'scanner']



help(json.JSONDecoder)
Help on class JSONDecoder in module json.decoder:

help(json.decoder)
Help on module json.decoder in json:


android@mec18:/usr/lib/python3.2/json$ ls
decoder.py  encoder.py  __init__.py  __pycache__  scanner.py  tool.py

class JSONEncoder(object): 是實作在　encoder.py 裡面。　


CLASSES
    builtins.object
        json.decoder.JSONDecoder
        json.encoder.JSONEncoder



|  decode(self, s, _w=<built-in method match of _sre.SRE_Pattern object>)
|      Return the Python representation of ``s`` (a ``str`` instance
|      containing a JSON document).





在__init__.py 內，　會show出來在 help() 看到的東西，　

只有""" """ 內的東西，　　還有　　一些func的定義，　

其它的東西如  實作跟給定值給 private 變數，　則不會show出來。


如下面這段，　　不會在 help 中山現。
__version__ = '2.0.9'
__all__ = [
    'dump', 'dumps', 'load', 'loads',
    'JSONDecoder', 'JSONEncoder',
]

__author__ = 'Bob Ippolito <bob@redivi.com>'


json.JSONDecoder().decode ; 我這樣呼叫可以, 想必是下面這段的import ,

它是寫在__init__.py

from .decoder import JSONDecoder
from .encoder import JSONEncoder

_default_encoder = JSONEncoder(
    skipkeys=False,
    ensure_ascii=True,
    check_circular=True,
    allow_nan=True,
    indent=None,
    separators=None,
    default=None,
)






以下是我, 在交談介面的操作, 但不是很懂json module ,

雖然好像印出了, 題目要的東西.
>>> import json
>>> json.JSONDecoder()
<json.decoder.JSONDecoder object at 0x192ca10>
>>> file  = open("company1.json".r)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'str' object has no attribute 'r'
>>> file  = open("company1.json","r")
>>> json.JSONDecoder().encoder(file)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'JSONDecoder' object has no attribute 'encoder'
>>> json.JSONDecoder().decode(file)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/lib/python3.2/json/decoder.py", line 351, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
TypeError: expected string or buffer
>>> json.JSONDecoder().decode(file.read())
{'employees': [{'lastName': 'Doe', 'firstName': 'John'}, {'lastName': 'Smith', 'firstName': 'Anna'}, {'lastName': 'Jones', 'firstName': 'Peter'}], 'owners': [{'lastName': 'Petter', 'firstName': 'Jack'}, {'lastName': 'Petter', 'firstName': 'Jessy'}]}


由下面的實作，可以了解， 為什麼要一個
json module 來處理檔案， 一班 檔案讀進來，只是文本，用指標去抓東西，
或復寫東西， 它無法分辦dict 格式的資料，
但經過 json.load 會把資料變成dict 格式。
>>> import json
>>> file = open("company1.json","r")
>>> d = json.load(file)
>>> type(d)
<class 'dict'>
>>> type(file)
<class '_io.TextIOWrapper'>
>>> file
<_io.TextIOWrapper name='company1.json' mode='r' encoding='US-ASCII'>
>>> help(file)

"""
