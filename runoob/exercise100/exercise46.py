# http://www.runoob.com/python/python-exercise-example46.html

# 题目：求输入数字的平方，如果平方运算后小于 50 则退出。

import math

while True:
    num = int(input("请输出一个数字："))
    res = math.pow(num, 2)
    if res >= 50:
        print(res)
        break
    else:
        print("%d的平方小于50，请重试" %num)
