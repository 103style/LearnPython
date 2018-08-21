# http://www.runoob.com/python/python-exercise-example49.html

# 题目：使用lambda来创建匿名函数。

MAX = lambda x, y: (x > y) * x + (x < y) * y
MIN = lambda x, y: (x > y) * y + (x < y) * x

a = 10
b = 20
print('The largar one is %d' % MAX(a, b))

print('The lower one is %d' % MIN(a, b))

SUM = lambda x, y: x + y
print(SUM(10, 5))

DOUBLE = lambda x: x % 2 == 0

print(DOUBLE(10))
