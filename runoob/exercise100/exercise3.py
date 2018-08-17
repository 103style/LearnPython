# http://www.runoob.com/python/python-exercise-example3.html

# 题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？

S = {}
for x in range(1, 169):
    S[x * x] = x

R = []

for k in S.keys():
    if k - 168 in S:
        R.append(k - 168 - 100)

print(R)

# 网站答案
# 程序分析：
#
# 假设该数为x。
#
# 1、则：x + 100 = n * n, x + 100 + 168 = m * m
#
# 2、计算等式：m * m - n * n = (m + n)(m - n) = 168
#
# 3、设置： m + n = i，m - n = j，i * j = 168，i和j至少一个是偶数
#
# 4、可得： m = (i + j) / 2， n = (i - j) / 2，i和j要么都是偶数，要么都是奇数。
#
# 5、从3和4推导可知道，i与j均是大于等于2的偶数。
#
# 6、由于i * j = 168， j >= 2，则1 < i < 168 / 2 + 1。
#
# 7、接下来将i的所有数字循环计算即可。
#
# 程序源代码：
#
# 实例(Python2.0 +)
# !/usr/bin/python
# -*- coding: UTF-8 -*-

for i in range(1, 85):
    if 168 % i == 0:
        j = 168 / i;
        if i > j and (i + j) % 2 == 0 and (i - j) % 2 == 0:
            m = (i + j) / 2
            n = (i - j) / 2
            x = n * n - 100
            print(x)
