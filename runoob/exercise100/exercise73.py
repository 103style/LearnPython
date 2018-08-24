# http://www.runoob.com/python/python-exercise-example73.html

# 题目：反向输出一个链表。

temp = []

for x in range(10):
    temp.append(x)
print(temp)

res = temp[::-1]
print(res)