# http://www.runoob.com/python/python-exercise-example44.html

# 两个 3 行 3 列的矩阵，实现其对应位置的数据相加，并返回一个新矩阵：
#
# X = [[12,7,3],
#     [4 ,5,6],
#     [7 ,8,9]]
#
# Y = [[5,8,1],
#     [6,7,3],
#     [4,5,9]]


X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]


c = len(X[0])
r = len(X)

res=[]
for x in range(0,r):
    temp = []
    for y in range(0, c):
        temp.append(X[x][y] + Y[x][y])
    res.append(temp)

print(res)

