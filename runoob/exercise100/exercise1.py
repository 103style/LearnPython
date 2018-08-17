# http://www.runoob.com/python/python-exercise-example1.html

# 题目：有四个数字：1、2、3、4，
# 能组成多少个互不相同且无重复数字的三位数？各是多少？
L = []
for x in range(1, 5):
    for y in range(1, 5):
        for z in range(1, 5):
            if (x == y or y == z or x == z):
                continue
            else:
                L.append(100 * x + 10 * y + z)
print(len(L))
print(L)

# -*- coding: UTF-8 -*-
t = 0
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if (i != k) and (i != j) and (j != k):
                print(i, j, k)
                t += 1
print(t)
