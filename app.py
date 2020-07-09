import os
import logging
import logging.handlers

# 项目url

BASE_URL = "http://localhost"
# 当前项目的绝对路径
PRO_PATH = os.path.dirname(os.path.abspath(__file__))
# print(PRO_PATH)

# 当前文件的绝对路径
# print(os.path.abspath(__file__))
"""
配置文件
"""
# 导包


# 该语句返回当前文件的上一层文件夹的绝对路径
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(BASE_DIR)


def config_log():
    """日志配置方法"""

    # 实例化日志器
    logger = logging.getLogger()

    # 实例化处理器
    sh = logging.StreamHandler()  # 控制台
    th = logging.handlers.TimedRotatingFileHandler(filename=BASE_DIR + '/log/info.log',
                                                   when='H',
                                                   interval=5,
                                                   backupCount=3)  # 文件
    # 实例化格式器
    fmt = "%(asctime)s %(levelname)s [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"
    formatter = logging.Formatter(fmt)

    # 将格式器添加给处理器
    sh.setFormatter(formatter)
    th.setFormatter(formatter)

    # 将处理器添加给日志器
    logger.addHandler(sh)
    logger.addHandler(th)
