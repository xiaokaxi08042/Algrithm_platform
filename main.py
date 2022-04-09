import os
import sys
import time
import sqlite3
import tkinter

import select_func
from tkinter import *
from tkinter.ttk import *
from search import in_log
from tkinter.filedialog import *
from tkinter.messagebox import *
from PyQt5.QtWidgets import QMainWindow, QApplication

# 打开文件
def openfile():
    filePath = askopenfilename()  # 全路径
    fileName = os.path.basename(filePath)  # 文件名
    tab = Frame(master=tabBar)
    tabBar.add(tab, text=fileName)
    textContainer = Labelframe(tab)
    textContainer.pack(expand=YES, fill=BOTH)
    tabBar.pack(expand=YES, fill=BOTH)
    textArea = Text(master=textContainer, background='lightskyblue')
    textArea.pack(side=LEFT, expand=YES, fill=BOTH)
    inSql(filePath, fileName, textArea)
    time1 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())  # 执行该操作的时间
    in_log(time1, '导入数据', fileName)
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
    cu.execute('create table if not exists ' + "'" + fileName + "'" + ' (id integer primary key,w integer,v integer )')  # 创建表，此处须修改表名
    f = open(filePath, mode='r', encoding="utf-8")
    list = []
    i = 0
    for line in f.readlines():
        textArea.insert(INSERT, line)
        list.append(line.strip().split(' '))
        cu.execute('insert into ' + "'" + fileName + "'" + ' values(?,?,?)', (i, list[i][0], list[i][1]))
        i += 1

    f.close()  # 关闭文件
    cu.close()  # 关闭游标
    cx.commit()  # 事务提交
    cx.close()  # 关闭数据库


# 创建窗口：实例化一个窗口对象。
app = QApplication(sys.argv)
root = Tk()
root.geometry('500x400')
root.title('0/1背包算法求解平台')
# root.attributes('-alpha', 0.8)
# root.configure(background='lightskyblue')
root.maxsize(500, 300)
root.minsize(500, 300)

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
suanfaMenu.add_command(label="动态规划", command=select_func.dpAlgrithm, background='lightskyblue')
suanfaMenu.add_command(label="贪心算法", command=select_func.gdAlgrithm, background='pink')
suanfaMenu.add_command(label="回溯算法", command=select_func.btAlgrithm, background='lightskyblue')
suanfaMenu.add_command(label="遗传算法", command=select_func.ycAlgrithm, background='pink')
shujuMenu.add_command(label="选择文件", command=openfile, background='lightskyblue')
pictureMenu.add_command(label="散点图", command=select_func.sdAlgrithm, background='pink')
pictureMenu.add_command(label="柱状图", command=select_func.zzAlgrithm, background='lightskyblue')
sortMenu.add_command(label="递增排序", command=select_func.dzAlgrithm, background='pink')
sortMenu.add_command(label="递减排序", command=select_func.djAlgrithm, background='lightskyblue')
logMenu.add_command(label="算法日志", command=select_func.logAlgrithm, background='pink')

tabBar = Notebook(master=root)
root.configure(menu=menuBar)


# 加载图片
canvas = tkinter.Canvas(root, width=500, height=300, bg=None)
image_file = tkinter.PhotoImage(file="./src/picture/2.gif")
image = canvas.create_image(250, 0, anchor='n', image=image_file)
canvas.pack()

# 显示窗口
root.mainloop()
