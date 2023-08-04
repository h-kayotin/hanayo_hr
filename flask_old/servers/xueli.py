#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import pymysql
from pandas.core.frame import DataFrame
from hanayo_hr import config

db = pymysql.connect(
    host="localhost",
    port=3306,
    user=config.USERNAME,
    password=config.PASSWORD,
    db=config.DATABASE,
    charset='utf8'
)

# 拿到游标
cursor = db.cursor()


def get_edu():
    try:
        cursor.execute("select edu from data ")
        salary = cursor.fetchall()
        # 向数据库提交
        db.commit()
        return salary
    except:
        # 发生错误时回滚
        db.rollback()
        print("查询失败")
        return 0

def xuelifun():
    edu = get_edu()
    data = []
    for i in edu:
       data.append(i)
       # print(i)

    data = DataFrame(data)
    da = data[0].value_counts()
    # print(da)
    list_all = []
    for (i, j) in zip(da.index, da):
        print(j, i)
        if '招' in i:
            # print(i)
            continue
        list_all.append([i, j])
    # print(type(da))
    return list_all


if __name__ == '__main__':
    a = xuelifun()
    print(a)
    print(type(a))