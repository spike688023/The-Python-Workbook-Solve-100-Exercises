#Name the file datetime.py and fix the error
import requests
print(__name__)

r = requests.get("http://www.pythonhow.com")
print(r.text[:100])

print(__name__)

"""

import requests
print(help(requests))

r = requests.get("http://www.pythonhow.com")
print(r.text[:100])


會印出東西如下, 好酷喔，它把當下folder內的這個檔案檔成module了，
由這可以推敲出，import moduel，第一步是先找當目録，找不到，才到這個python 的

環 境變數去找，拿最下面， 我放的code來看，用不同的python版本，去執行，會跑出它各自的

環境變數：
Help on module requests:

    NAME
        requests

        FILE
            /Users/nickboy/Temp/requests.py

            (END)


import sys

#Python Paht:
for ref in sys.path:
        print(ref)


還有另一個方法，可以看， 當下程 式，是主程 式呢，還是被當然module執 行 呢？
用 __name__:

因為，我檔名是取 requests.py ，所 以會跑 出request ,
用目前的69.py則不會， 它會跑 出 __main__ , 因為它是主程 式，

不是module.
abliarsecde-MacBookPro:Temp nickboy$ python3.6 requests.py

None
requests

"""

