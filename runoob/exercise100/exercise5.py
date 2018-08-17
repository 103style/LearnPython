# http://www.runoob.com/python/python-exercise-example5.html

# 题目：输入三个整数x,y,z，请把这三个数由小到大输出。

L = []
for x in range(0, 3):
    x = int(input("integer:"))
    L.append(x)
L.sort()
print(L)


# 网站 2.X 版本源码
# !/usr/bin/python
# -*- coding: UTF-8 -*-
# l = []
# for i in range(3):
#     x = int(raw_input('integer:\n'))
# l.append(x)
# l.sort()
# print l
