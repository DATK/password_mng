from flask import Flask, request, render_template, redirect, abort
from random import randint
import json
from src.app import User, Manager
from src.config import port,ip
app = Flask(__name__)

users_ident={}
#"name_user:[randkey,user]"


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
    if request.method == "POST":
        login, password = request.form["login"], request.form["pass"]
        usr = User(login, password)
        if usr.auth():
            name_user = usr.get()[0]
            tmp=randint(10000000,99999999999)
            if login not in users_ident:      
                users_ident[login]=[f"{tmp}",usr]
            else:
                del usr
                return "Вы уже вошли в аккаунт на другом устройстве"
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


@app.route("/autoris/<name>", methods=["GET"])
def autorisation(name):
    global users_ident
    if request.method == "GET":
        return redirect(f"http://{ip}:{port}/main_page/{name}/{users_ident[name][0]}")
    else:
        return abort(405)


@app.route("/main_page/<name>/<key>", methods=["POST", "GET"])
def main(name,key):
    try:
        mng=Manager(name,users_ident[name][-1])
    except KeyError:
        return ("Выполните повторный вход")
    print(key,users_ident[name])
    if key!=users_ident[name][0]:
        return abort(403)
    if request.method == "POST" and mng.chek_usr_auth(name):
        try:
            if request.form["exit"]=="":
                del users_ident[name]
                return redirect(f"http://{ip}:{port}/")
        except:
            pass
        try:
            login, password = request.form["login"], request.form["pswrd"]
            if request.form["del"]=="":
                mng.set(login,password)
                mng.del_dt()
        except:
            login, password = request.form["login"], request.form["pswrd"]
            mng.set(login,password)
            mng.save()
        tmp=randint(10000000,99999999999)
        users_ident[name][0]=str(tmp)
        return redirect(f"http://{ip}:{port}/main_page/{name}/{tmp}")
    
    elif request.method == "GET" and mng.chek_usr_auth(name):
        data=mng.output()
        return render_template("index3.html",data=data)
    else:
        return abort(403)


