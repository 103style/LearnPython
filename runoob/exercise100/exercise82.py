# http://www.runoob.com/python/python-exercise-example82.html

# 题目：八进制转换为十进制

import math

n = 0
p = input('input a octal number:\n')
index = 1
for x in p:
    n = n + int(x) * math.pow(8, len(p) - index)
    index += 1

print(int(n))
