import logging

from sqlalchemy.exc import OperationalError

from wxcloudrun import db
from wxcloudrun.model import Service_order

# 初始化日志
logger = logging.getLogger('log')


def query_service_orderbyid(id):
    """
    根据ID查询service_order实体
    :param id: service_order的ID
    :return: service_order实体
    """
    try:
        return Service_order.query.filter(Service_order.id == id).first()
    except OperationalError as e:
        logger.info("query_service_orderbyid errorMsg= {} ".format(e))
        return None


def delete_service_orderbyid(id):
    """
    根据ID删除service_order实体
    :param id: service_order的ID
    """
    try:
        service_order = service_orders.query.get(id)
        if service_order is None:
            return
        db.session.delete(service_order)
        db.session.commit()
    except OperationalError as e:
        logger.info("delete_service_orderbyid errorMsg= {} ".format(e))




def insert_service_order(s):
    """
    插入一个service_order实体
    :param service_order: service_orders实体
    """
    try:
        db.session.add(s)
        db.session.commit()
    except OperationalError as e:
        logger.info("insert_service_order errorMsg= {} ".format(e))


def update_service_orderbyid(service_order):
    """
    根据ID更新service_order的值
    :param service_order实体
    """
    try:
        service_order = query_service_orderbyid(service_order.id)
        if service_order is None:
            return
        db.session.flush()
        db.session.commit()
    except OperationalError as e:
        logger.info("update_service_orderbyid errorMsg= {} ".format(e))
