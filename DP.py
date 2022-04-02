import time
import search


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
    maxvalue = value[i][j]
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
    return stime, y1, maxvalue


def Dp(s):
    last_time = time.time()
    c, n, w, v = search.table_data(s)
    print("背包容量：", c, "物品个数：", n)
    print("重量:", w)
    print("价值:", v)
    stime, y1, maxvalue = bag(n, c, w, v, s, last_time)
    return c, n, w, v, stime, y1, maxvalue






