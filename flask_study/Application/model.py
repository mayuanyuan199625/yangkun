from Application import db
from passlib.apps import custom_app_context as pwd_context
from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)


class User(db.Model):
    """用户"""
    __tablename__ = 'users'
    __table_args__ = {'mysql_engine': 'InnoDB'}  # 支持事务操作和外键
    id = db.Column(db.Integer, doc='手机号码', primary_key=True,autoincrement=True)
    nickname = db.Column(db.String(20), doc='昵称', default='Wanted User', nullable=False, unique=True)
    password_hash = db.Column(db.String(128), doc='密码', nullable=False)
    payPassword = db.Column(db.String(32), doc='支付密码', nullable=False)
    money = db.Column(db.Float, doc='账户余额', default=50, nullable=False)
    description = db.Column(db.String(50), doc='个性签名', default='这个人很懒，什么也没留下', nullable=False)
    isAdmin = db.Column(db.Boolean, doc='是否管理员', default=False)
    # orders = db.relationship('Order', backref='users', cascade='all', lazy='dynamic')
    # coupons = db.relationship('Coupon', backref='users', cascade='all', lazy='dynamic')
    # favorites = db.relationship('Favorite', backref='users', cascade='all', lazy='dynamic')
    # comments = db.relationship('Comment', backref='users', cascade='all', lazy='dynamic')

# user1 = User(id = 6, nickname= "吴彦", password_hash = 343838, payPassword = 345353, money = 0, isAdmin = 0)
# db.session.add(user1)
# db.session.commit()
# db.create_all()