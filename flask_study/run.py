from .Application import create_app
from .Application.model import User
def main():
    app = create_app()
    app.run('127.0.0.1',8000)

#方式1 装饰器绑定路由
#实现源码 内部调用 add_url_rule

if __name__ == "__main__":
    main()