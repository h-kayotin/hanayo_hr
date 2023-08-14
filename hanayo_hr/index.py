"""
index - home页面，网站入口

Author: kayotin
Date 2023/8/10
"""
import time

from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, session
)
from werkzeug.exceptions import abort
import datetime
import math
from hanayo_hr.db import get_db
import pymysql
from hanayo_hr.spider_hr import SpiderHR
import threading
import queue

bp = Blueprint('index', __name__)
date_today = datetime.datetime.today().strftime('%Y-%m-%d')


def run_sql(sql_text):
    conn = get_db()
    res_list = []
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql_text)
            while True:
                row = cursor.fetchone()
                if row:
                    res_list.append(row)
                else:
                    break
            return res_list
    except pymysql.MySQLError as err:
        conn.rollback()
        print(type(err), err)


def get_keys_data():
    """从数据库获取需要关键字数据"""
    sql_text = """
        select keys_name, keys_count from tb_keys ORDER BY keys_count DESC  limit 0, 3;
    """
    return run_sql(sql_text)


@bp.route('/', methods=("GET", "POST"))
def index():
    keys_list = get_keys_data()
    keys = []
    for key in keys_list:
        key_obj = {
            "keys_name": key[0], "keys_count": key[1]
        }
        keys.append(key_obj)
    if request.method == "POST":
        input_key = request.form["search_text"]
        my_spider = SpiderHR(input_key, "上海")
        q = queue.Queue(1)
        new_thread = threading.Thread(target=my_spider.do_work, args=(q,))
        new_thread.start()
        while True:
            time.sleep(3)
            res_text = q.get()
            if res_text:
                print(res_text)
                break
        return render_template('pages/index.html', date_today=date_today, keys=keys,
                               res_text=res_text, input_key=input_key)

    return render_template('pages/index.html', date_today=date_today,
                           keys=keys, res_text=None, input_key=None)


@bp.route('/show_details/<key_word>')
def show_records(key_word, start_page=0, page_size=20):
    """详细展示某职位数据"""
    sql_text = f"""
        select * from tb_data where data_post like "%{key_word}%" or data_content like "%{key_word}%"
        ORDER BY data_id limit {start_page*page_size},{page_size};
    """
    records_tuples = run_sql(sql_text)
    keys = ["data_id", "data_post", "data_company", "data_address", "data_salary_min",
            "data_salary_max", "data_date", "data_edu", "data_exp", "data_content"]
    records = []
    for record_tuple in records_tuples:
        new_record = dict(zip(keys, record_tuple))
        records.append(new_record)

    sql_count = f"""
            SELECT count(*) as total_num from tb_data 
            WHERE data_post like "%{key_word}%" or data_content like "%{key_word}%";
        """
    print(sql_count)
    total_page = run_sql(sql_count)[0][0]
    print(total_page)
    current_page = start_page + 1

    return render_template('pages/records.html', records=records, total_page=total_page,
                           current_page=current_page)


@bp.route('/echarts/<key_word>')
def show_echarts(key_word):
    """展示数据分析图表"""
    return key_word

