# http://www.runoob.com/python/python-exercise-example69.html

# 题目：有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，问最后留下的是原来第几号的那位。

n = int(input("请输入一共多少个人："))

res = []

for x in range(1, n + 1):
    res.append(x)

temp = []

count = 1
while len(temp) != 1:
    for x in range(len(res)):
        if count % 3 != 0:
            temp.append(res[x])
        count += 1
    res = temp[:]
    if len(temp) == 1:
        break
    else:
        temp = []

print(temp)
