#Print out the text of this file www.pythonhow.com/data/universe.txt. Please don't manually download the file. Let Python do all the work.
import requests

response = requests.get("http://www.pythonhow.com/data/universe.txt")
text = response.text
print(text)

"""
這是從 help(request) 中抓出來的， 雖然例子有寫到 text，

但說明書，並沒有提到這個參數丫。
       >>> payload = dict(key1='value1', key2='value2')
              >>> r = requests.post('http://httpbin.org/post', data=payload)
                     >>> print(r.text)
                            {
                                             ...
                                                      "form": {
                                                                     "key2": "value2",
                                                                                "key1": "value1"
                                                                                         },
                                                                                                  ...
                                                                                                         }


以下是實驗，看 ，要怎麼抓出有text 這個data 可以抓出來看，

首先要知道回傳的r 是什麼型態，才能用help去看怎麼操作，

但是呢，help回傳的東西，有時， 講 的不詳細，可能要用dir()  ,

跑 出來的東西比較 詳細，但是都沒有說明。

像是requests 這個modue， 它沒有說明 get func , 我是用dir() ，

才看到有列出來。
>>> r = requests.get('https://www.python.org')
>>> r
<Response [200]>
>>> type(r)
<class 'requests.models.Response'>
>>> help(requests.models.Response)

>>> r.ok
True


>>> dir(requests)
['ConnectTimeout', 'ConnectionError', 'DependencyWarning', 'FileModeWarning', 'HTTPError', 'NullHandler', 'PreparedRequest', 'ReadTimeout', 'Request', 'RequestException', 'RequestsDependencyWarning', 'Response', 'Session', 'Timeout', 'TooManyRedirects', 'URLRequired', '__author__', '__author_email__', '__build__', '__builtins__', '__cached__', '__cake__', '__copyright__', '__description__', '__doc__', '__file__', '__license__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__title__', '__url__', '__version__', '_internal_utils', 'adapters', 'api', 'auth', 'certs', 'chardet', 'check_compatibility', 'codes', 'compat', 'cookies', 'delete', 'exceptions', 'get', 'head', 'hooks', 'logging', 'models', 'options', 'packages', 'patch', 'post', 'put', 'request', 'session', 'sessions', 'status_codes', 'structures', 'urllib3', 'utils', 'warnings']


找到了，我就 在想 help 列的那麼少，這裡用 dir()  列的這麼多，

它是去那抓的， 我想dir() 是去 __init__ 抓關 鍵字 import ，把後 面的東西，

都給弄進來  , 看來是這樣沒錯，那大小寫呢？

好吧，小寫都算成是function  , 大寫都看成是 class, 我記得 有例外，

但先這樣吧。
>>> requests.Session
<class 'requests.sessions.Session'>

from . import utils
from . import packages
from .models import Request, Response, PreparedRequest
from .api import request, get, head, post, patch, put, delete, options
from .sessions import session, Session
from .status_codes import codes

from .exceptions import (
            RequestException, Timeout, URLRequired,
                TooManyRedirects, HTTPError, ConnectionError,
                    FileModeWarning, ConnectTimeout, ReadTimeout
                    )

注意到了， PACKAGE CONTESTS ， 就 是上面import 用到的。
PACKAGE CONTENTS
    __version__
        _internal_utils
            adapters
                api
                    auth
                        certs
                            compat
                                cookies
                                    exceptions
                                        help
                                            hooks
                                                models
                                                    packages
                                                        sessions
                                                            status_codes
                                                                structures
                                                                    utils
"""
