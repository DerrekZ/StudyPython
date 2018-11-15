#!/usr/bin/python
#Filename: UserManage.py

import sys
sys.path.append('Base')
import DBHandles

dFucs = DBHandles.DFucs()

sql_gUsers = "select * from user where userid=%d" % (1)
data = dFucs.getData(dbName='mytest', sql=sql_gUsers)
print(data)
