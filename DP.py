import time

def bag(n, c, w, v, s, last_time):
    # 置零，表示初始状态
    value = [[0 for j in range(c + 1)] for i in range(n + 1)]
    for i in range(1, n+1):
        for j in range(1, c+1):
            value[i][j] = value[i - 1][j]
            # 背包总容量够放当前物体，遍历前一个状态考虑是否置换
            if j >= w[i - 1] and value[i][j] < value[i - 1][j - w[i - 1]] + v[i - 1]:
                value[i][j] = value[i - 1][j - w[i - 1]] + v[i - 1]
    print("最大价值为：", value[i][j])
    file_handle = open('result.txt', mode='a')
    file_handle.write('动态规划法\n')
    file_handle.write(s)
    file_handle.write('  最大值：')
    file_handle.write(str(value[i][j]))
    j = c
    i = n
    y1 = [0 for i in range(1, n+1)]
    while i != 0:
        if value[i][j] > value[i-1][j]:
            y1[i-1] = 1
            j = j-w[i-1]
        else:
            y1[i-1] = 0
        i = i-1
    print("解向量为：", y1)
    current_time = time.time()
    print("耗时： {}".format(current_time - last_time))
    file_handle.write('  解向量：[')
    for i in y1:
        file_handle.write(str(i))
        file_handle.write(',')
    file_handle.write(']   耗时：')
    file_handle.write(str(current_time - last_time))
    file_handle.write('\n')
    file_handle.close()

def zhi(s):
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
    vw(c, n, w, v, x, y)
    bag(n, c, w, v,s,last_time)


def vw(c,n,w,v,x,y):
    for i in range(n):
        x.append(v[i]/w[i])
        y.append(i+1)
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
    print("       --------------动态规划法---------------")
    print("       |                                   |")
    print("       |   可输入数字0-9选择文件               |")
    print("       |                                   |")
    print("       |   10.退出系统                       |")
    print("       |                                   |")
    print("       -------------------------------------")
    num = 0
    while num != 10:
        num = int(input("选择文件:"))
        match num:
            case 0: zhi("data/beibao0.in")
            case 1: zhi("data/beibao1.in")
            case 2: zhi("data/beibao2.in")
            case 3: zhi("data/beibao3.in")
            case 4: zhi("data/beibao4.in")
            case 5: zhi("data/beibao5.in")
            case 6: zhi("data/beibao6.in")
            case 7: zhi("data/beibao7.in")
            case 8: zhi("data/beibao8.in")
            case 9: zhi("data/beibao9.in")
            case 10:print("退出动态规划法!")
