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
import re

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


    def get_info_by_pages(self):
        pass


    @staticmethod
    def get_job_info(s_url, page, headers):
        url = f"{s_url}{page}"
        res = requests.get(url, headers=headers)
        bs_html = BeautifulSoup(res.content, "html.parser")
        divs = bs_html.find_all("div", {
            "class": "joblist-box__item clearfix"
        })
        for div in divs:
            job_name = div.find("span", class_='iteminfo__line1__jobname__name').text
            company_name = div.find("span", class_='iteminfo__line1__compname__name').text
            info_li_list = div.find_all("li", class_='iteminfo__line2__jobdesc__demand__item')
            comp_add = info_li_list[0].text
            job_exp = info_li_list[1].text
            job_edu = info_li_list[2].text
            job_content = ""
            content_list = div.find_all("div", class_='iteminfo__line3__welfare__item')
            for con in content_list:
                job_content += f"{con.text};"

            salary_info = div.find("p", class_='iteminfo__line2__jobdesc__salary').text.strip().split("-")
            salary_min = re.findall(r'\d+\.?\d*', salary_info[0])[0]
            salary_max = re.findall(r'\d+\.?\d*', salary_info[1])[0]
            salary_unit = re.findall(r'\D$', salary_info[0])[0]
            if salary_unit == "万":
                num = 10000
            else:
                num = 1000
            salary_min = float(salary_min) * num
            salary_max = float(salary_max) * num

            print(job_name)
            print(company_name)
            print(comp_add)
            print(job_edu)
            print(job_exp)
            print(job_content)
            print(salary_min)
            print(salary_max)
            break

    def save_2_db(self, data):
        """数据保存到mysql数据库"""
        sql_text = f"""
            insert into tb_data (data_post,data_company,data_address,data_salary_min,
            data_salary_max,data_dateT,data_edu,data_exper,data_content) 
            values("测试职位","hanayo_company","下北泽",2000,5000,2023-07-07,"本科","3年","详细信息")
        """
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
    # my_spider.get_total_page()
    my_spider.get_headers()

    my_spider.get_job_info("https://sou.zhaopin.com/?jl=538&kw=python&p=", 2, my_spider.headers)
