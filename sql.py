import sqlite3      #导入sqlite3


cx = sqlite3.connect('./data.db')  # 创建数据库，如果数据库已经存在，则链接数据库；如果数据库不存在，则先创建数据库，再链接该数据库。
cu = cx.cursor()           # 定义一个游标，以便获得查询对象。
t1 = 't3'
s = 'create table if not exists '+ t1 +' (id integer primary key,w integer,v integer )'
print(s)
cu.execute(s)  # 创建表，此处须修改表名

fr = open("data/beibao2.in")    # 打开要读取的txt文件
list=[]
i=0
for line in fr.readlines():
    list.append(line.strip().split(' '))
    cu.execute('insert into '+ t1 +' values(?,?,?)', (i, list[i][0], list[i][1]))
    i += 1

'''
cu.execute('create table if not exists t1 (id integer primary key,w integer,v integer )')  # 创建表，此处须修改表名
fr = open("data/beibao1.in")    # 打开要读取的txt文件
list=[]
i=0
for line in fr.readlines():
    list.append(line.strip().split(' '))
    cu.execute('insert into t1 values(?,?,?)', (i, list[i][0], list[i][1]))
    i += 1

cu.execute('create table if not exists t2 (id integer primary key,w integer,v integer )')  # 创建表，此处须修改表名
fr = open("data/beibao2.in")    # 打开要读取的txt文件
list=[]
i=0
for line in fr.readlines():
    list.append(line.strip().split(' '))
    cu.execute('insert into t2 values(?,?,?)', (i, list[i][0], list[i][1]))
    i += 1
cu.execute('create table if not exists t3 (id integer primary key,w integer,v integer )')  # 创建表，此处须修改表名
fr = open("data/beibao3.in")    # 打开要读取的txt文件
list=[]
i=0
for line in fr.readlines():
    list.append(line.strip().split(' '))
    cu.execute('insert into t3 values(?,?,?)', (i, list[i][0], list[i][1]))
    i += 1

cu.execute('create table if not exists t4 (id integer primary key,w integer,v integer )')  # 创建表，此处须修改表名
fr = open("data/beibao4.in")    # 打开要读取的txt文件
list=[]
i=0
for line in fr.readlines():
    list.append(line.strip().split(' '))
    cu.execute('insert into t4 values(?,?,?)', (i, list[i][0], list[i][1]))
    i += 1
cu.execute('create table if not exists t5 (id integer primary key,w integer,v integer )')  # 创建表，此处须修改表名
fr = open("data/beibao5.in")    # 打开要读取的txt文件
list=[]
i=0
for line in fr.readlines():
    list.append(line.strip().split(' '))
    cu.execute('insert into t5 values(?,?,?)', (i, list[i][0], list[i][1]))
    i += 1

cu.execute('create table if not exists t6 (id integer primary key,w integer,v integer )')  # 创建表，此处须修改表名
fr = open("data/beibao6.in")    # 打开要读取的txt文件
list=[]
i=0
for line in fr.readlines():
    list.append(line.strip().split(' '))
    cu.execute('insert into t6 values(?,?,?)', (i, list[i][0], list[i][1]))
    i += 1
cu.execute('create table if not exists t7 (id integer primary key,w integer,v integer )')  # 创建表，此处须修改表名
fr = open("data/beibao7.in")    # 打开要读取的txt文件
list=[]
i=0
for line in fr.readlines():
    list.append(line.strip().split(' '))
    cu.execute('insert into t7 values(?,?,?)', (i, list[i][0], list[i][1]))
    i += 1

cu.execute('create table if not exists t8 (id integer primary key,w integer,v integer )')  # 创建表，此处须修改表名
fr = open("data/beibao8.in")    # 打开要读取的txt文件
list=[]
i=0
for line in fr.readlines():
    list.append(line.strip().split(' '))
    cu.execute('insert into t8 values(?,?,?)', (i, list[i][0], list[i][1]))
    i += 1
cu.execute('create table if not exists t9 (id integer primary key,w integer,v integer )')  # 创建表，此处须修改表名
fr = open("data/beibao9.in")    # 打开要读取的txt文件
list=[]
i=0
for line in fr.readlines():
    list.append(line.strip().split(' '))
    cu.execute('insert into t9 values(?,?,?)', (i, list[i][0], list[i][1]))
    i += 1
'''
cu.close()  # 关闭游标
cx.commit()   # 事务提交
cx.close()  # 关闭数据库