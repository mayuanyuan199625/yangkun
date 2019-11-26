"""
类视图
类视图好处，可以继承 把一些共性的东西抽取出来放到父视图中 子视图直接拿出来用就可以了

"""
from flask_sqlalchemy import SQLAlchemy
from flask import Flask,views,jsonify
from flask import request,redirect,url_for,render_template,flash,session
from ..Application.model import User
from ..Application import db
from sqlalchemy.ext.declarative import DeclarativeMeta
from functools import wraps
import json


"""SQLAlchemy查询结果 由对象转为字典"""
class AlchemyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)
                try:
                    json.dumps(data) # this will fail on non-encodable values, like other classes
                    fields[field] = data
                except TypeError:
                    fields[field] = None
            # a json-encodable dict
            return fields

        return json.JSONEncoder.default(self, obj)


class JsonView(views.View):
    def get_data(self):
        raise NotImplementedError #get_data 必须实现 不实现会报错

    def dispatch_request(self):
        return jsonify(self.get_data())


class ListView(JsonView):
    def get_data(self):
        return {'username':'zhangsan','password':'1111111'}


"""登陆检测装饰器"""
def login_required(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        if session.get('username'):
            return func(*args,**kwargs)
        else:
            return redirect(url_for('login'))
    return wrapper


"""登陆验证"""
class LoginView(views.MethodView):
    def get(self):
        # return "这是get请求返回值"
        return render_template("login.html")

    def post(self):
        error = None
        if self.valid_login(request.form['username'],request.form['password']):
            flash("成功登陆!")
            session['username'] = request.form.get('username')
            return redirect(url_for('home'))
        else:
            error = "用户名或者密码错误！！！"
        return render_template('login.html',error=error)

    #登陆检验 QAQ 用户名、密码验证
    def valid_login(self,username,password):
        user = User.query.filter(User.nickname==username,User.password_hash==password).first()
        if user:
            return True
        else:
            return False

"""注册类提交是否成功vv"""
class Regist(views.MethodView):
    def __init__(self):
        self.error = None

    def get(self):
        return render_template("regist.html",error=self.error)

    def post(self):
        if request.form.get("password1") != request.form.get("password2"):
            self.error = '两次密码不相同...请仔细检查下亲QAQ'
        else:
            user1 = User(nickname=request.form.get("username"), password_hash=request.form.get("password1"), payPassword=345353, money=0, isAdmin=0)
            db.session.add(user1)
            db.session.commit()
            flash("成功注册...")
            return redirect(url_for("login"))


        return render_template("regist.html",error=self.error)


"""个人中心"""
class Panel(views.MethodView):
     decorators = {
         'get':[login_required],
     }
     def get(self):
         pass