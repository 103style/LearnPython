# http://www.runoob.com/python3/python3-data-type.html

#  基本的数据类型

counter = 100  # 整型变量
miles = 1000.0  # 浮点型变量
name = "runoob"  # 字符串

print(counter)
print(miles)
print(name)

# 多个变量赋值
# Python允许你同时为多个变量赋值。例如：

a = b = c = 1
# 以上实例，创建一个整型对象，值为 1，从后向前赋值，三个变量都指向同一个内存地址。

# 您也可以为多个对象指定多个变量。例如：

a, b, c = 1, 2, "runoob"
# 以上实例，两个整型对象 1 和 2 的分配给变量 a 和 b，字符串对象 "runoob" 分配给变量 c。


# 标准数据类型
# Python3 中有六个标准的数据类型：

# Number（数字）
# String（字符串）
# List（列表）
# Tuple（元组）
# Set（集合）
# Dictionary（字典）
# Python3 的六个标准数据类型中：
#
# 不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
# 可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。


# Number（数字）
# Python3 支持 int、float、bool、complex（复数）。
#
# 在Python 3里，只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
#
# 像大多数语言一样，数值类型的赋值和计算都是很直观的。
#
# 内置的 type() 函数可以用来查询变量所指的对象类型。

a, b, c, d = 20, 5.5, True, 4 + 3j
print(type(a), type(b), type(c), type(d))


# <class 'int'> <class 'float'> <class 'bool'> <class 'complex'>


class A:
    pass


class B(A):
    pass


print(isinstance(A(), A))  # returns True
print(type(A()) == A)  # returns True
print(isinstance(B(), A))  # returns True
print(type(B()) == A)  # returns False

# isinstance 和 type 的区别在于：1
#
# type()不会认为子类是一种父类类型。
# isinstance()会认为子类是一种父类类型。

# 注意：在 Python2 中是没有布尔型的，它用数字 0 表示 False，用 1 表示 True。
# 到 Python3 中，把 True 和 False 定义成关键字了，但它们的值还是 1 和 0，它们可以和数字相加。

print(True + 2)
print(False + 2)

# 当你指定一个值时，Number 对象就会被创建：
print("创建删除对象相关：")
var1 = 1
var2 = 10
var3 = 10
varN = 10

# 您也可以使用del语句删除一些对象引用。
# del语句的语法是：
# del var1[var1, var2[var3[....varN]]]


# 您可以通过使用del语句删除单个或多个对象。例如：
del var1
del var2, var3
print()
#  数值运算
# 1、Python可以同时为多个变量赋值，如a, b = 1, 2。
# 2、一个变量可以通过赋值指向不同类型的对象。
# 3、数值的除法包含两个运算符：/ 返回一个浮点数，// 返回一个整数。
# 4、在混合计算时，Python会把整型转换成为浮点数。
print("数值运算相关：")
print("7/3 = ", 7 / 3)
print("7//3 = ", 7 // 3)

# String（字符串）
# Python中的字符串用单引号 ' 或双引号 " 括起来，同时使用反斜杠 \ 转义特殊字符。

print()
# List（列表）
# List（列表） 是 Python 中使用最频繁的数据类型。
#
# 列表可以完成大多数集合类的数据结构实现。列表中元素的类型可以不相同，它支持数字，字符串甚至可以包含列表（所谓嵌套）。
#
# 列表是写在方括号 [] 之间、用逗号分隔开的元素列表。
#
# 和字符串一样，列表同样可以被索引和截取，列表被截取后返回一个包含所需元素的新列表。

# 与Python字符串不一样的是，列表中的元素是可以改变的：

# 列表截取的语法格式如下：
# 变量[头下标:尾下标]
print("列表相关：")
list = ['abcd', 786, 2.23, 'runoob', 70.2]
tinylist = [123, 'runoob']

print(list)  # 输出完整列表
print(list[0])  # 输出列表第一个元素
print(list[1:3])  # 从第二个开始输出到第三个元素
print(list[2:])  # 输出从第三个元素开始的所有元素
print(tinylist * 2)  # 输出两次列表
print(list + tinylist)  # 连接列表
print()
# Tuple（元组）
# 元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号 () 里，元素之间用逗号隔开。
#
# 元组中的元素类型也可以不相同：
# 虽然tuple的元素不可改变，但它可以包含可变的对象，比如list列表。
print("元组相关：")

tuple = ('abcd', 786, 2.23, 'runoob', 70.2)
tinytuple = (123, 'runoob')
print(tuple)  # 输出完整元组
print(tuple[0])  # 输出元组的第一个元素
print(tuple[1:3])  # 输出从第二个元素开始到第三个元素
print(tuple[2:])  # 输出从第三个元素开始的所有元素
print(tinytuple * 2)  # 输出两次元组
print(tuple + tinytuple)  # 连接元组
print()

# Set（集合）
# 集合（set）是一个无序不重复元素的序列。
# 基本功能是进行成员关系测试和删除重复元素。
# 可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
print("集合set相关：")

student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
print(student)  # 输出集合，重复的元素被自动去掉
# 成员测试
if 'Rose' in student:
    print('Rose 在集合中')
else:
    print('Rose 不在集合中')
# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')
print(a)
print(a - b)  # a和b的差集
print(a | b)  # a和b的并集
print(a & b)  # a和b的交集
print(a ^ b)  # a和b中不同时存在的元素
print()

# Dictionary（字典）
# 字典（dictionary）是Python中另一个非常有用的内置数据类型。


print("Dictionary字典相关：")

dict = {}
dict['one'] = "1 - 菜鸟教程"
dict[2] = "2 - 菜鸟工具"
tinydict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}
print(dict['one'])  # 输出键为 'one' 的值
print(dict[2])  # 输出键为 2 的值
print(tinydict)  # 输出完整的字典
print(tinydict.keys())  # 输出所有键
print(tinydict.values())  # 输出所有值
#
# 注意：
#
# 1、字典是一种映射类型，它的元素是键值对。
# 2、字典的关键字必须为不可变类型，且不能重复。
# 3、创建空字典使用 { }。
#
print()

#
# Python数据类型转换
# 有时候，我们需要对数据内置的类型进行转换，数据类型的转换，你只需要将数据类型作为函数名即可。
#
# 以下几个内置的函数可以执行数据类型之间的转换。这些函数返回一个新的对象，表示转换的值。

# 函数	                            描述
# int(x [,base])            将x转换为一个整数
#
# float(x)                  将x转换到一个浮点数
#
# complex(real [,imag])     创建一个复数
# 
# str(x)                    将对象 x 转换为字符串
#
# repr(x)                   将对象 x 转换为表达式字符串
#
# eval(str)                 用来计算在字符串中的有效Python表达式,并返回一个对象
#
# tuple(s)                  将序列 s 转换为一个元组
#
# list(s)                   将序列 s 转换为一个列表
#
# set(s)                    转换为可变集合
#
# dict(d)                   创建一个字典。d 必须是一个序列 (key,value)元组。
#
# frozenset(s)              转换为不可变集合
#
# chr(x)                    将一个整数转换为一个字符
#
# ord(x)                    将一个字符转换为它的整数值
#
# hex(x)                    将一个整数转换为一个十六进制字符串
#
# oct(x)                    将一个整数转换为一个八进制字符串
