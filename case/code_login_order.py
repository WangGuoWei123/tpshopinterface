"""
测试用例
"""
import json
import logging
import unittest

import requests
from parameterized import parameterized

from api.code_login_api import CodeLoginApi
from app import PRO_PATH, config_log


def read_json():
    list_data = list()
    # 文件要用绝对路径，不然在套件中执行的时候会报错因为文件在run_suite执行的时候切换了路径
    with open(PRO_PATH + "/data/user_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        for dat in data.values():
            list_data.append(
                (dat.get("username"), dat.get("password"), dat.get("verify_code"), dat.get("status"),
                 dat.get("msg")))

    return list_data


class CodeLoginOrder(unittest.TestCase):

    def setUp(self) -> None:
        self.session = requests.Session()

    def tearDown(self) -> None:
        self.session.close()

    def test_code(self):
        msg = "image"
        response = CodeLoginApi.verify_code(self.session)
        rs_data = response.headers.get('Content-Type')
        self.assertIn(msg, rs_data)

    @parameterized.expand(read_json())
    def test_login(self, username, password, code, status, msg):
        msg = msg
        CodeLoginApi.verify_code(self.session)
        response1 = CodeLoginApi.login(self.session, username, password, code)
        self.assertIn(msg, response1.json().get("msg"))
        config_log()
        logging.warning("hello")

    def test_order(self):
        msg = "我的订单"
        CodeLoginApi.verify_code(self.session)
        CodeLoginApi.login(self.session, "13811176151", "123456", "8888")
        response2 = CodeLoginApi.order(self.session)
        self.assertIn(msg, response2.text)


if __name__ == '__main__':
    unittest.main()
