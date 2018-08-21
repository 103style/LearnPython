# http://www.runoob.com/python/python-exercise-example37.html

# 题目：对10个数进行排序。

print("请依次输入十个数")

L = []
for x in range(0, 10):
    L.append(int(input("请输入第%d个数：" % (x + 1))))

S = L[:]

L.sort()
print(L)

print(S)
for x in range(0,10):
    for y in range(0, 10):
        if S[x] < S[y]:
            temp = S[x]
            S[x] = S[y]
            S[y] = temp

print(S)


