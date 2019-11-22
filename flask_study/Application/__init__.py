from flask import *
from flask_sqlalchemy import SQLAlchemy


# instance_relative_config 是否自定义配置文件
db = SQLAlchemy()
def create_app():
    app = Flask(__name__,template_folder='./templates',instance_relative_config=False)
    app.config.from_object('config')
    app.config['SECRET_KEY'] = '123456'
    db.init_app(app)
    with app.test_request_context():
        db.create_all()
    handle_route(app)
    return app

#数据库连接
# db = SQLAlchemy(create_app(),use_native_unicode='utf8')
"""
第一个参数：函数对应的url规则，满足条件和app.route()的第一个参数一样，必须以'/'开始
endpoint：站点，就是在使用url_for()进行反转的时候，这个里面传入的第一个参数就是这个endpoint对应的值。这个值也可以不指定，那么默认就会使用函数的名字作为endpoint的值
view_func：对应的函数，即这个url对应的是哪一个函数，注意，这里函数只需要写函数名字，不要加括号，加括号表示将函数的返回值传给了view_func参数了。程序就会直接报错。

"""


#注册路由方法 QAQ
def handle_route(app):
    from Application.views import ListView,LoginView,Regist
    #主页
    app.add_url_rule('/', view_func=ListView.as_view('index'))
    #登陆
    app.add_url_rule('/login',view_func=LoginView.as_view('login'))
    #注册路由
    app.add_url_rule('/regist',view_func=Regist.as_view('regist'))

