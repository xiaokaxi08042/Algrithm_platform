import DP
import search
import Greedy
import tkinter
import backtrack
import tkinter as tk            # 导入GUI界面函数库
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from PIL import Image, ImageTk  # 导入图像处理函数库
from draw_picture import scatter, barh

# 1.算法
def in_main(a_name, choice):

    def go(*args):  # 处理事件，*args表示可变参数
        s = comboxlist.get()
        if choice==1:
            c, n, w, v, stime, y1, maxvalue = DP.Dp(s)
        elif choice == 2:
            c, n, w, v, stime, y1, maxvalue = Greedy.Greedy(s)
        elif choice == 3:
            c, n, w, v, stime, y1, maxvalue = backtrack.Bt(s)
        elif choice == 4:
            print('lll')


        # 显示文本框
        tab = Frame(master=tabBar)
        tabBar.add(tab, text=s)
        textContainer = Labelframe(tab)
        textContainer.pack(expand=YES, fill=BOTH)
        tabBar.pack(expand=YES, fill=BOTH)
        textArea = tkinter.Text(master=textContainer)
        textArea.pack(side=LEFT, expand=YES, fill=BOTH)

        textArea.insert(INSERT, '\n背包容量：' + str(c) + '\n物品个数：' + str(n))
        textArea.insert(INSERT, '\n最大价值：'+str(maxvalue))
        textArea.insert(INSERT, "\n耗时：" + stime + 's')
        textArea.insert(INSERT, '\n重量       价值      解向量\n')
        for i in range(len(w)):
            textArea.insert(INSERT, str(w[i]) + '         ' + str(v[i]) + '           ' + str(y1[i]) + '\n')

    win = tkinter.Tk()  # 构造窗体
    win.geometry('500x400')
    win.title(a_name)
    comvalue = tkinter.StringVar()  # 窗体自带的文本，新建一个值
    comboxlist = ttk.Combobox(win, textvariable=comvalue)  # 初始化
    comboxlist["values"] = search.sqlite_read()
    # comboxlist.current(0)  # 选择第一个
    comboxlist.bind("<<ComboboxSelected>>", go)  # 绑定事件,(下拉列表框被选中时，绑定go()函数)
    comboxlist.pack()
    # 显示文本框
    tabBar = Notebook(master=win)
    tab = Frame(master=tabBar)
    # tabBar.add(tab, text=s)
    textContainer = Labelframe(tab)
    textContainer.pack(expand=YES, fill=BOTH)
    tabBar.pack(expand=YES, fill=BOTH)
    textArea = tkinter.Text(master=textContainer)
    textArea.pack(side=LEFT, expand=YES, fill=BOTH)

    win.mainloop()  # 进入消息循环


# 2.绘图
def in_main2(a_name, choice):
    win = tk.Tk()  # 构造窗体
    win.geometry('500x400')
    win.title(a_name)
    global img_png, s  # 定义全局变量 图像的
    # var = tk.StringVar()

    def go(*args):
        s = comboxlist.get()
        if choice == 5:
            scatter(s)
        elif choice == 6:
            barh(s)

    def Open_Img():
        global img_png
        # s = comboxlist.get()
        Img = Image.open('./picture/'+ s +'.png')
        img_png = ImageTk.PhotoImage(Img)

    def Show_Img():
        global img_png
        label_Img = tk.Label(win, image=img_png)
        label_Img.pack()


    comvalue = tkinter.StringVar()  # 窗体自带的文本，新建一个值
    comboxlist = ttk.Combobox(win, textvariable=comvalue)  # 初始化
    comboxlist["values"] = search.sqlite_read()
    # comboxlist.current(0)  # 选择第一个
    comboxlist.bind("<<ComboboxSelected>>", go)  # 绑定事件,(下拉列表框被选中时，绑定go()函数)
    comboxlist.pack()
    # 创建打开图像按钮
    btn_Open = tk.Button(win,
                         text='打开图像',  # 显示在按钮上的文字
                         width=15, height=2,
                         command=Open_Img)  # 点击按钮式执行的命令
    btn_Open.pack()  # 按钮位置
    # 创建显示图像按钮
    btn_Show = tk.Button(win,
                         text='显示图像',  # 显示在按钮上的文字
                         width=15, height=2,
                         command=Show_Img)  # 点击按钮式执行的命令
    btn_Show.pack()  # 按钮位置
    win.mainloop()  # 进入消息循环


# 显示日志记录
def in_main3(a_name, choice):
    # 构造窗体
    win = tkinter.Tk()
    win.geometry('500x400')
    win.title(a_name)
    # 构造文本框
    text = tk.Text(win)
    text.pack(side=LEFT, expand=YES, fill=BOTH)

    # "insert" 索引表示插入光标当前的位置
    text.insert("insert", "I love ")
    text.insert("end", "Python.com!")
    win.mainloop()