#!/usr/bin/env python3
# -*- coding: utf-8 -*-



import pymysql
from pandas.core.frame import DataFrame
import re
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
        cursor.execute("select exper from data ")
        salary = cursor.fetchall()
        # 向数据库提交
        db.commit()
        return salary
    except:
        # 发生错误时回滚
        db.rollback()
        print("查询失败")
        return 0

def jinyanfun():
    edu = get_edu()
    data = []
    for i in edu:
        # print(type(i))
        year = re.findall(r"\d+", i[0])
        if len(year)==1:
            data.append(year[0]+'年工作经验')
        elif len(year)==2:
            data.append(year[0]+'-'+year[1]+'年工作经验')
        elif len(year)==0:
            data.append('无工作经验')

    data = DataFrame(data)
    da = data[0].value_counts()
    # print(da)
    list_all = []
    for (i, j) in zip(da.index, da):
        print(j,i)
        list_all.append([i,j])
    # print(type(da))
    return list_all


if __name__ == '__main__':
    a = jinyanfun()
    print(a)
