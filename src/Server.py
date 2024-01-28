from flask import Flask, request, render_template, redirect, abort
from src.app import User, Manager
from src.config import port
app = Flask(__name__)
user="obj"
ip="localhost"
@app.route("/", methods=["POST", "GET"])
def wlc():
    if request.method == "POST":
        try:
            if request.form["inside"] == "":
                return redirect(f"http://{ip}:{port}/inside")
            else:
                return "1"
        except:
            if request.form["reg"] == "":
                return redirect(f"http://{ip}:{port}/registation")
            else:
                return "1"
    elif request.method == "GET":
        return render_template("index4.html")


@app.route("/inside", methods=["POST", "GET"])
def input():
    global user
    if request.method == "POST":
        login, password = request.form["login"], request.form["pass"]
        usr = User(login, password)
        user=User(login, password)
        if usr.auth():
            name_user = usr.get()[0]
            del usr
            return redirect(f"http://{ip}:{port}/autoris/{name_user}")
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
            return redirect(f"http://{ip}:{port}/inside")
        else:
            return render_template("index2.html")
    elif request.method == "GET":
        return render_template("index2.html")


@app.route("/autoris/<name>", methods=["POST", "GET"])
def autorisation(name):
    if request.method == "POST":
        return redirect(f"http:/{ip}:{port}/main_page/{name}")
    elif request.method == "GET":
        return redirect(f"http://{ip}:{port}/main_page/{name}")
    else:
        return abort(405)


@app.route("/main_page/<name>", methods=["POST", "GET"])
def main(name):
    mng=Manager(name,user)
    if request.method == "POST" and mng.chek_usr_auth(name):
        try:
            login, password = request.form["login"], request.form["pswrd"]
            if request.form["del"]=="":
                mng.set(login,password)
                mng.del_dt()
        except:
            login, password = request.form["login"], request.form["pswrd"]
            mng.set(login,password)
            mng.save()
                
        return redirect(f"http://{ip}:{port}/main_page/{name}")
    
    elif request.method == "GET" and mng.chek_usr_auth(name):
        data=mng.output()
        return render_template("index3.html",data=data)
    else:
        return abort(403)


