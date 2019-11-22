"""
flask 配置文件 QAQ
"""

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456789@localhost:3306/flask_db'
# 'mysql+pymysql://用户名称:密码@localhost:端口/数据库名称'
SQLALCHEMY_TRACK_MODIFICATIONS = True
