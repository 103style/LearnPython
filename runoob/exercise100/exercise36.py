# http://www.runoob.com/python/python-exercise-example36.html

# 题目：求100之内的素数。


L = []
for x in range(2,100):
    temp = int(x / 2)
    for y in range(2,temp):
        if x % y == 0:
            break

        if y + 1 == temp:
            L.append(x)

print("100以内共有%d个素数，分别是：" %len(L))
print(L)
