# Please print the script in the expected output

from datetime import datetime

print(datetime.now().strftime("Today is %A, %B %d, %Y"))

"""

這題 還是有看 python 官網 的document ，看來， 只要知道，

要用什麼module 接下來去官網 看教學， 是最快的,

因為有很多的例子。
>>> from datetime import datetime, date, time
>>> now = datetime.now()
>>> now
datetime.datetime(2017, 9, 3, 3, 13, 39, 602715)
>>> now.strftime("%A, %d. %B %Y %I:%M%p")
'Sunday, 03. September 2017 03:13AM'
>>> now.strftime("Today is %A, %B %d, %Y")
'Today is Sunday, September 03, 2017'


strftime() 的用法，要看這裡, help() 教的不多：

https://docs.python.org/3.6/library/datetime.html#strftime-strptime-behavior

%A	Weekday as locale’s full name.
%B	Month as locale’s full name.
%d	Day of the month as a zero-padded decimal number.
%Y	Year with century as a decimal number.
"""
