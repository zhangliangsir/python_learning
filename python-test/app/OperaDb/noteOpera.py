#!/usr/bin/python3

from app.SqlDefine.sqlUtil import sqlUtil
from app.Models.note import Note
import sys

class noteOpera():
    
    @staticmethod
    def queryNote():
        session=sqlUtil.getSession()
#         notes = session.query(Note).filter_by(id=1).all()
        notes = session.query(Note).filter().all()
        for item in notes:
            print(item.id,item.name,item.date,item.data)
        session.close()
    
    @staticmethod
    def insertNote(note):
        try:
            session=sqlUtil.getSession()
            session.add(note)
            session.commit()
        except:
            print(sys.exc_info()[0], sys.exc_info()[1])
            session.rollback()
            raise
        finally:
            session.close()
          
    @staticmethod
    def updateNote(updateDict):
        try:
            session=sqlUtil.getSession()
            session.query(Note).filter_by(id=1).update(updateDict)
            session.commit()
        except:
            print(sys.exc_info()[0], sys.exc_info()[1])
            session.rollback()
            raise
        finally:
            session.close() 
    
    @staticmethod
    def deleteNote(deleteDict):
        try:
            session=sqlUtil.getSession()
            print(deleteDict[0])
            session.query(Note).filter(Note.deleteDict[0].key==deleteDict[0].value).delete()
            session.commit()
        except:
            print(sys.exc_info()[0], sys.exc_info()[1])
            session.rollback()
            raise
        finally:
            session.close()  

if  __name__  ==  '__main__': 
    
    #insert
#     note=Note(id=4,name="test",date="2019-08-13 17:07:49",data="hello everyone!")
#     note=Note({"id":"4","name":"test","date":"2019-08-13 17:07:49","data":"hello everyone!"})        #这个还需要测试一下
#     noteOpera.insertNote(note)
    
    #query
    noteOpera.queryNote()
    
    #update
#     updateDict={"name":"haha","date":"2020-02-13 17:07:49","data":"hello everydsone!"}
#     noteOpera.updateNote(updateDict)
    
    #deltete
    deleteDict={"id","1"}
    noteOpera.deleteNote(deleteDict)
