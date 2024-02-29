from pydantic import BaseModel
from datetime import datetime
from flask import render_template, request, jsonify, send_from_directory
from run import app
from wxcloudrun.dao import delete_counterbyid, query_counterbyid, insert_counter, update_counterbyid
from wxcloudrun.model import Counters
from wxcloudrun.response import make_succ_empty_response, make_succ_response, make_err_response
from dataconfig import goods, home, initial
from methods import order


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


@app.route("/service_order/", methods=["POST"])
def service_order():
    order_data = OrderData(**request.json)
    buy_number = order_data.buy_number
    desc = order_data.desc
    goods_price = order_data.goods_price
    goods_title = order_data.goods_title
    notes = order_data.notes
    phone_number = order_data.phone_number
    tag = order_data.tag
    state = order_data.state
    open_id = order_data.open_id
    order_number = order.generate_order_id()
    return jsonify({
        "order_number": order_number,
        "buy_number": buy_number,
        "desc": desc,
        "goods_price": goods_price,
        "goods_title": goods_title,
        "notes": notes,
        "phone_number": phone_number,
        "tag": tag
    })


class Openid(BaseModel):
    openid: str


@app.route("/op_id/", methods=["POST"])
def receive_openid():
    openid_data = Openid(**request.json)
    code = openid_data.openid
    url = 'https://api.weixin.qq.com/sns/jscode2session'
    params = {
        'appid': 'wx549c0fa1cd5e49a7',
        'secret': '822e1e21cb7dc1cfeaa3eb3bfdfe9547',
        'js_code': code,
        'grant_type': 'authorization_code'
    }
    response = requests.get(url, params=params)
    data = response.json()
    if data is None:
        data = "None"
    openid = data.get('openid')
    session_key = data.get('session_key')
    print(data, code)
    v = [openid, session_key, code]
    try:
        unionid = data.get('unionid')
        v.append(unionid)
    except:
        pass
    return jsonify({"message": "Received openid successfully", "openid": openid})


@app.route("/coupon", methods=["POST"])
def receive_op():
    return "True"


# @app.route("/get_image/<path:name>", methods=["GET"])
# def get_image(name):
#     image_filename = f"{name}"
#     image_path = os.path.join(current_dir, "images", image_filename)
#     return send_from_directory(os.path.join(current_dir, "images"), image_filename)


@app.route("/goods_list", methods=["GET"])
def get_product():
    return_goods = goods.goods
    modified_goods = []
    for i in return_goods:
        modified_good = i.copy()
        modified_good["pic_url"] = initial.Server_ImageUrl + '/product/' + i["pic_url"]
        modified_goods.append(modified_good)
    return jsonify(modified_goods)


@app.route("/get_banner", methods=["GET"])
def get_banner():
    return jsonify(home.banner)


@app.route("/get_category", methods=["GET"])
def get_category():
    return jsonify(home.categories)


@app.route("/home_initial", methods=["GET"])
def home_initial():
    return jsonify(home.initial_data)



























@app.route('/')
def index():
    """
    :return: 返回index页面
    """
    return render_template('index.html')


@app.route('/api/count', methods=['POST'])
def count():
    """
    :return:计数结果/清除结果
    """

    # 获取请求体参数
    params = request.get_json()

    # 检查action参数
    if 'action' not in params:
        return make_err_response('缺少action参数')

    # 按照不同的action的值，进行不同的操作
    action = params['action']

    # 执行自增操作
    if action == 'inc':
        counter = query_counterbyid(1)
        if counter is None:
            counter = Counters()
            counter.id = 1
            counter.count = 1
            counter.created_at = datetime.now()
            counter.updated_at = datetime.now()
            insert_counter(counter)
        else:
            counter.id = 1
            counter.count += 1
            counter.updated_at = datetime.now()
            update_counterbyid(counter)
        return make_succ_response(counter.count)

    # 执行清0操作
    elif action == 'clear':
        delete_counterbyid(1)
        return make_succ_empty_response()

    # action参数错误
    else:
        return make_err_response('action参数错误')


@app.route('/api/count', methods=['GET'])
def get_count():
    """
    :return: 计数的值
    """
    counter = Counters.query.filter(Counters.id == 1).first()
    return make_succ_response(0) if counter is None else make_succ_response(counter.count)
