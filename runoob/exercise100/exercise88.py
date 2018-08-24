# http://www.runoob.com/python/python-exercise-example88.html

# 题目：读取7个数（1—50）的整数值，每读取一个值，程序打印出该值个数的＊。

import random

index = 0
while index < 7:
    temp = int(random.uniform(1, 50))
    print(temp)
    for x in range(temp):
        print('＊', end='')
    print()
    index += 1
