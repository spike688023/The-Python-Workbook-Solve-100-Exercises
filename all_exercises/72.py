#Create a script that let the user type in a search term and opens and search on the browser for that term on Google

import webbrowser

query = input("Enter your Google query: ")
url = "https://www.google.com/?gws_rd=cr,ssl&ei=NCZFWIOJN8yMsgHCyLV4&fg=1#q=%s" % str(query)
webbrowser.open_new(url)


"""
哇，這題 是真的不會，  但有查到webbrowser ，

這題 是有點作必的， 要先把goole用的查詢格式，先給抓下來，


>>> url = "https://www.google.com.tw/search?q=%s" % str("movie")
>>> webbrowser.open_new(url)


今天在看help() 的時侯，又注意到新東西了，

這是個function的定義, 前面三個參數要給 ，self  我有點忘了，

要怎麼解釋它，  但這裡要說的是  body=None ，這種 有給 值的 ，

代表， 有預設 值， 我們可以先不用給 ，  真的有需求再用。

|  urlopen(self, method, url, body=None, headers=None, retries=None, redirect=True, assert_same_host=True, timeout=<object object at 0x108eb2360>, pool_timeout=None, release_conn=None, chunked=False, body_pos=None, **response_kw)


看這個例子就 知道了。
class MyClass(object):
        def __init__(self, x, y):
                    self.x = x
                            self.y = y

下面是網 路上，某個人的講 解：

I like to quote Peters' Zen of Python. "Explicit is better than implicit."

In Java and C++, 'this.' can be deduced, except when you have variable names that make it impossible to deduce. So you sometimes need it and sometimes don't.

Python elects to make things like this explicit rather than based on a rule.

Additionally, since nothing is implied or assumed, parts of the implementation are exposed. self.__class__, self.__dict__ and other "internal" structures are available in an obvious way.
"""
