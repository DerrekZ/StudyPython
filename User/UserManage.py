#!/usr/bin/python
#Filename: UserManage.py

import sys
sys.path.append('Base')
import DBHandles
import urllib
import json
# import numpy as np

# 数据库查询文章
def getArticles(a, b):
    sql_query = "select ArticleId,Title,Content from AC_Article_Content where ArticleId > %d and ArticleId <= %d order by ArticleId asc" % (
        a, b)
    sqlserver = DBHandles.dbSqlServer('Truckhome')
    result = sqlserver.getData(sql_query)
    return result

# 标签切割
def makeLabels(articleid, content):
    url = 'http://192.168.0.20:500/get_key_words'
    values = {'id': articleid, 'content': content}
    data = urllib.parse.urlencode(values).encode('utf-8')
    headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
    response = urllib.request.Request(url, data=data, headers=headers)
    html = urllib.request.urlopen(response).read().decode('utf-8')
    returnData = json.loads(html)
    return returnData

# 将标签保存到数据库
def InsertLabels(sql_insert):
    sqlserver = DBHandles.dbSqlServer('UserAnalysis')
    result = sqlserver.ExecuteSql(sql_insert)
    return result


# 输出标签结果
if __name__ == '__main__':

    a = 7000
    b = 7100
    while a < 12000:
        
        # 文章
        articles = getArticles(a, b)
        # 分词
        for i, (ArticleId, Title, Content) in enumerate(articles):
            lables = makeLabels(ArticleId, Content)
            print("\n文章id:" + str(ArticleId))
            
            # 打印标签
            sql_insert = ""
            for key, value in lables['data'].items():
                if key != '-':
                    print(key + ":" + value)
                    if sql_insert == "": 
                        sql_insert = "INSERT INTO [ArticleKeyWords_python]([F_ArticleID],[F_KeyWord],[F_Count]) values (%d,'%s',%d)," % (ArticleId, key, int(value))
                    else: 
                        sql_insert += "(%d,'%s',%d)," % (ArticleId, key, int(value))
            sql_insert = sql_insert[0:-1]
            InsertLabels(sql_insert)
        a = a + 100
        b = b + 100
                    
