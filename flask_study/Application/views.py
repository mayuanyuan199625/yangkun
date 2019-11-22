"""
类视图
类视图好处，可以继承 把一些共性的东西抽取出来放到父视图中 子视图直接拿出来用就可以了

"""
from flask import Flask,views,jsonify
from flask import request,redirect,url_for,render_template,flash
from Application.model import User
from Application import db
import json
class JsonView(views.View):
    def get_data(self):
        raise NotImplementedError #get_data 必须实现 不实现会报错

    def dispatch_request(self):
        return jsonify(self.get_data())


class ListView(JsonView):
    def get_data(self):
        return {'username':'zhangsan','password':'1111111'}


"""
基于调度的类视图

"""
class LoginView(views.MethodView):
    def get(self):
        # return "这是get请求返回值"
        return render_template("login.html")

    def post(self):
        username = request.form.get("username")
        password = request.form.get("password")
        print(username)
        print(password)
        if username and password:
            if username == "yangkun" and password == "123456":
                return "登陆成功..."
            else:
                return "账号或者密码输入错误..."
        else:
            return "账号或者密码为空"


"""注册类提交是否成功"""
class Regist(views.MethodView):
    def __init__(self):
        self.error = None

    def get(self):
        return render_template("regist.html",error=self.error)

    def post(self):
        if request.form.get("password1") != request.form.get("password2"):
            self.error = '两次密码不相同...请仔细检查下亲QAQ'
        else:
            user1 = User(id=6, nickname=request.form.get("username"), password_hash=request.form.get("password1"), payPassword=345353, money=0, isAdmin=0)
            db.session.add(user1)
            db.session.commit()
            flash("成功注册...")
            return redirect(url_for("login"))


        return render_template("regist.html",error=self.error)