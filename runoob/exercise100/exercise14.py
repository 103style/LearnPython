# http://www.runoob.com/python/python-exercise-example14.html

# 题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。

def slices(num):
    x = 2
    temp = num
    L = []
    while (x < num):
        if num % x == 0:
            L.append(x)
            x = 2
            num = int(num / x)
        else:
            x += 1

    if len(L) == 0:
        L.append(1)

    if num != 1:
        L.append(num)

    return L


T = 144
L = slices(T)
L.sort()
print("%d = " % T, end='')
for x in range(0, len(L)):
    if x + 1 == len(L):
        print(L[x], end='')
    else:
        print("%d * " % L[x], end='')
print()
