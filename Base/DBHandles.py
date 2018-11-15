#!/usr/bin/python
# Filename: DBHandles.py

import pymysql
import dbConfig

class DFucs:
    def getData(self, dbName, sql):
        try:
            conn = pymysql.connect(db=dbName, **dbConfig.config)
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