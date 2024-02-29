import uuid
import time


def generate_order_id():
    timestamp = int(time.time() * 1000)  # 获取当前时间戳（毫秒级）
    order_id = f"{timestamp}{uuid.uuid4().hex[:8]}"  # 根据时间戳和随机数生成订单编号
    return order_id
