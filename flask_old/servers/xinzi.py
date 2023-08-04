#!/usr/bin/env python3
# -*- coding: utf-8 -*-



import pymysql
import pandas as pd
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
        cursor.execute("select salary_min,salary_max from data ")
        salary = cursor.fetchall()
        # 向数据库提交
        db.commit()
        return salary
    except:
        # 发生错误时回滚
        db.rollback()
        print("查询失败")
        return 0

def xinzi():
    a = get_xinzi()
    data = []
    for i in a:
        data.append((int(i[0])+int(i[1]))/2)

    fenzu=pd.cut(data,[0,5000,8000,11000,14000,17000,20000,23000,9000000000],right=False)
    pinshu=fenzu.value_counts()
    # print(pinshu)
    list = []
    for i in pinshu:
        # print(i)
        list.append(i)

    list_all = [
        ['小于5k', list[0]],
        ['5k~8k', list[1]],
        ['8k~11k',list[2]],
        ['11k~14k',list[3]],
        ['14k-17k', list[4]],
        ['17k-20k', list[5]],
        ['20k-23k', list[6]],
        ['23K~', list[7]]
    ]
    return list

if __name__ == '__main__':
    a = xinzi()
    print(a)