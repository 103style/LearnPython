# http://www.runoob.com/python/python-exercise-example31.html

# 题目：请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。

# -*- coding:utf-8 -*-

W = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

l = input("请输入第一个字母：")

res = []
for x in W:
    if l == x[0]:
        res.append(x)

print(res)
if len(res) == 1:
    print(res[0])
else:
    l = input("请输入第二个字母:")
    for x in res:
        if l == x[1]:
            print(x)