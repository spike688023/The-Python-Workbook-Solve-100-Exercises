#import flask
from flask import Flask, request, render_template
app = Flask('flask99')

file = open("99_file.txt","w+")

#import yourapplication.views
@app.route('/', methods=['POST', 'GET'])
def index():
    #return 'Hello 0909 World!'
    print(request.method)
    print(request)
    print(request.args)
    print(request.args.get("lines"))
    #if request.method == 'POST':
    if request.args.get("lines") != None:
        string = str( request.args.get("lines") )+ "\n"
        file.write(string)
        file.flush()
        #return '%s!'% request.args.get("lines")
        return render_template("index.html",back=request.args.get("lines"))
    else:
        return render_template("index.html",name="Paul")

@app.route('/<lines>')
def lines(lines):
    return '%s'% lines

if __name__=='__main__':
    app.run()
