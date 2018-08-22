# http://www.runoob.com/python/python-exercise-example54.html

# 题目：取一个整数a从右端开始的4〜7位。


print(3 << 4)
print(4 >> 2)


# 程序分析：可以这样考虑：
# (1)先使a右移4位。
# (2)设置一个低4位全为1,其余全为0的数。可用~(~0<<4)
# (3)将上面二者进行&运算。


a = int(input('input a number:\n'))
print(a)
b = a >> 4
print(b)
c = ~(~0 << 4)
print(c)
d = b & c
print('%o\t%o' % (a, d))

# ???