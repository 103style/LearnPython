# http://www.runoob.com/python/python-exercise-example5.html

# 题目：输入三个整数x,y,z，请把这三个数由小到大输出。

L = []
for x in range(0,3):
    x = int(input("integer:"))
    L.append(x)
L.sort()
print(L)