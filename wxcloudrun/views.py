from pydantic import BaseModel,parse_obj_as
from datetime import datetime
from flask import render_template, request, jsonify, send_from_directory
from run import app
from wxcloudrun.model import Service_order
from wxcloudrun.model import op
from wxcloudrun.model import user
from wxcloudrun.response import make_succ_empty_response, make_succ_response, make_err_response

from wxcloudrun import db

from wxcloudrun.dataconfig import goods, home, initial
from wxcloudrun.methods import utils,order_Service,nick_name



@app.route('/user_orders', methods=["POST"])
def user_orders():
    data = request.json
    result = Service_order.query.filter_by(open_id=data['open_id']).all() #通过密码查询
    if result:
        orders_list = []
        for order in result:
            order_dict = {
                "id": order.id,
                "order_number": order.order_number,
                "buy_number": order.buy_number,
                "goods_price": order.goods_price,
                "goods_title": order.goods_title,
                "notes": order.notes,
                "phone_number": order.phone_number,
                "tag": order.tag,
                "state": order.state,
                "created_at": utils.format_time(order.created_at),
                "updated_at": utils.format_time(order.updated_at),
                'goods_url':order.goods_url
            }
            orders_list.append(order_dict) 
        return jsonify(orders_list)
    else:
        return jsonify({"error": "User not found by open_id"})

#删除订单
@app.route("/delete_order/<int:order_id>", methods=["DELETE"])
def delete_order(order_id):
    order = Service_order.query.get(order_id)
    if order:
        db.session.delete(order)
        db.session.commit()
        return jsonify({"message": "Order deleted successfully"})
    else:
        return jsonify({"error": "Order not found"}), 404


#设置订单状态
@app.route("/update_order", methods=["PUT"])
def update_order():
    data = request.json
    order = Service_order.query.get(data['order_id'])
    if order:
        state = data['state']
        if state == '订单已取消':
            order.state = state
            order.updated_at = utils.now_time()
            db.session.commit()
            return jsonify({"message": "Order updated successfully state => cancel"})
        elif state == '订单已完成':
            order.state = state
            order.updated_at = utils.now_time()
            db.session.commit()
            return jsonify({"message": "Order updated successfully state => finish"})
    else:
        return jsonify({"error": "Order not found"}), 404



@app.route("/all_orders", methods=["GET"])
def all_orders():
    orders = Service_order.query.order_by(Service_order.id.desc()).all()
    
    orders_list = []
    for order in orders:
        order_dict = {
            "id": order.id,
            "order_number": order.order_number,
            "buy_number": order.buy_number,
            "goods_price": order.goods_price,
            "goods_title": order.goods_title,
            "notes": order.notes,
            "phone_number": order.phone_number,
            "tag": order.tag,
            "state": order.state,
            "created_at": utils.format_time(order.created_at),
            "updated_at": utils.format_time(order.updated_at)
        }
        orders_list.append(order_dict)
    
    return jsonify(orders_list)









# 创建一个 Pydantic 模型来定义请求体的结构
class OrderData(BaseModel):
    buy_number: int
    desc: str
    goods_price: float
    goods_title: str
    notes: str
    phone_number: str
    tag: str
    state: str
    open_id: str
    pic_url:str


#添加订单——服务类型的订单
@app.route("/service_order", methods=["POST"])
def service_order():
    order_data = parse_obj_as(OrderData, request.json)
    
    order_number = utils.generate_order_id()
    
    time = utils.now_time()


    s = Service_order(
        buy_number=order_data.buy_number,
        goods_price=order_data.goods_price,
        goods_title=order_data.goods_title,
        notes=order_data.notes,
        phone_number=order_data.phone_number,
        tag=order_data.tag,
        state=order_data.state,
        order_number=order_number,
        created_at=time,
        updated_at=time,
        open_id=order_data.open_id,
        goods_url=order_data.pic_url
    )
    
    order_Service.insert_service_order(s)
    
    return jsonify({
        "order_number": order_number,
        "buy_number": order_data.buy_number,
        "desc": order_data.desc,
        "goods_price": order_data.goods_price,
        "goods_title": order_data.goods_title,
        "notes": order_data.notes,
        "phone_number": order_data.phone_number,
        "tag": order_data.tag,
        "state": order_data.state,
        'order_number':order_number,
        'open_id':order_data.open_id,
        'goods_url':order_data.pic_url

    })


# class Openid(BaseModel):
#     openid: str


# @app.route("/op_id/", methods=["POST"])
# def receive_openid():
#     openid_data = Openid(**request.json)
#     code = openid_data.openid
#     url = 'https://api.weixin.qq.com/sns/jscode2session'
#     params = {
#         'appid': 'wx549c0fa1cd5e49a7',
#         'secret': '822e1e21cb7dc1cfeaa3eb3bfdfe9547',
#         'js_code': code,
#         'grant_type': 'authorization_code'
#     }
#     response = requests.get(url, params=params)
#     data = response.json()
#     if data is None:
#         data = "None"
#     openid = data.get('openid')
#     session_key = data.get('session_key')
#     print(data, code)
#     v = [openid, session_key, code]
#     try:
#         unionid = data.get('unionid')
#         v.append(unionid)
#     except:
#         pass
#     return jsonify({"message": "Received openid successfully", "openid": openid})

#管理员登录
@app.route("/coupon", methods=["POST"])
def login_op():
    data = request.json
    result = op.query.filter_by(password=data['coupon']).first() #通过密码查询
    if result:
        result.login_time = utils.now_time()
        db.session.commit()
        return "True"
    else:
        return "False"

#获取全部商品
@app.route("/goods_list", methods=["GET"])
def get_product():
    return_goods = goods.goods
    modified_goods = []
    for i in return_goods:
        modified_good = i.copy()
        modified_good["pic_url"] = initial.Server_ImageUrl + '/product/' + i["pic_url"]
        modified_goods.append(modified_good)
    return jsonify(modified_goods)


#获取轮播图
@app.route("/get_banner", methods=["GET"])
def get_banner():
    return jsonify(home.banner)

# #获取 目录
# @app.route("/get_category", methods=["GET"])
# def get_category():
#     return jsonify(home.categories)

#初始化index
@app.route("/home_initial", methods=["GET"])
def home_initial():
    return jsonify(home.initial_data) #目前 返回nick宣传弹幕


#用于登录
@app.route('/wp-login', methods=['GET'])
def wplogin():
    hearders = request.headers
    openid = hearders['X-Wx-Openid']
    try:
        User = user.query.filter_by(open_id=openid).first() #查询是否注册账户
        if User:
            User.login_time = utils.now_time()
            db.session.commit()
            return jsonify({'openid':openid,'user_name':User.user_name})
        else:
            User = user()
            time = utils.now_time()
            User.creat_time = time
            User.login_time = time
            User.open_id = openid

            name = nick_name.get()
            User.user_name = name

            order_Service.insert_service_order(User)
            return jsonify({'openid':openid,'user_name':name})
    except OperationalError as e:         
        logger.info("service_wplogin errorMsg= {} ".format(e))
        return None


@app.route('/')
def index():
    """
    :return: 返回index页面
    """
    return 'successful the Service is runing'


# @app.route('/api/count', methods=['POST'])
# def count():
#     """
#     :return:计数结果/清除结果
#     """

#     # # 获取请求体参数
#     # params = request.get_json()

#     # # 检查action参数
#     # if 'action' not in params:
#     #     return make_err_response('缺少action参数')

#     # # 按照不同的action的值，进行不同的操作
#     # action = params['action']

#     # 执行自增操作
#     # if action == 'inc':
#     counter = query_counterbyid(1)
#     if counter is None:
#         counter = Counters()
#         counter.id = 1
#         counter.count = 1
#         counter.created_at = datetime.now()
#         counter.updated_at = datetime.now()
#         insert_counter(counter)
#     else:
#         counter.id = 1
#         counter.count += 1
#         counter.updated_at = datetime.now()
#         update_counterbyid(counter)
#     return make_succ_response(counter.count)

#     # # 执行清0操作
#     # elif action == 'clear':
#     #     delete_counterbyid(1)
#     #     return make_succ_empty_response()

#     # action参数错误
#     # else:
#     #     return make_err_response('action参数错误')


# # @app.route('/api/count', methods=['GET'])
# # def get_count():
# #     """
# #     :return: 计数的值
# #     """
# #     counter = Counters.query.filter(Counters.id == 1).first()
# #     # return make_succ_response(0) if counter is None else make_succ_response(counter.count)
# #     return "9999999"
