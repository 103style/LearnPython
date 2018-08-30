# http://www.runoob.com/python3/python3-basic-operators.html

# Python算术运算符

print("算术运算符相关:")
a = 21
b = 10
print("a = %d, b = %d" % (a, b))
c = a + b
print("a + b 的值为：", c)

c = a - b
print("a - b 的值为：", c)

c = a * b
print("a * b 的值为：", c)

c = a / b
print("a / b 的值为：", c)

c = a % b
print("a % b 的值为：", c)

# 修改变量 a 、b 、c
a = 2
b = 3
print("a = %d, b = %d" % (a, b))
c = a ** b
print("a ** b 的值为：", c)
a = 10
b = 5
c = a // b
print("a // b 的值为：", c)
print("8.2 // 4.0 的值为：", 8.2 // 4.0)
print()


# Python比较运算符
print("比较运算符相关:")
a = 21
b = 10
print("a = %d, b = %d" % (a, b))
c = 0
if (a == b):
    print("a 等于 b")
else:
    print("不等于 b")

if (a != b):
    print("a 不等于 b")
else:
    print("a 等于 b")

if (a < b):
    print("a 小于 b")
else:
    print("a 大于等于 b")

if (a > b):
    print("a 大于 b")
else:
    print("a 小于等于 b")

# 修改变量 a 和 b 的值
a = 5
b = 20
print("a = %d, b = %d" % (a, b))
if (a <= b):
    print("a 小于等于 b")
else:
    print("a 大于  b")

if (b >= a):
    print("b 大于等于 a")
else:
    print("b 小于 a")
print()


print("赋值运算符相关:")
a = 21
b = 10
print("a = %d, b = %d" % (a, b))
c = a + b
print("c = a + b 的值为：", c)

c += a
print("减法赋值运算符 c += a 的值为：", c)

c *= a
print("乘法赋值运算符 c *= a 的值为：", c)

c /= a
print("除法赋值运算符 c /= a 的值为：", c)

c = 2
print('c = ', c)
c %= a
print("取模赋值运算符 c %= a 的值为：", c)

c **= a
print("幂赋值运算符  c **= a 的值为：", c)

c //= a
print("取整除赋值运算符 c //= a 的值为：", c)
print()

print("逻辑运算符相关:")
a = 10
b = 20
print("a = %d, b = %d" % (a, b))

if (a and b):
    print("变量 a 和 b 都为 true")
else:
    print("变量 a 和 b 有一个不为 true")

if (a or b):
    print("变量 a 和 b 都为 true，或其中一个变量为 true")
else:
    print("变量 a 和 b 都不为 true")

# 修改变量 a 的值
a = 0
print("a = %d, b = %d" % (a, b))
if (a and b):
    print("变量 a 和 b 都为 true")
else:
    print("变量 a 和 b 有一个不为 true")

if (a or b):
    print("变量 a 和 b 都为 true，或其中一个变量为 true")
else:
    print("变量 a 和 b 都不为 true")

if not (a and b):
    print("变量 a 和 b 都为 false，或其中一个变量为 false")
else:
    print("变量 a 和 b 都为 true")
print()

# 除了以上的一些运算符之外，Python还支持成员运算符，测试实例中包含了一系列的成员，包括字符串，列表或元组。
print("成员运算符相关:")
# in	      如果在指定的序列中找到值返回 True，否则返回 False。	         x 在 y 序列中 , 如果 x 在 y 序列中返回 True。
# not i       如果在指定的序列中没有找到值返回 True，否则返回 False。	     x 不在 y 序列中 , 如果 x 不在 y 序列中返回 True。

a = 10
b = 20
print("a = %d, b = %d" % (a, b))
list = [1, 2, 3, 4, 5]
print("list = ", list)
if (a in list):
    print("变量 a 在给定的列表中 list 中")
else:
    print("变量 a 不在给定的列表中 list 中")

if (b not in list):
    print("变量 b 不在给定的列表中 list 中")
else:
    print("变量 b 在给定的列表中 list 中")

# 修改变量 a 的值
a = 2
print("a = %d, b = %d" % (a, b))
if (a in list):
    print("变量 a 在给定的列表中 list 中")
else:
    print("变量 a 不在给定的列表中 list 中")
print()

# 身份运算符用于比较两个对象的存储单元
print("身份运算符相关:")
# is	     is 是判断两个标识符是不是引用自一个对象	      x is y, 类似 id(x) == id(y) , 如果引用的是同一个对象则返回 True，否则返回 False
# is not	 is not 是判断两个标识符是不是引用自不同对象	  x is not y ， 类似 id(a) != id(b)。如果引用的不是同一个对象则返回结果 True，否则返回 False。
# id() 函数用于获取对象内存地址。
a = 20
b = 20
print("a = %d, b = %d" % (a, b))
if (a is b):
    print("a 和 b 有相同的标识")
else:
    print("a 和 b 没有相同的标识")

if (id(a) == id(b)):
    print("a 和 b 有相同的标识")
else:
    print("a 和 b 没有相同的标识")

# 修改变量 b 的值
b = 30
print("a = %d, b = %d" % (a, b))
if (a is b):
    print("a 和 b 有相同的标识")
else:
    print("a 和 b 没有相同的标识")

if (a is not b):
    print("a 和 b 没有相同的标识")
else:
    print("a 和 b 有相同的标识")
print()

