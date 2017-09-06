"""
看 pyglet 內, __init__.py, 的檔案, 到底import了什麼.

下面二個from, 跟我以前認知的 from xxx.yyy import zzz 是不一樣, 

from xxx.yyy 是指yyy這個package folder在xxx下面, 要import 裡面yyy的東西, 

這裡就不一樣了,  我想__future__ 是那個module的名字也就是  __name__ ,

當它被檔成module, __name__ 就會給它的名字.

from __future__ import print_function
from __future__ import absolute_import

這塊如我所料, window 有先被import進來.
if False:
    from . import app
    from . import canvas
    from . import clock
    from . import com
    from . import event
    from . import font
    from . import gl
    from . import graphics
    from . import input
    from . import image
    from . import lib
    from . import media
    from . import resource
    from . import sprite
    from . import text
    from . import window


看來, 最簡單的import 方式, 就是在 __init__內, 

把要的東西, 用from . import zzz 進來, zzz 不見得是package *.py , 

我想其它*.py內的東西也可以.


我想呢, 因該是 因為這是 ssh 連結, 所以不給我 Window() 嗎?

也怪怪的, 不能跑, 至少也要能讓我寫丫.
window = pyglet.window.Window()
Reference: https://pyglet.readthedocs.io/en/latest/index.html
"""

