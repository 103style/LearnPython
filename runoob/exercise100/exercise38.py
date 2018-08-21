# http://www.runoob.com/python/python-exercise-example38.html

# 题目：求一个3*3矩阵主对角线元素之和。

L = []

t = int(input("请输入矩阵的行数："))

for x in range(1, t + 1):
    temp = []
    for y in range(1, t + 1):
        temp.append(int(input("请输入第%d行第%d列的元素:" % (x, y))))
    L.append(temp)

sum = 0

for x in range(0, t):
    sum += L[x][x]

print(sum)
