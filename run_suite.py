import unittest
import time
from case.code_login_order import CodeLoginOrder
from tools.HTMLTestRunner import HTMLTestRunner
suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(CodeLoginOrder))
# with open("report/login{}.html".format(time.strftime('%Y%m%d_%H%M%S')), "wb", ) as f:
with open("report/login.html", "wb") as f:

    runner = HTMLTestRunner(stream=f)
# unittest.TextTestRunner().run(suite)
    runner.run(suite)

