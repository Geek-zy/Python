#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# 安装PyMySQL
# sudo pip install PyMySQL

import pymysql


config = {

    'host':'localhost',
    'port':3306,
    'user':'root',
    'passwd':'root',
    'db':'Geek_Web',
    'charset':'utf8mb4',
    # 数据库内容以字典格式输出
    #'cursorclass':pymysql.cursors.DictCursor,
}

# 连接数据库
def Mysql():

    # 连接数据库
    #db = pymysql.connect(host="localhost", port=3306, user="root", passwd="root", db="Geek_Web", charset="utf8mb4")
    db = pymysql.connect(**config)
    #cursor()方法获取操作游标 
    pointer = db.cursor()

    try:

        return (db, pointer)
    
    except:
        
        print("数据库访问失败")

# 增
def Insert(db, pointer):
    sql = "insert into main(id, Tag, Name, Version, Introduce, Class, Worked_OS, Course_URL, Download_URL, Image_URL, Remarks_1, Remarks_2) \
     values (NULL, '软件编号', '软件名称', '软件版本', '软件简介', '软件类别', '运行环境', '教程地址', '下载地址', '图标地址', '备注1', '备注2')"
    # 执行SQL语句
    pointer.execute(sql)
    # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
    db.commit()

# 删
def Delect(db, pointer):
    sql = "DELETE FROM main WHERE Name = '修改后的名字'"
    pointer.execute(sql)
    db.commit()

# 查
def Select(db, pointer):
    sql = "SELECT * FROM main"
    pointer.execute(sql)
    # 获取所有记录列表
    results = pointer.fetchall()
    
    return results

# 改
def Update(db, pointer):
    sql = "UPDATE main SET Name = '修改后的名字' WHERE Remarks_2 = '备注2'"
    pointer.execute(sql)
    db.commit()

# 关闭数据库连接
def Close(db, pointer):
    pointer.close()
    db.close()

(db, pointer) = Mysql()
print("\n-------------数据库初始状态-------------")
print(Select(db, pointer))
Insert(db, pointer)
print("\n-------------数据库插入数据-------------")
print(Select(db, pointer))
Update(db, pointer)
print("\n-------------数据库修改数据-------------")
print(Select(db, pointer))
Delect(db, pointer)
print("\n-------------数据库删除数据-------------")
print(Select(db, pointer))
Close(db, pointer)

