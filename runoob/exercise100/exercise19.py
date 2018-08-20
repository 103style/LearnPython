# http://www.runoob.com/python/python-exercise-example19.html

# 题目：一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。

# from sys import stdout
#
# for j in range(2, 1001):
#     k = []
#     n = -1
#     s = j
#     for i in range(1, j):
#         if j % i == 0:
#             n += 1
#             s -= i
#             k.append(i)
#
#     if s == 0:
#         print(j)
#         for i in range(n):
#             stdout.write(str(k[i]))
#             stdout.write(' ')
#         print(k[n])

for x in range(2, 1000):
    s = []
    for y in range(1, x):
        if x % y == 0:
            s.append(y)
    num = 0
    for t in s:
        num += t
    if num == x:
        print(num)
        for t in s:
            print("%d  " % t, end='')
        print()

