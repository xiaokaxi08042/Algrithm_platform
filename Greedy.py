import time


def Greedy(s):
    last_time = time.time()
    daten = open(s, "r")
    lines = daten.readlines()
    list = []
    for i in lines:
        list.append(i.strip().split(' '))
    daten.close()
    f = []
    w = []
    v = []
    x = []
    y = []
    z = []
    for i in list:
        for b in i:
            f.append(b)
    # print(f)
    for i in range(len(f)):
        if i == 0:
            c = int(f[i])
        elif i == 1:
            n = int(f[i])
            # print(n)
        elif i > 1 and i % 2 == 0:
            w.append(int(f[i]))
        else:
            v.append(int(f[i]))
    print("背包容量：", c, "物品个数：", n)
    print("重量:", w)
    print("价值:", v)
    vw(c, n, w, v, x, y, z)
    weight = 0
    value = 0
    for i in range(n):
        if w[y[i]-1] + weight < c:
            value += v[y[i]-1]
            weight += w[y[i]-1]
            z[y[i]-1] = 1
        else:
            z[y[i]-1] = 0
    print("最大价值为：", value)
    file_handle = open('result.txt', mode='a')
    file_handle.write('贪心法\n')
    file_handle.write(s)
    file_handle.write('  最大值：')
    file_handle.write(str(value))
    print("解向量为：", z)
    current_time = time.time()
    print("耗时： {}".format(current_time - last_time))
    file_handle.write('  解向量：[')
    for i in z:
        file_handle.write(str(i))
        file_handle.write(',')
    file_handle.write(']   耗时：')
    file_handle.write(str(current_time - last_time))
    file_handle.write('\n')
    file_handle.close()


def vw(c,n,w,v,x,y,z):
    for i in range(n):
        x.append(v[i]/w[i])
        y.append(i+1)
        z.append(0)
    # print(x,y)
    sort(x,y)
    print("按单位价值排序得：", y)


def sort(x,y):
    for i in range(len(x)):
        for m in range(i):
            if x[i] > x[m]:
                t = x[i]
                x[i] = x[m]
                x[m] = t
                t = y[i]
                y[i] = y[m]
                y[m] = t


def in_main():
    print("       ----------------贪心法----------------")
    print("       |                                   |")
    print("       |   可输入数字0-9选择文件               |")
    print("       |                                   |")
    print("       |   10退出系统                        |")
    print("       |                                   |")
    print("       -------------------------------------")
    num = 0
    s = " "
    while num != 10:
        num = int(input("选择文件:"))
        match num:
            case 0: Greedy("data/beibao0.in")
            case 1: Greedy("data/beibao1.in")
            case 2: Greedy("data/beibao2.in")
            case 3: Greedy("data/beibao3.in")
            case 4: Greedy("data/beibao4.in")
            case 5: Greedy("data/beibao5.in")
            case 6: Greedy("data/beibao6.in")
            case 7: Greedy("data/beibao7.in")
            case 8: Greedy("data/beibao8.in")
            case 9: Greedy("data/beibao9.in")
            case 10:print("退出贪心法!")
