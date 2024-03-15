import uuid
import time
from datetime import datetime, timedelta, timezone


def generate_order_id():
    timestamp = int(time.time() * 1000)  # 获取当前时间戳（毫秒级）
    order_id = f"{timestamp}{uuid.uuid4().hex[:8]}"  # 根据时间戳和随机数生成订单编号
    return str(order_id)

def now_time():
    # 服务器时间（假设是UTC时间）
    server_time_utc = datetime.utcnow()

    # 定义你所在的时区
    your_timezone_offset = timedelta(hours=8)  # 东八区时差

    # 创建你所在时区的时区对象
    your_timezone = timezone(your_timezone_offset)

    # 将服务器时间转换为你所在时区的时间
    your_local_time = server_time_utc.replace(tzinfo=timezone.utc).astimezone(your_timezone)

    return your_local_time

# 定义一个函数来格式化时间
def format_time(time_obj):

    formatted_time = time_obj.strftime('%Y-%m-%d %H:%M:%S')
    return formatted_time
