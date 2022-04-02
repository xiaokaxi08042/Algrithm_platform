import os
import sqlite3
from tkinter import *
from tkinter.filedialog import *
from tkinter.ttk import *
import select_func


# 打开文件
def openfile():
    filePath = askopenfilename()  # 全路径
    fileName = os.path.basename(filePath)  # 文件名
    tab = Frame(master=tabBar)
    tabBar.add(tab, text=fileName)
    textContainer = Labelframe(tab)
    textContainer.pack(expand=YES, fill=BOTH)
    tabBar.pack(expand=YES, fill=BOTH)
    textArea = Text(master=textContainer)
    textArea.pack(side=LEFT, expand=YES, fill=BOTH)
    inSql(filePath, fileName, textArea)
    '''
    f = open(filePath, mode='r', encoding="utf-8")
    while True:
       line = f.readline()
       if not line : break
       textArea.insert(INSERT, line)
    f.close()
    '''
    # 右侧滑动条
    scrollBar = Scrollbar(master=textContainer)
    scrollBar.pack(side=RIGHT, fill=Y)
    # 导航条获得文本位置
    scrollBar.config(command=textArea.yview)
    # 文本获得导航条位置
    textArea.config(yscrollcommand=scrollBar.set)


# 写入数据库
def inSql(filePath, fileName, textArea):
    cx = sqlite3.connect('./datafile.db')  # 创建数据库，如果数据库已经存在，则链接数据库；如果数据库不存在，则先创建数据库，再链接该数据库。
    cu = cx.cursor()  # 定义一个游标，以便获得查询对象。
    print('mao')
    fileName = "'" + fileName + "'"
    print(fileName)
    s = 'create table if not exists ' + fileName + ' (id integer primary key,w integer,v integer )'
    print(s)
    cu.execute(s)  # 创建表，此处须修改表名
    f = open(filePath, mode='r', encoding="utf-8")
    list = []
    i = 0
    for line in f.readlines():
        textArea.insert(INSERT, line)
        list.append(line.strip().split(' '))
        cu.execute('insert into '+ fileName + ' values(?,?,?)', (i, list[i][0], list[i][1]))
        i += 1
    f.close()  # 关闭文件
    cu.close()  # 关闭游标
    cx.commit()  # 事务提交
    cx.close()  # 关闭数据库


# 创建窗口：实例化一个窗口对象。
root = Tk()
root.geometry('500x400')
root.title('0/1背包算法求解平台')
# root.configure(background='pink')

menuBar = Menu(root)
shujuMenu = Menu(menuBar, tearoff=0)
suanfaMenu = Menu(menuBar, tearoff=0)
pictureMenu = Menu(menuBar, tearoff=0)
sortMenu = Menu(menuBar, tearoff=0)
logMenu = Menu(menuBar, tearoff=0)

bendiMenu = Menu(shujuMenu)
dpMenu = Menu(suanfaMenu)
gdMenu = Menu(suanfaMenu)
btMenu = Menu(suanfaMenu)
ycMenu = Menu(suanfaMenu)
sandianMenu = Menu(pictureMenu)
zhuzMenu = Menu(pictureMenu)
dzMenu = Menu(sortMenu)
djMenu = Menu(sortMenu)

menuBar.add_cascade(label="导入数据", menu=shujuMenu)
menuBar.add_cascade(label="算法求解", menu=suanfaMenu)
menuBar.add_cascade(label="绘制图形", menu=pictureMenu)
menuBar.add_cascade(label="排序", menu=sortMenu)
menuBar.add_cascade(label="日志记录", menu=logMenu)
suanfaMenu.add_command(label="动态规划", command=select_func.dpAlgrithm, background='pink')
suanfaMenu.add_command(label="贪心算法", command=select_func.gdAlgrithm, background='pink')
suanfaMenu.add_command(label="回溯算法", command=select_func.btAlgrithm, background='pink')
suanfaMenu.add_command(label="遗传算法", command=select_func.ycAlgrithm, background='pink')
shujuMenu.add_command(label="选择文件", command=openfile, background='pink')
pictureMenu.add_command(label="散点图", command=select_func.sdAlgrithm, background='pink')
pictureMenu.add_command(label="柱状图", command=select_func.zzAlgrithm, background='pink')
sortMenu.add_command(label="递增排序", command=select_func.dzAlgrithm, background='pink')
sortMenu.add_command(label="递减排序", command=select_func.djAlgrithm, background='pink')
logMenu.add_command(label="算法日志", command=select_func.logAlgrithm, background='pink')

tabBar = Notebook(master=root)
root.configure(menu=menuBar)
# 显示窗口
root.mainloop()
"""
注意到：该窗口默认的显示位置在哪里，观察我下面的截图。
窗口默认显示在整个电脑屏幕的左上角，并且窗口大小特别小。
"""