from flask import Flask, request, render_template, redirect, abort
from src.app import User, Manager

app = Flask(__name__)

autoris = False
mng=Manager()

@app.route("/", methods=["POST", "GET"])
def wlc():
    if request.method == "POST":
        try:
            if request.form["inside"] == "":
                return redirect("http://127.0.0.1:5000/inside")
            else:
                return "1"
        except:
            if request.form["reg"] == "":
                return redirect("http://127.0.0.1:5000/registation")
            else:
                return "1"
    elif request.method == "GET":
        return render_template("index4.html")


@app.route("/inside", methods=["POST", "GET"])
def input():
    global autoris
    if request.method == "POST":
        login, password = request.form["login"], request.form["pass"]
        usr = User(login, password)
        if usr.auth():
            name_user = usr.get()[0]
            del usr
            autoris = True
            return redirect(f"http://127.0.0.1:5000/autoris/{name_user}")
        return render_template("index1.html")
    elif request.method == "GET":
        return render_template("index1.html")


@app.route("/registation", methods=["POST", "GET"])
def reg():
    if request.method == "POST":
        login, password = request.form["login"], request.form["pass"]
        usr = User(login, password)
        if usr.reg():
            del usr
            return redirect("http://127.0.0.1:5000/inside")
        else:
            return render_template("index2.html")
    elif request.method == "GET":
        return render_template("index2.html")


@app.route("/autoris/<name>", methods=["POST", "GET"])
def autorisation(name):
    if request.method == "POST" and autoris:
        return redirect("http://127.0.0.1:5000/main_page")
    elif request.method == "GET" and autoris:
        return redirect("http://127.0.0.1:5000/main_page")
    else:
        return abort(405)


@app.route("/main_page", methods=["POST", "GET"])
def main():
    if request.method == "POST" and autoris:
        try:
            login, password = request.form["login"], request.form["pswrd"]
            if request.form["del"]=="":
                mng.set(login,password)
                mng.del_dt()
        except:
            login, password = request.form["login"], request.form["pswrd"]
            mng.set(login,password)
            mng.save()
                
        return redirect("http://127.0.0.1:5000/main_page")
    
    elif request.method == "GET" and autoris:
        data=mng.output()
        return render_template("index3.html",data=data)
    else:
        return abort(403)


