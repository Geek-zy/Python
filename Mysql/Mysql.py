#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# 安装PyMySQL
# sudo pip install PyMySQL

import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "root", "root", "Geek_Web" )

# 使用cursor()方法获取操作游标 
cursor = db.cursor()

# 创建数据表SQL语句
sql = "SELECT * FROM main"

try:
    # 执行SQL语句
    cursor.execute(sql)
             
    # 获取所有记录列表
    results = cursor.fetchall()
    
    # 打印结果
    print (results)

except:
    print ("数据访问失败")

# 关闭数据库连接
db.close()

