# http://www.runoob.com/python/python-exercise-example29.html

# 题目：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。

import math


def getNumCountAndPrint(num):
    if num > 99999 or num <= 0:
        return '请给一个不多于5位的正整数'

    count = str(num).__len__()
    print("num是%d位数" % count)
    for x in range(0, count):
        if x + 1 != count:
            print("%d  " % (int(num / math.pow(10, x))% 10) , end='')
        else:
            print("%d  " % (int(num / math.pow(10, x))), end='')


num = int(input("请输出一个不多于5位的正整数："))

getNumCountAndPrint(num)
