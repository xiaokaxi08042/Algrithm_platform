import time

import search

bestV = 0
curW = 0
curV = 0
bestx = None


# 读入数据库内容和结果存入
def Bt(s):
    last_time = time.time()
    c, n, w, v = search.table_data(s)
    print("背包容量：", c, "物品个数：", n)
    x = [0 for i in range(n)]
    # print(x)
    print("重量:", w)
    print("价值:", v)
    backtrack(0, w, v, n, c, x)
    print("最大价值为：", bestV)
    file_handle = open('result.txt', mode='a')
    file_handle.write('回溯法\n')
    file_handle.write(s)
    file_handle.write('  最大值：')
    file_handle.write(str(bestV))
    print("解向量为：", bestX)
    current_time = time.time()
    print("耗时： {}".format(current_time - last_time))
    file_handle.write('  解向量：[')
    for i in bestX:
        file_handle.write(str(i))
        file_handle.write(',')

    file_handle.write(']   耗时：')
    file_handle.write(str(current_time - last_time))
    stime = str(current_time - last_time)
    file_handle.write('\n')
    file_handle.close()
    # x = [0 for i in range(n)]
    return c, n, w, v, stime, bestX, bestV


# 回溯算法主要代码
def backtrack(i, w, v, n, c, x):
    global bestV, curW, curV, bestX
    if i >= n:
        if bestV < curV:
            bestV = curV
            bestX = x[:]
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



