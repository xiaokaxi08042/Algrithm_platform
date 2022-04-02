import search
import time


def Greedy(s):
    last_time = time.time()
    c, n, w, v = search.table_data(s)
    x = []
    y = []
    y1 = []
    print("背包容量：", c, "物品个数：", n)
    print("重量:", w)
    print("价值:", v)
    vw(c, n, w, v, x, y, y1)
    weight = 0
    value = 0
    for i in range(n):
        if w[y[i]-1] + weight < c:
            value += v[y[i]-1]
            weight += w[y[i]-1]
            y1[y[i]-1] = 1
        else:
            y1[y[i]-1] = 0
    print("最大价值为：", value)
    file_handle = open('result.txt', mode='a')
    file_handle.write('贪心法\n')
    file_handle.write(s)
    file_handle.write('  最大值：')
    file_handle.write(str(value))
    print("解向量为：", y1)
    current_time = time.time()
    stime = str(current_time - last_time)
    print("耗时： {}".format(current_time - last_time))
    file_handle.write('  解向量：[')
    for i in y1:
        file_handle.write(str(i))
        file_handle.write(',')
    file_handle.write(']   耗时：')
    file_handle.write(str(current_time - last_time))
    file_handle.write('\n')
    file_handle.close()
    return c, n, w, v, stime, y1, value


def vw(c, n, w, v, x, y, y1):
    for i in range(n):
        x.append(v[i]/w[i])
        y.append(i+1)
        y1.append(0)
    sort(x,y)
    print('递减排序：', y)


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
