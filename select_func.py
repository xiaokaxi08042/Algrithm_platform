import DP
import Greedy
import backtrack
import follow_root


# 动态规划算法
def dpAlgrithm():
    choice = 1
    a_name = '动态规划算法'
    follow_root.in_main(a_name,choice)


# 贪心算法
def gdAlgrithm():
    choice = 2
    a_name = '贪心算法'
    follow_root.in_main(a_name, choice)


# 回溯算法
def btAlgrithm():
    choice = 3
    a_name = '回溯算法'
    follow_root.in_main(a_name, choice)


# 遗传算法
def ycAlgrithm():
    choice = 4
    a_name = '遗传算法'
    follow_root.in_main(a_name, choice)


# 绘制散点图
def sdAlgrithm():
    choice = 5
    a_name = '绘制散点图'
    follow_root.in_main2(a_name, choice)


# 绘制柱状图
def zzAlgrithm():
    choice = 6
    a_name = '绘制柱状图'
    follow_root.in_main2(a_name, choice)


# 递增排序
def dzAlgrithm():
    choice = 7
    a_name = '递增排序'
    follow_root.in_main3(a_name, choice)


# 递减排序
def djAlgrithm():
    choice = 8
    a_name = '递减排序'
    follow_root.in_main3(a_name, choice)


# 日志记录
def logAlgrithm():
    choice = 9
    a_name = '日志记录'
    follow_root.in_main3(a_name, choice)
