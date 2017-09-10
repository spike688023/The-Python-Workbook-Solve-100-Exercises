"""
中間帳密的比對，是拿81題 的來用，用作者的。
"""
from flask import Flask, request, render_template
app = Flask('flask100')

#import yourapplication.views
@app.route('/', methods=['POST', 'GET'])
def index():
    message = ""
    usr = ""
    psw = ""
    usr = request.args.get("user")

    with open("users.txt", "r") as file:
        users = file.readlines()
        users = [i.strip("\n") for i in users]


    notes = []
    psw = request.args.get("password")
    print(request.args)
    print(psw)
    if psw != None and not any(i.isdigit() for i in psw):
        notes.append("You need at least one number")
    if psw != None and not any(i.isupper() for i in psw):
        notes.append("You need at least one uppercase letter")
    if psw != None and len(psw) < 5:
        notes.append("You need at least 5 characters")


    if usr != None and usr in users and len(notes) == 0:
        message = "Success!"
        return render_template("index.html", msg = message)
    elif usr != None and usr in users and len(notes) > 0:
        message = "Username Exists!"
        return render_template("index.html", msg = message)
    else:
        message = "Username is fine"
        #第三個參數，只是要看，能不能傳list結構過去而已。
        return render_template("index.html", msg = message, error=notes)

    return render_template("index.html")

if __name__=='__main__':
    app.run()
