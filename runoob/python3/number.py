# http://www.runoob.com/python3/python3-number.html

#  数值类型

# Python 数字数据类型用于存储数值。
# 数据类型是不允许改变的,这就意味着如果改变数字数据类型的值，将重新分配内存空间。

a = 1
b = 2
c = 3
del a
del b, c

# 整型(Int)
# 浮点型(float)
# 复数( (complex))  可以用a + bj,或者complex(a,b)表示， 复数的实部a和虚部b都是浮点型。

print("0x12 = ", 0x12)
print("0o12 = ", 0o12)
print(complex(1, 2))
print()

# Python 数字类型转换
#
# int(x) 将x转换为一个整数。
# float(x) 将x转换到一个浮点数。
# complex(x) 将x转换到一个复数，实数部分为 x，虚数部分为 0。
# complex(x, y) 将 x 和 y 转换到一个复数，实数部分为 x，虚数部分为 y。x 和 y 是数字表达式。
a = 5
b = 3
c = 1.2
print("a = %d, b = %d, c = %s" % (a, b, c))
print(complex(a, b))

print("a/b = ", a / b)
print("a//v = ", a // b)
print("a//c = ", a // c)
# 除法 / 总是返回一个浮点数，如果只想得到整数的结果，丢弃可能的分数部分，可以使用运算符 // ：
# // 得到的并不一定是整数类型的数，它与分母分子的数据类型有关系。
# 使用 ** 操作来进行幂运算：
print("a ** b = ", a ** b)
print()

import math

# 数学函数
# abs(x)	           返回数字的绝对值，如abs(-10) 返回 10
# ceil(x)	           返回数字的上入整数，如math.ceil(4.1) 返回 5
print("math.ceil(5.2) = ", math.ceil(5.2))
# cmp(x, y)            如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1。 Python 3 已废弃 。使用 使用 (x>y)-(x<y) 替换。
# exp(x)	           返回e的x次幂(ex),如math.exp(1) 返回2.718281828459045
print("math.exp(1) = ", math.exp(1))
# fabs(x)	           返回数字的绝对值，如math.fabs(-10) 返回10.0
print("math.fabs(1.5) = ", math.fabs(1.5))
# floor(x)             返回数字的下舍整数，如math.floor(4.9)返回 4
print("math.floor(1.5) = ", math.floor(1.5))
# log(x)	           如math.log(math.e)返回1.0,math.log(100,10)返回2.0
print("math.log(32,2) = ", math.log(32, 2))
# log10(x)             返回以10为基数的x的对数，如math.log10(100)返回 2.0
print("math.log10(1000) = ", math.log10(1000))
# max(x1, x2,...)	   返回给定参数的最大值，参数可以为序列。
# min(x1, x2,...)	   返回给定参数的最小值，参数可以为序列。
# modf(x)	           返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示。
print("math.modf(3.14) = ", math.modf(3.14))
# pow(x, y)            x**y 运算后的值。
print("math.pow(2,5) = ", math.pow(2, 5))
# round(x [,n])	       返回浮点数x的四舍五入值，如给出n值，则代表舍入到小数点后的位数。
print("round(5.27455,2) = ", round(5.27455, 2))
print("round(5.27455,3) = ", round(5.27455, 3))
print("round(5.27455,4) = ", round(5.27455, 4))
print("round(5.27456,4) = ", round(5.27456, 4))
# sqrt(x)	           返回数字x的平方根。
print("math.sqrt(9) = ", math.sqrt(9))
print()

# 随机数函数
import random

# choice(seq)  	  从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。
print("random.choice(range(10)) = ", random.choice(range(10)))
# randrange       ([start,] stop [,step])	从指定范围内，按指定基数递增的集合中获取一个随机数，基数缺省值为1
print("random.randrange(2, 5)) = ", random.randrange(2, 5))
# random()   	  随机生成下一个实数，它在[0,1)范围内。
print("random.random()) = ", random.random())
# seed([x])  	  改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。
# shuffle(lst)	  将序列的所有元素随机排序
list = [1,2,3,4,5,6]
random.shuffle(list)
print(list)
# uniform(x, y)	  随机生成下一个实数，它在[x,y]范围内。
print(random.uniform(1,3))
