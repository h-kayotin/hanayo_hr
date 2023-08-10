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
import datetime
from concurrent.futures import ThreadPoolExecutor
from threading import RLock
import os

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
        self.datetime = datetime.datetime.today()
        root_path = os.path.abspath(os.path.dirname(__file__))
        self.log_path = os.path.join(root_path, "logs")
        if not os.path.exists(self.log_path):
            os.makedirs(self.log_path)
        self.count = 0
        self.lock = RLock()

    def get_headers(self):
        """
        生成请求的headers信息
        :return:
        """
        num = random.randint(0, len(user_agent) - 1)
        self.headers = {
            "User-Agent": user_agent[num],
            "Cookie": COOKIE
        }

    def get_pages(self, page_num):
        """获取底部页码的span，用以判断这一页有没有内容"""
        url = f"{self.s_url}{page_num}"
        res = requests.get(url, headers=self.headers)
        bs_html = BeautifulSoup(res.content, "html.parser")
        items_page_spans = bs_html.find_all("span", {
            "class": "soupager__index"
        })
        return len(items_page_spans)

    def get_info_by_pages(self):
        """多线程的获取每一页的数据"""
        with ThreadPoolExecutor(max_workers=32) as pool:
            while True:
                self.total_page += 1
                if self.get_pages(self.total_page):
                    pool.submit(self.get_job_info, page=self.total_page)
                else:
                    break

    @staticmethod
    def trans_salary(salary_str):
        """
        薪资格式转化
        :param salary_str:薪资字符串比如1.5万
        :return: 返回数字，例如15000
        """
        try:
            salary = re.findall(r'\d+\.?\d*', salary_str)[0]
            is_10_k = re.search(r'万', salary_str)
            is_k = re.search(r'千', salary_str)
            if is_10_k:
                # salary_unit = "万"
                num = 10000
            elif is_k:
                # salary_unit = "千"
                num = 1000
            else:
                # salary_unit = "日"
                num = 1
            salary_num = float(salary) * num
        except IndexError:
            salary_num = 0

        return salary_num

    def get_job_info(self, page):
        """
        根据页码循环获取一页中的所有职位数据
        :param page: 页码
        :return: 无
        """
        print(f"正在读取第{page}页的数据-->", end="")
        url = f"{self.s_url}{page}"
        res = requests.get(url, headers=self.headers)
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

            salary_info = div.find("p", class_='iteminfo__line2__jobdesc__salary').text.split("·")[0].split("-")
            try:
                salary_min = SpiderHR.trans_salary(salary_info[0].strip())
                salary_max = SpiderHR.trans_salary(salary_info[1].strip())
            except IndexError:
                salary_min = 0
                salary_max = 0

            data = {
                "data_post": job_name, "data_company": company_name, "data_address": comp_add,
                "data_salary_min": salary_min, "data_salary_max": salary_max,
                "data_edu": job_edu, "data_exp": job_exp, "data_content": job_content
            }
            self.lock.acquire()
            self.save_2_db(data)
            self.lock.release()
        print(f"第{page}页数据读取完毕。\n", end="")

    def save_2_db(self, data):
        """数据保存到mysql数据库"""
        sql_text = f"""
            insert into tb_data (data_post,data_company,data_address,data_salary_min,
            data_salary_max,data_date,data_edu,data_exp,data_content) 
            values("{data['data_post']}", "{data['data_company']}", "{data['data_address']}",
            "{data['data_salary_min']}", "{data['data_salary_max']}" ,"{self.datetime}",
            "{data['data_edu']}","{data['data_exp']}","{data['data_content']}")
        """
        try:
            # 获取游标对象
            with self.db.cursor() as cursor:
                # 通过游标对象对数据库服务器发出sql语句
                affected_rows = cursor.execute(sql_text)
                if affected_rows == 1:
                    self.count += 1
                if self.count % 100 == 0:
                    print(f"已保存{self.count}条数据-->", end="")
                    # print("插入数据成功")
            self.db.commit()
        except pymysql.MySQLError as err:
            # 如果出现报错就回滚数据
            self.db.rollback()
            err_log = f"{type(err)}，错误信息：{err}\n"
            print(err_log)
            self.save_log(False, err_log)

    def clo_db(self):
        suc_log = f"数据读取完毕，共保存了{self.count}条数据。\n"
        print(suc_log)
        self.save_log(True, suc_log)
        self.db.close()

    def save_log(self, log_type, log_txt):
        """
        保存日志
        :param log_type: True表示成功日志，False表示错误日志
        :param log_txt: 日志文本
        :return:
        """
        if log_type:
            log_name = "success.log"
        else:
            log_name = "error.log"
        with open(f"{self.log_path}/{log_name}", "a", encoding="utf-8") as file:
            file.write(log_txt)

    def do_work(self):
        log_txt = f"开始读取城市：{self.city_cn}，关键字：{self.key_word}的数据\n"
        print(log_txt, end="")
        self.save_log(True, log_txt)
        self.get_headers()
        self.get_info_by_pages()
        self.clo_db()


if __name__ == '__main__':
    my_spider = SpiderHR("python", "上海")
    my_spider.do_work()



