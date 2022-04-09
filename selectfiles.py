import sqlite3


'''
def bb():
    win = tkinter.Tk()
    win.title("Combobox下拉框")
    win.geometry("800x600+600+100")

    cv = tkinter.StringVar()
    com = ttk.Combobox(win, textvariable=cv)
    com.pack()
    huoqu(com)
    # 设置下拉数据
    # com["value"] = ("福建", "江西", "浙江")
    # 设置默认值
    com.current(0)
'''

# 获取数据库中表名
def huoqu(com):
    conn = sqlite3.connect('data.db')
    cu = conn.cursor()

    # 获取表名，保存在tab_name列表
    # cu.execute('select * from' + "'" + 'beibao0.in' +"'")
    cu.execute("select name from sqlite_master where type='table'")
    com = cu.fetchall()
    print(com)
    # 之所以保存为元组，一是可避免误操作修改字段名，二是元组巧用转化字符串，可
    # 直接用于SQL的insert语句中。例如下面代码可得到第一个表的带括号字段名集合：
    '''
    sql_col_name=str(col_names[0]).replace('\'','')
    '''
