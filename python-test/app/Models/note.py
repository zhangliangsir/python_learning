#!/usr/bin/python3

from sqlalchemy import Column, String,INT,DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class Note(Base):
    # 表的名字:
    __tablename__ = 'notes'

    # 表的结构:
    id = Column(INT, primary_key=True)
    name = Column(String(20))
    date = Column(DateTime(20))
    data = Column(String(10000))
    
    @staticmethod
    def createNote():
        engine = create_engine('mysql://root:123456@127.0.0.1:3306/mysql_test')
        Base.metadata.create_all(engine)
 
if  __name__  ==  '__main__':        
    Note.createNote()