#!/usr/bin/env python3

# -*- coding:utf-8 -*-
from app import db#导入db 对象
class Data(db.Model):#定义User类
       """ 定义User类 """
       __tablename__='data'#表的别名
       data_id = db.Column(db.Integer,primary_key=True,autoincrement=True)   #定义id字段
       post = db.Column(db.String(50),nullable=False)                        #定义post字段
       company = db.Column(db.String(100),nullable=False)                    #定义company字段
       address = db.Column(db.String(11), nullable=False)                    #定义address字段
       salary_min = db.Column(db.String(11), nullable=False)                 #定义salary_min字段
       salary_max = db.Column(db.String(11), nullable=False)                 # 定义salary_max字段
       dateT = db.Column(db.String(11), nullable=False)                      # 定义dateT字段
