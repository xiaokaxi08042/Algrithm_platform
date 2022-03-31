import time
bestV = 0
curW = 0
curV = 0
bestx = None


def zhi(s):
    last_time = time.time()
    daten = open(s, "r")
    # s = str(input(""))
    lines = daten.readlines()
    list = []

    for i in lines:
        list.append(i.strip().split(' '))
    daten.close()
    f = []
    w = []
    v = []
    y1 = []
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
    x = [0 for i in range(n)]
    # print(x)
    print("重量:", w)
    print("价值:", v)
    vw(c, n, w, v, y1, y)
    # bestV = 0
    backtrack(0, w, v, n, c, x)
    print("最大价值为：", bestV)
    file_handle = open('result.txt', mode='a')
    file_handle.write('回溯法\n')
    file_handle.write(s)
    file_handle.write('  最大值：')
    file_handle.write(str(bestV))
    print("解向量为：", bestx)
    current_time = time.time()
    print("耗时： {}".format(current_time - last_time))
    file_handle.write('  解向量：[')
    for i in bestx:
        file_handle.write(str(i))
        file_handle.write(',')
    file_handle.write(']   耗时：')
    file_handle.write(str(current_time - last_time))
    file_handle.write('\n')
    file_handle.close()
    x = [0 for i in range(n)]

def vw(c, n, w, v, y1, y):
    for i in range(n):
        y1.append(v[i]/w[i])
        y.append(i+1)
    sort(y1, y)
    print("按单位价值排序得：", y)


def sort(x, y):
    for i in range(len(x)):
        for m in range(i):
            if x[i] > x[m]:
                t = x[i]
                x[i] = x[m]
                x[m] = t
                t = y[i]
                y[i] = y[m]
                y[m] = t


def backtrack(i, w, v, n, c, x):
    global bestV, curW, curV, bestx
    if i >= n:
        if bestV < curV:
            bestV = curV
            bestx = x[:]
    else:
        if curW+w[i] <= c:
            x[i] = 1
            curW += w[i]
            curV += v[i]
            backtrack(i+1, w, v, n, c, x)
            curW -= w[i]
            curV -= v[i]
        x[i] = 0
        backtrack(i+1, w, v, n, c, x)

def in_main():
    print("       ----------------回溯法----------------")
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
            case 10:print("退出回溯法!")


