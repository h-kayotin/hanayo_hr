#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#encoding:utf-8
HOST = '127.0.0.1'
PORT = '3306'
USERNAME = 'root'
PASSWORD = '66688888'
DATABASE = 'u1'
DB_URI = 'mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8mb4'.format(username=USERNAME,
                                                                                        password=PASSWORD,
                                                                                        host=HOST,
                                                                                        port=PORT,
                                                                                        db=DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False