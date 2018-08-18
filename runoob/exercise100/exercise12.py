# http://www.runoob.com/python/python-exercise-example12.html

# 题目：判断101-200之间有多少个素数，并输出所有素数。

# 判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数。 　　

import math

res = []

for x in range(101, 200 + 1):
    temp = int(math.sqrt(x) + 1)
    for y in range(2, temp):
        if x % y == 0:
            break
        if y + 1 == temp:
            res.append(x)
print(res)

print(len(res))