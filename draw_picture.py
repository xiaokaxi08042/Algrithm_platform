import sqlite3
import numpy as np
import matplotlib.pyplot as plt

from search import table_data


def scatter(s):
    # s = 'beibao0.in'
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    # matplotlib画图中中文显示会有问题，需要这两行设置默认字体

    plt.xlabel('重量')
    plt.ylabel('价值')
    plt.xlim(xmax=200, xmin=0)
    plt.ylim(ymax=150, ymin=0)
    c,n,w,v = table_data(s)
    colors = 'blue'  #  点的颜色
    area = np.pi * 3**2 # 点面积
    # for i in range(len(w)):
    plt.scatter(w, v, s=area, c=colors, alpha=0.1, label=' ')
    plt.legend()
    plt.yticks(())
    plt.title('散点图')
    plt.savefig('./picture/'+ s +'.png')  # 保存图片
    plt.show()


def barh(s):
    fig, ax = plt.subplots()
    c, n, w, v = table_data(s)
    y=[]
    print(w,v)
    for i in range(len(w)):
        y.append(v[i]/w[i])
    # print(y)
    y_pos = np.arange(len(w)) + 1
    ax.barh(y_pos, y, color='b', align="center")
    plt.savefig('./picture/'+ s +'.png')  # 保存图片
    plt.show()
