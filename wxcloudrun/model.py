from datetime import datetime

from wxcloudrun import db




class Service_order(db.Model):
    # 设置结构体表格名称
    __tablename__ = 'Service_order'

    # 设定结构体对应表格的字段
    id = db.Column(db.Integer, primary_key=True)
    order_number = db.Column(db.String, default=1)
    buy_number = db.Column(db.Integer, default=1)
    goods_price = db.Column(db.Float, default=1)
    goods_title = db.Column(db.String, unique=True,nullable=False)
    notes = db.Column(db.String, unique=True,nullable=False)
    phone_number = db.Column(db.Integer, default=1)
    tag = db.Column(db.String, unique=True,nullable=False)
    state =  db.Column(db.String, unique=True,nullable=False)
    open_id = db.Column(db.Integer, default=1)
    goods_url =  db.Column(db.String, unique=True,nullable=False)

    created_at = db.Column( db.TIMESTAMP, nullable=False, default=datetime.now())
    updated_at = db.Column( db.TIMESTAMP, nullable=False, default=datetime.now())

class op(db.Model):
    __tablename__ = 'op'
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String,primary_key=True)
    login_time = db.Column( db.TIMESTAMP, nullable=False, default=datetime.now())

class user(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    user_name = db.Column(db.String,primary_key=True)
    open_id = db.Column(db.String,primary_key=True)
    creat_time = db.Column( db.TIMESTAMP, nullable=False, default=datetime.now())
    login_time = db.Column( db.TIMESTAMP, nullable=False, default=datetime.now())