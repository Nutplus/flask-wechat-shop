from config import initial

url_banner = initial.Server_ImageUrl + "/home/"
url_categories = initial.Server_ImageUrl + "/categories/"

banner = [
    'https://prod-0g03xycyc61e7df3-1324540232.tcloudbaseapp.com/home/banner1.png?sign=f2ff204a9e62f9572c58e4edd8efd487&t=1709219306',
    'https://prod-0g03xycyc61e7df3-1324540232.tcloudbaseapp.com/home/banner2.png?sign=acc4eaf63c72c4aad48cecd7254bc75a&t=1709219367',
    'https://prod-0g03xycyc61e7df3-1324540232.tcloudbaseapp.com/home/banner3.png?sign=d156d7225318a10ded9f49e7b9f21b9d&t=1709219395'

]

# banner元素直接完整URL，
# 图片大小 高480 宽250

categories = [
    {"id": 1, "name": "分类1", "icon": url_categories + "1.png"},
    {"id": 2, "name": "分类2", "icon": url_categories + "2.png"},
    {"id": 3, "name": "分类3", "icon": url_categories + "3.png"},
    {"id": 4, "name": "分类4", "icon": url_categories + "4.png"},
    {"id": 5, "name": "分类3", "icon": url_categories + "5.png"},
    {"id": 6, "name": "分类3", "icon": url_categories + "6.png"},
    {"id": 7, "name": "分类3", "icon": url_categories + "7.png"},
    {"id": 8, "name": "分类3", "icon": url_categories + "8.png"},
    {"id": 9, "name": "分类3", "icon": url_categories + "9.png"},
    {"id": 10, "name": "分类3", "icon": url_categories + "10.png"}
]
initial_data = {
    'goodsDynamic': [
        {'avatarUrl': '/static/images/categorie/1.png', 'nick': 'A', 'goodsName': 'B'},
        {'avatarUrl': '/static/images/categorie/1.png', 'nick': 'B', 'goodsName': 'A'},
    ],
    'show_buy_dynamic': '1'
}
