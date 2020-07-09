"""
接口实现
"""


# 静态方法封装一些单独存在的工具（在类中封装避免self干扰）
from app import BASE_URL


class CodeLoginApi(object):

    @staticmethod
    def verify_code(session):
        response = session.get(BASE_URL + "/index.php?m=Home&c=User&a=verify")
        return response

    @staticmethod
    def login(session, username, password, code):
        data = {"username": username, "password": password, "verify_code": code}
        response1 = session.post(BASE_URL + "/index.php?m=Home&c=User&a=do_login", data=data)
        return response1

    @staticmethod
    def order(session):
        response2 = session.get(BASE_URL + "/Home/Order/order_list.html")
        return response2
