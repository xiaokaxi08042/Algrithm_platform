# -*- coding: UTF-8 -*-
import sqlite3


def sqlite_read():
    """python读取sqlite数据库文件
    """
    mydb = sqlite3.connect('datafile.db')       # 链接数据库
    cur = mydb.cursor()                         # 创建游标cur来执行SQL语句

    # 获取表名
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' and name != 'log'")
    Tables = cur.fetchall()                     # Tables 为元组列表
    # print(Tables)
    language = []
    for i in range(len(Tables)):
        language.append(Tables[i][0])
    # print(language)
    return language
# sqlite_read()


def table_data(s):
    mydb = sqlite3.connect('datafile.db')  # 链接数据库
    cur = mydb.cursor()  # 创建游标cur来执行SQL语句

    # 获取表的内容
    cur.execute('SELECT * FROM' + "'" + s + "'")
    list = cur.fetchall()  # Tables 为元组列表
    # print(list)
    w = []
    v = []
    for i in range(len(list)):
        if i == 0:
            c = list[i][1]
            n = list[i][2]
        else:
            w.append(list[i][1])
            v.append(list[i][2])
    return c, n, w, v


# 存入日志记录
def in_log(time, s1, s):
    cx = sqlite3.connect('./datafile.db')  # 创建数据库，如果数据库已经存在，则链接数据库；如果数据库不存在，则先创建数据库，再链接该数据库。
    cu = cx.cursor()  # 定义一个游标，以便获得查询对象。
    cu.execute('insert into log values(?,?,?)', (time, s1, s))
    cu.close()  # 关闭游标
    cx.commit()  # 事务提交
    cx.close()  # 关闭数据库