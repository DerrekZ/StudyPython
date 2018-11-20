#!/usr/bin/python
# Filename: DBHandles.py

import pymysql
import pymssql
import dbConfig

class dbMysql:
    def getData(self, dbName, sql):
        try:
            conn = pymysql.connect(db=dbName, **dbConfig.mysql_config)
        except pymysql.err as e:
            print('connect fails!{}'.format(e))
        cursor = conn.cursor()
        try:
            rowNums = cursor.execute(sql)
            data = cursor.fetchall()
        except cursor.Error as e:
            print('query error!{}'.format(e))
        finally:
            cursor.close()
            conn.close()
        return data

class dbSqlServer:
    conn = None
    cursor = None

    #构造函数，初始化数据库连接
    def __init__(self, dbName): 
        try:
            self.conn = pymssql.connect(database=dbName, **dbConfig.sqlserver_config)
        except pymysql.err as e:
            print('connect fails!{}'.format(e))
        self.cursor = self.conn.cursor()

    #查询方法
    def getData(self, sql):
        try:
            rowNums = self.cursor.execute(sql)
            data = self.cursor.fetchall()
        except:
            print('query error!')
        finally:
            self.cursor.close()
            self.conn.close()
        return data

    #插入方法
    def ExecuteSql(self, sql): 
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except: 
            print('insert or update error!')
        finally: 
            self.cursor.close()
            self.conn.close()


