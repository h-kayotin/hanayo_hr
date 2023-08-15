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
from hanayo_hr.db import get_db, get_db_pd
import pymysql
from hanayo_hr.spider_hr import SpiderHR
import threading
import queue
import pandas as pd
from sqlalchemy import text
import matplotlib.pyplot as plt

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
def show_records(key_word, start_page=1, page_size=10):
    start_page = int(start_page) - 1
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
    total_page = math.ceil(run_sql(sql_count)[0][0] / page_size)
    current_page = start_page + 1
    return render_template('pages/records.html', records=records, total_page=total_page,
                           current_page=current_page, date_today=date_today, key_word=key_word)


@bp.route('/<key_word>/<page>')
def next_page(page, key_word):
    """对于筛选后的结果进行翻页"""
    next_page_num = int(page)
    # print(f"当前页码是{page}，筛选项目是{status}")
    if next_page_num > 0:
        return show_records(key_word, next_page_num)
    else:
        return show_records(key_word)


def get_dataframe(key_word):
    """获取某关键字的所有dataframe对象"""
    engine = get_db_pd()
    sql_text = f"""
        select * from tb_data 
        where data_post like "%{key_word}%" or data_content like "%{key_word}%";
    """
    data_frame = pd.read_sql(text(sql_text), engine.connect(), index_col='data_id')
    return data_frame


def get_salary_echarts_data(df):
    """获取供图表展示的薪资数据"""
    df_salary = df[["data_salary_min", "data_salary_max"]]
    df_salary = df_salary.drop(df_salary[(df_salary.data_salary_min < 2000)].index)
    df_salary["mean"] = (df_salary["data_salary_min"] + df_salary["data_salary_max"]) / 2
    bins = [0, 8000, 12000, 15000, 20000, df_salary["mean"].max()]
    df_salary["group"] = pd.cut(df_salary["mean"], bins=bins)
    grouped = df_salary.groupby("group")
    values_list = []
    for name, group in grouped:
        values_list.append(len(group))
    columns = ["8k以下", "8k-12k", "12k-15k", "15k-20k", "20k以上"]
    return columns, values_list


def get_pie_data(df, option):
    """获取供饼图展示的数据"""
    df_exp = df[[option]]
    groups = df_exp.groupby(option)
    groups = groups[option].count()
    res_list = []
    for key, value in groups.items():
        res_list.append({
            "name": key, "value": value
        })
    return res_list


@bp.route('/echarts/<key_word>')
def show_echarts(key_word):
    """展示数据分析图表"""
    df = get_dataframe(key_word)
    salary_columns, salary_values = get_salary_echarts_data(df)
    edu_list = get_pie_data(df, "data_edu")
    exp_list = get_pie_data(df, "data_exp")

    return render_template('pages/echarts.html', date_today=date_today, salary_columns=salary_columns,
                           salary_values=salary_values, edu_list=edu_list, exp_list=exp_list)

