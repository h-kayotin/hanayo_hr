"""
index - home页面，网站入口

Author: kayotin
Date 2023/8/10
"""

from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, session
)
from werkzeug.exceptions import abort
import datetime
import math
from hanayo_hr.db import get_db
import pymysql

bp = Blueprint('index', __name__)
date_today = datetime.datetime.today().strftime('%Y-%m-%d')


def get_data():
    """从数据库获取需要的数据"""
    conn = get_db()
    sql_text = """
        select * from tb_data limit 0,10
    """
    try:
        with conn.cursor() as cursor:
            affected_rows = cursor.execute(sql_text)
            row = cursor.fetchone()
            while row:
                print(row)
                row = cursor.fetchone()
    except pymysql.MySQLError as err:
        conn.rollback()
        print(type(err), err)
    finally:
        conn.close()



@bp.route('/')
def index():
    keys = [
        {"keys_name": "python", "keys_count": 200},
        {"keys_name": "java", "keys_count": 200},
        {"keys_name": "c++", "keys_count": 200}
    ]
    return render_template('pages/index.html', date_today=date_today, keys=keys)
