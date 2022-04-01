# python 获取sqlite3数据库mydb.db中的表名和表字段名

import sqlite3


def huoqu():
        conn = sqlite3.connect('data.db')
        cu = conn.cursor()

        # 获取表名，保存在tab_name列表
        # cu.execute('select * from' + "'" + 'beibao0.in' +"'")
        cu.execute("select name from sqlite_master where type='table'")
        tab_name = cu.fetchall()
        print(tab_name)
        # 之所以保存为元组，一是可避免误操作修改字段名，二是元组巧用转化字符串，可
        # 直接用于SQL的insert语句中。例如下面代码可得到第一个表的带括号字段名集合：
        '''
          sql_col_name=str(col_names[0]).replace('\'','')
        '''


