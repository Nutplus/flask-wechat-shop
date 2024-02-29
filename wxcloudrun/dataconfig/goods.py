from config import initial

# 使用格式化字符串构建HTML代码
# html_code = '''
# <div style="position: relative; width: 100%; height: 100vh;">
#   <text style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); font-size: 24px; color: white;">{}</text>
#   < img src="{}" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;" />
# </div>
# '''
''''
"goodsAddition": [
    {
        "id": 1,
        "name": "颜色",
        "items": [
            {"id": 1, "name": "红色", "active": False},
            {"id": 2, "name": "蓝色", "active": False},
            {"id": 3, "name": "绿色", "active": False}
        ]
    },
    {
        "id": 2,
        "name": "尺码",
        "items": [
            {"id": 1, "name": "S", "active": False},
            {"id": 2, "name": "M", "active": False},
            {"id": 3, "name": "L", "active": False}
        ]
    }
]
'''''

url = initial.Server_ImageUrl + '/product_details/'

# 主页商品图大小width: 329# height: 260
goods = [
    {
        "id": 1,
        "name": '小A',
        "pic_url": '商品1.png',
        "minPrice": 32.99,
        "originalPrice": 60,
        "characteristic": '特点1',

        'goods_info': {
            "banner": [
                {"img_id": 1, "url": url + "商品1/banner1.JPG"},
                {"img_id": 2, "url": url + "商品1/banner2.png"},
                {"img_id": 3, "url": url + "商品1/banner3.jpg"}
            ],
            "goods_title": "小A",
            "goods_introduce_image": url + "商品1/detail.png",  # 底部预留一部分白边 防止立即购买按钮遮挡
            "goods_introduce_text": '',  # 当为""不会显示任何内容
            "shopType": 'service',  # 商品类型 用于跳转页面以及是否可以购买 service服务页面 just_show只能用于展示不能购买 item作为一般货物购买(item未开发）
            "tag": "小A",
            "desc": "特惠价",
            "quantity": 10,  # 存货 暂时没有逻辑作用用 只用于展示
            "min_buy": 4,
            "max_buy": 16,
            "min_buy_for_step": 4,  # 点加号减号改变的数量
            "initial_number": 4,  # 一点开页面就显示的购买数量 后面js中用户操作会对进行修改  buyNumber
            "bar_tip_show": '请注意您的订单信息完整，我们会尽快联系您',  # 当为""不会显示任何内容
            "minHour": 8,
            "maxHour": 19,  # 设置服务可选时间范围
            "maxDate": 5  # 当前日期的X个月后
        },

    },
    {
        "id": 2,
        "name": '商品2',
        "pic_url": '商品2.png',
        "minPrice": 50,
        "originalPrice": 60,
        "characteristic": '特点1',

        'goods_info': {
            "banner": [
                {"img_id": 1, "url": url + "商品1/banner1.JPG"},
                {"img_id": 2, "url": url + "商品1/banner2.png"},
                {"img_id": 3, "url": url + "商品1/banner3.jpg"}
            ],
            "goods_price": 199.99,
            "Need_PAY": "NO",
            "goods_title": "永诺YN85mm F1.8S（金属外壳版）索尼E口全画幅定焦自动对焦镜头",
            "goods_introduce_image": url + "商品1/detail.png",
            "goods_introduce_text": '',
            "shopType": 'service',
            "tag": "小A",
            "desc": "特惠价",
            "quantity": 10,
            "min_buy": 4,
            "max_buy": 16,
            "min_buy_for_step": 4,
            "initial_number": 4,
            "bar_tip_show": '请注意您的订单信息完整，我们会尽快联系您',
            "minHour": 8,
            "maxHour": 19
        }

    },
    {
        "id": 3,
        "name": '商品3',
        "pic_url": '商品2.png',
        "minPrice": 50,
        "originalPrice": 60,
        "characteristic": '特点1',

        'goods_info': {
            "banner": [
                {"img_id": 1, "url": url + "商品1/banner1.JPG"},
                {"img_id": 2, "url": url + "商品1/banner2.png"},
                {"img_id": 3, "url": url + "商品1/banner3.jpg"}
            ],
            "goods_price": 199.99,
            "goods_title": "永诺YN85mm F1.8S（金属外壳版）索尼E口全画幅定焦自动对焦镜头",
            "goods_introduce_image": url + "商品1/detail.png",
            "goods_introduce_text": '',
            "shopType": 'service',
            "tag": "小A",
            "desc": "特惠价",
            "quantity": 10,
            "min_buy": 4,
            "max_buy": 16,
            "min_buy_for_step": 4,
            "initial_number": 4,
            "bar_tip_show": '请注意您的订单信息完整，我们会尽快联系您',
            "minHour": 8,
            "maxHour": 19
        }
    },
    {
        "id": 4,
        "name": '商品4',
        "pic_url": '商品2.png',
        "minPrice": 30,
        "originalPrice": 40,
        "characteristic": '特点2',

        'goods_info': {
            "banner": [
                {"img_id": 1, "url": url + "商品1/banner1.JPG"},
                {"img_id": 2, "url": url + "商品1/banner2.png"},
                {"img_id": 3, "url": url + "商品1/banner3.jpg"}
            ],
            "goods_price": 199.99,
            "goods_title": "永诺YN85mm F1.8S（金属外壳版）索尼E口全画幅定焦自动对焦镜头",
            "goods_introduce_image": url + "商品1/detail.png",
            "goods_introduce_text": '',
            "shopType": 'service',
            "tag": "小A",
            "desc": "特惠价",
            "quantity": 10,
            "min_buy": 4,
            "max_buy": 16,
            "min_buy_for_step": 4,
            "initial_number": 4,
            "bar_tip_show": '请注意您的订单信息完整，我们会尽快联系您',
            "minHour": 8,
            "maxHour": 19
        }
    }
]
