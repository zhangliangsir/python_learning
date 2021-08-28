#!/usr/bin/python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()
class sqlUtil():
    @staticmethod
    def getSession():
        
        # 初始化数据库连接:
        #engine = create_engine("mysql://root:123456@127.0.0.1:3306/mysql_test")
        engine = create_engine("mysql+pymysql://root:123456@127.0.0.1:3306/mysql_test")
        # 创建DBSession类型:
        session = sessionmaker(bind=engine)

        return session()
    