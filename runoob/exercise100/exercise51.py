# http://www.runoob.com/python/python-exercise-example51.html


# 题目：学习使用按位与 & 。


print(2 & 5)

a = 0x77
b = a & 3
print('a & b = %d' % b)
b &= 7
print('a & b = %d' % b)

c = 12 & 8
d = 12 | 8
print(c)
print(d)

a = 0x10
b = 0x11
print(a|b)
print(a&b)