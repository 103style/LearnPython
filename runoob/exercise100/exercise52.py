# http://www.runoob.com/python/python-exercise-example52.html

# 题目：学习使用按位或 | 。

# 0|0=0; 0|1=1; 1|0=1; 1|1=1

a = 0x77
b = a | 3
print('a | b is %d' % b)
b |= 7
print('a | b is %d' % b)

print( 0x002 | 0x010)