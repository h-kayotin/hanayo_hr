"""
db - 连接数据库

Author: kayotin
Date 2023/8/10
"""


from flask import current_app, g
from hanayo_hr.config import DATABASE, USERNAME, PASSWORD, DB_URI
import pymysql
from sqlalchemy import create_engine


def get_db():
    """获取数据库对象"""
    if 'db' not in g:
        g.db = pymysql.connect(host="192.168.32.11", port=3306,
                               user=USERNAME, password=PASSWORD,
                               database=DATABASE, charset="utf8mb4")
    return g.db


def get_db_pd():
    """用pandas连接数据库"""
    engine = create_engine(DB_URI)
    return engine



def close_db(e=None):
    """关闭数据库连接"""
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_app(app):
    app.teardown_appcontext(close_db)




