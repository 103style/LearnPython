# http://www.runoob.com/python/python-exercise-example61.html

# 题目：打印出杨辉三角形（要求打印出10行如下图）。　　

res = []

for x in range(10):
    temp = []
    for y in range(10):
        temp.append("")
    res.append(temp)

for x in range(10):
    for y in range(10):
        if x == y or (y == 0):
            res[x][y] = 1
        elif x > 1:
            res[x][y] = res[x - 1][y] + res[x - 1][y - 1]

for x in range(len(res)):
    for y in range(len(res[x])):
        print("%s " % str(res[x][y]), end='')
    print()
