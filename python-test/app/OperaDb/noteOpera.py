#!/usr/bin/python3

import sys
sys.path.append("..")

from SqlDefine.sqlUtil import sqlUtil
from Models.note import Note


class noteOpera():
    
    @staticmethod
    def queryNote():
        session=sqlUtil.getSession()

#         notes = session.query(Note).filter_by(id=1).all()
        notes = session.query(Note).filter(Note.id>=1).all()
        for item in notes:
            print(item.id,item.name,item.date_time,item.data)
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
            print(deleteDict["id"])
            session.query(Note).filter(Note.id==deleteDict["id"]).delete()

            session.commit()
        except:
            print(sys.exc_info()[0], sys.exc_info()[1])
            session.rollback()
            raise
        finally:
            session.close()  

if  __name__  ==  '__main__':
    # query
    noteOpera.queryNote()

    #insert
    note=Note(id=1,name="test1",date_time="2019-08-13 17:07:49",data="hello everyone!")
    #note=Note({"id":"4","name":"test","date_time":"2019-08-13 17:07:49","data":"hello everyone!"})        #这个还需要测试一下
    noteOpera.insertNote(note)
    

    
    #update
    # updateDict={"name":"haha","date_time":"2020-02-13 17:07:49","data":"hello everydsone!"}
    # noteOpera.updateNote(updateDict)
    
    #deltete
    # deleteDict={"id":"1"}
    # noteOpera.deleteNote(deleteDict)

    # query
    noteOpera.queryNote()