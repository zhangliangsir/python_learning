#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql
import config

def create_conn():
    # 连接database
    conn = pymysql.connect(host=config.hostIP, user=config.userName,password=config.passWord,database=config.dataName,charset="utf8mb4")
    # 返回连接和一个可以执行SQL语句的光标对象
    return conn,conn.cursor()

def create():
    conn,cursor=create_conn()
    
    sql_create = """
    CREATE TABLE USER1 (
    id INT auto_increment PRIMARY KEY ,
    name CHAR(10) NOT NULL UNIQUE,
    age TINYINT NOT NULL,
    passwd CHAR(10) NOT NULL,
    address CHAR(10) NOT NULL
    )ENGINE=innodb DEFAULT CHARSET=utf8mb4;
    """
    try:
        #delete data
        cursor.execute(sql_create)
    
        conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()
    finally:
        closed(cursor,conn)

def insert(data):
    conn,cursor=create_conn()
    sql_insert = "INSERT INTO USER1(name, age,passwd,address) VALUES (%s,%s,%s,%s);"
    try:
        cursor.execute(sql_insert,data)
    
        conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()
    finally:
        closed(cursor,conn)
    
def batch_insert():
    conn,cursor=create_conn()
    sql_insert = "INSERT INTO USER1(name, age) VALUES (%s, %s);"
    data = [("Alex", 18), ("Egon", 20), ("Yuan", 21)]
    try:
        cursor.execute(sql_insert,data)
    
        conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()
    finally:
        closed(cursor,conn)

def delete(userName):
    conn,cursor=create_conn()
    sql_delete = "DELETE FROM USER1 WHERE name=%s;"
    try:
        cursor.execute(sql_delete,[userName])
    
        conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()
    finally:
        closed(cursor,conn)

def update(data):
    conn,cursor=create_conn()
    sql_update = "UPDATE USER1 SET age=%s,passwd=%s,address=%s WHERE name=%s;"
    try:
        cursor.execute(sql_update,data)
    
        conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()
    finally:
        closed(cursor,conn)
        

def query(username):
    conn,cursor=create_conn()
    sql_query = "SELECT name,age,passwd,address from USER1 WHERE name=%s;"
    
    cursor.execute(sql_query,[username])
    # 获取单条查询数据
    ret = cursor.fetchone()
    print(ret)
    closed(cursor,conn)
    return ret

def batch_query():
    conn,cursor=create_conn()
    batch_query = "SELECT name,age,passwd,address from USER1;"
    
    cursor.execute(batch_query)
    # 获取多条查询数据
    ret = cursor.fetchall()
    print(ret)
    closed(cursor,conn)
    return ret

def drop_table(tableName):
    conn,cursor=create_conn()
    
    sql_deleteTable = "DROP TABLE %s;" % tableName
    try:
        #delete data
        cursor.execute(sql_deleteTable)
        print("%s table drop successful" % tableName)
        conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()
    finally:
        closed(cursor,conn)

#查询指定数量的数据    
def fixed_data():
    conn,cursor=create_conn()
    batch_query = "SELECT id,name,age from USER1;"
    
    cursor.execute(batch_query)
    # 获取多条查询数据
    ret = cursor.fetchmany(2)
    print(ret)
    closed(cursor,conn)
    return ret
    
#光标移动位置
def cursor_move():
    conn,cursor=create_conn()
    try:
        batch_query = "SELECT id,name,age from USER1;"
        cursor.execute(batch_query)
    
    # 光标按绝对位置移动1
        cursor.scroll(1, mode="absolute")
    # 光标按照相对位置(当前位置)移动1
#     cursor.scroll(1, mode="relative")
        ret=cursor.fetchall()
        print(ret)
    except Exception as e:
        print(e)
        conn.rollback()
    finally:
        closed(cursor,conn)
        return ret
    
#查看连接数
def conn_num():
    conn,cursor=create_conn()
    sql_query = "show status like 'thread%';"
    
    cursor.execute(sql_query)
    # 获取单条查询数据
    ret = cursor.fetchone()
    print(ret)
    closed(cursor,conn)
    return ret

#关闭光标和连接
def closed(cursor,conn):
    if cursor == None: 
        cursor.close()
    if conn == None:
        conn.close()

if  __name__  ==  '__main__':
#     query()
#     create()
    batch_query()
    
    #insert
#     data=["hello",20,"hello","hangzhou"]
#     insert(data)
    
    #update
#     data=[21,"admin","guangzhou","admin"]
#     update(data)
    
    #delete
#     delete("hello")

    #query
#     query("admin")

    #drop table
#     drop_table("USER1")

#     conn_num()
#     fixed_data()
#     cursor_move()
    query("cat")
    batch_query()
    print("execute successful")
    
    