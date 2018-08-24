# http://www.runoob.com/python/python-exercise-example74.html


# 题目：列表排序及连接。


import random

res = []
temp = []
# 查看函数描述
help(random.uniform)
for x in range(5):
    res.append(random.uniform(0, 100))
    temp.append(random.uniform(0, 100))

print("res = ", res)
print("temp = ", temp)
#  排序
res.sort()
print("res排序之后", res)


#  连接
print(res + temp)
print(res.extend(temp))