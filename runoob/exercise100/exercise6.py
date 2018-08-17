# http://www.runoob.com/python/python-exercise-example6.html

# 题目：斐波那契数列。

def fibonacci(n):
    L = []
    if n < 2:
        L = [1]
    elif n < 3:
        L = [1, 1]
    else:
        L = [1,1]
        for x in range(0,n -2):
            L.append(L[-1] + L[-2])

    return L

print(fibonacci(1))
print(fibonacci(3))
print(fibonacci(5))
print(fibonacci(20))