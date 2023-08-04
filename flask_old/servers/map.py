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


def get_xinzi():
    try:
        cursor.execute("select address from data ")
        salary = cursor.fetchall()
        # 向数据库提交
        db.commit()
        return salary
    except:
        # 发生错误时回滚
        db.rollback()
        print("查询失败")
        return 0
a = get_xinzi()

list = []
for i in a:
    test = i[0].split('-')
    list.append(test[0])
    # print(test)

data = DataFrame(list)
da = data[0].value_counts()


for (i,j) in zip(da.index,da):
    pass
    print(j,i)
print(type(da))