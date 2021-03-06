# -*- coding: UTF-8 -*-

import os
from datetime import timedelta

DEBUG = True
SECRET_KEY = os.urandom(24)
PERMANENT_SESSION_LIFETIME = timedelta(days=5)

# 数据库配置 这里使用MYSQL
DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'root' # 用户名、密码根据各位本地mysql的设置而定
PASSWORD = '123456'
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'db_bignews2'

SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT,DRIVER,USERNAME,PASSWORD,HOST,PORT,DATABASE)

SQLALCHEMY_TRACK_MODIFICATIONS = False