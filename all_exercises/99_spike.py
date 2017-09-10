"""
看來,  是要, 灌flask來用.

http://localhost:5000/  從這可以看出來，很多localhost,

我可以一起跑，沒差， 換port 而已。

Variable Rules:

這段的意思， username是使用者多打的url ，

這裡route 的解讀， 把它當成變數來用。
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

Static Files:

Dynamic web applications also need static files. That’s usually where the CSS and JavaScript files are coming from.



Rendering Templates:

Here’s a simple example of how to render a template:

    from flask import render_template

    @app.route('/hello/')
    @app.route('/hello/<name>')
    def hello(name=None):
        return render_template('hello.html', name=name)


So if your application is a module, this folder is next to that module, if it’s a package it’s actually inside your package:

    Case 1: a module:

    /application.py
    /templates
        /hello.html

    Case 2: a package:

    /application
        /__init__.py
        /templates
            /hello.html


Redirects and Errors:

To redirect a user to another endpoint, use the redirect() function; to abort a request early with an error code, use the abort() function:

    from flask import abort, redirect, url_for

    @app.route('/')
    def index():
        return redirect(url_for('login'))

    @app.route('/login')
    def login():
        abort(401)
        this_is_never_executed()

"""
