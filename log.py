import sqlite3


def log():
    mydb = sqlite3.connect('datafile.db')  # 链接数据库
    cur = mydb.cursor()  # 创建游标cur来执行SQL语句

    # 获取表名
    cur.execute('SELECT * FROM log')
    list = cur.fetchall()
    for i in range(len(list)):
        print(list[i])
    return list