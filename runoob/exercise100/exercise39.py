# http://www.runoob.com/python/python-exercise-example39.html

# 题目：有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。

L = []
for x in range(0, 10):
    L.append(x)

i = int(input("请输入要插入的数："))

d = True

if L[1] < L[0]:
    d = False

L.append(i)

res = []

if d:
    L.sort()
    print(L)
else:
    L.sort()
    res = L[::-1]
    print(res)