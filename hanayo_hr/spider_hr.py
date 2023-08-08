"""
spider_hr - 获取职位信息的爬虫程序

Author: kayotin
Date 2023/8/4
"""

from config import COOKIE, user_agent, DATABASE, USERNAME, PASSWORD
import requests
import random
from bs4 import BeautifulSoup
import pymysql

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
        self.city_cn = city_cn
        self.city_code = city_dict[city_cn]
        self.default_page = 1
        self.key_word = key_word
        self.s_url = f"https://sou.zhaopin.com/?jl={self.city_code}&kw={self.key_word}&p="
        self.total_page = 0
        self.headers = {
        }
        self.db = pymysql.connect(host="192.168.32.11", port=3306,
                                  user=USERNAME, password=PASSWORD,
                                  database=DATABASE, charset="utf8mb4")

    def get_headers(self):
        num = random.randint(0, len(user_agent) - 1)
        self.headers = {
            "User-Agent": user_agent[num],
            "Cookie": COOKIE
        }

    def get_pages(self, page_num):
        url = f"{self.s_url}{page_num}"
        res = requests.get(url, headers=self.headers)
        bs_html = BeautifulSoup(res.content, "html.parser")
        items_page_spans = bs_html.find_all("span", {
            "class": "soupager__index"
        })
        return len(items_page_spans)

    def get_total_page(self):
        print(f"正在获取{self.city_cn}的关键字：{self.key_word}的总页数-->", end="")
        self.get_headers()
        page_num = 100
        while True:
            len_spans = self.get_pages(page_num)
            if not len_spans:
                page_num = page_num // 2
            else:
                break
        page_num += 5
        while True:
            len_spans = self.get_pages(page_num)
            if len_spans:
                page_num += 5
            else:
                break
        page_num -= 1
        while True:
            len_spans = self.get_pages(page_num)
            if not len_spans:
                page_num -= 1
            else:
                break
        self.total_page = page_num
        print(f"页数获取完毕，{self.city_cn}的{self.key_word}岗位共有{page_num}页。")

    @staticmethod
    def get_job_info(s_url, page, headers):
        url = f"{s_url}{page}"
        res = requests.get(url, headers=headers)
        bs_html = BeautifulSoup(res.content, "html.parser")
        divs = bs_html.find_all("div", {
            "class": "joblist-box__item clearfix"
        })
        for div in divs:
            pass

    def save_2_db(self, data):
        """数据保存到mysql数据库"""
        sql_text = f""
        try:
            # 获取游标对象
            with self.db.cursor() as cursor:
                # 通过游标对象对数据库服务器发出sql语句
                affected_rows = cursor.execute(sql_text)
                if affected_rows == 1:
                    print("新增部门成功")
            # 提交
            self.db.commit()
        except pymysql.MySQLError as err:
            # 回滚
            self.db.rollback()
            print(type(err), err)
        finally:
            # 5.关闭连接
            self.db.close()


if __name__ == '__main__':
    my_spider = SpiderHR("数据分析师", "上海")
    my_spider.get_total_page()
