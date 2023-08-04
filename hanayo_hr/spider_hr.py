"""
spider_hr - 获取职位信息的爬虫程序

Author: kayotin
Date 2023/8/4
"""

from config import COOKIE
import requests

city_dict = {
    "上海": 538,
    "北京": 530
}


class SpiderHR:

    def __init__(self, key_word, city_cn):
        """
        初始化爬虫程序
        :param key_word: 搜索关键字，
        :param city_cn: 城市中文名，比如北京或上海
        """
        self.cookie = COOKIE
        city_code = city_dict[city_cn]
        self.default_page = 1
        self.s_url = f"https://sou.zhaopin.com/?jl={city_code}&kw={key_word}&p={self.default_page}"
        self.total_page = 0

    def get_total_page(self):
        pass
