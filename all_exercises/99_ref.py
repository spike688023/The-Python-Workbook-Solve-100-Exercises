from flask import Flask
app = Flask(__name__)

@app.route('/<username>')
def hello_world(username):
    # 這裡return 可以看成是，回傳到網頁中，要呈現給使用者看的東西。
    return 'Hello %s, World!' % username

if __name__=='__main__':
    app.run()
"""
這裡的app.run , 如果寫在__main__,

跟不寫在裡面，我覺得得是有差的，

這裡因為例子很簡單， 所以拿掉


if __name__=='__main__':  這行 ，

也是能正常 運作。

直接擷路，網頁裡的說明。

Next we create an instance of this class. The first argument is the name of the application’s module or package. If you are using a single module (as in this example), you should use __name__ because depending on if it’s started as application or imported as module the name will be different ('__main__' versus the actual import name). This is needed so that Flask knows where to look for templates, static files, and so on. For more information have a look at the Flask documentation.

reference:
http://flask.pocoo.org/docs/0.12/quickstart/#a-minimal-application

這是把module 轉成package,

首先，要開二個相同module名字的folder, 一個在一個的裡面，然後 把module，

改成__init__.py 放在第二層module folder裡面， 再到第一層裡面新增

setup.py , 因為原本的module 變成了 __init__.py，所 以不能用𠩤本跑 的方式。
Reference:
http://flask.pocoo.org/docs/0.12/patterns/packages/

這裡講 render 跟template

template 有點像，一般， 我們之前的HTML格式 ， 但多了{}這種大括號 ，

用做條件，或flow的控制，

最簡單的hello world，只要用return，就會出現在 網頁上，

但如果要傳資料給 template 通常 會用到render_template() 之前的function，

裡面通常 會有  xxx.html 檔，跟一些 變數。
Reference:
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-ii-templates
http://www.frogjumpjump.com/2015/12/the-flask-mega-tutorial-part-ii.html



"""
