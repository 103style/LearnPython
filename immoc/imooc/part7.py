# https://www.imooc.com/learn/177  第七章 学习

# 函数

# 查看函数abs帮助信息
help(abs)

# 调用函数的时候，如果传入的参数数量不对，会报TypeError的错误，并且Python会明确地告诉你：abs()有且仅有1个参数，但给出了两个：
# abs(1, 2)

# abs('a')

a = '123'
a = int(a)
print(a, '-', type(a))

a = str(a)
print(a, '-', type(a))

# sum()函数接受一个list作为参数，并返回list所有元素之和。请计算 1*1 + 2*2 + 3*3 + ... + 100*100。
list = []
for x in range(1, 101):
    list.append(x * x)
print(sum(list))


# 函数格式 定义一个函数要使用 def 语句，依次写出函数名、括号、括号中的参数和冒号:，
# 然后，在缩进块中编写函数体，函数的返回值用 return 语句返回。
def square_of_sum(L):
    print(L)
    sum = 0
    for x in L:
        sum = sum + x * x
    return sum


L = []
for x in range(1, 101):
    L.append(x)
print(square_of_sum(L))

# 一元二次方程的定义是：ax² + bx + c = 0
# 请编写一个函数，返回一元二次方程的两个解。

import math


def quadratic_equation(a, b, c):
    return -b / 2 / a + math.sqrt((b * b) / (4 * a * a) - (c / a))


print(quadratic_equation(2, 3, 0))
print(quadratic_equation(1, -6, 5))


# 递归函数

# 任务
# 汉诺塔 (http://baike.baidu.com/view/191666.htm) 的移动也可以看做是递归函数。
# 我们对柱子编号为a, b, c，将所有圆盘从a移到c可以描述为：
# 如果a只有一个圆盘，可以直接移动到c；
# 如果a有N个圆盘，可以看成a有1个圆盘（底盘） + (N-1)个圆盘，首先需要把 (N-1) 个圆盘移动到 b，然后，将 a的最后一个圆盘移动到c，再将b的(N-1)个圆盘移动到c。
# 请编写一个函数，给定输入 n, a, b, c，打印出移动的步骤：
# move(n, a, b, c)
#
# 例如，输入 move(2, 'A', 'B', 'C')，打印出：
# A --> B
# A --> C
# B --> C

# def move(n, a, b, c):
#     if n - 1 == 0:
#         print(a, ' --> ', c)
#         print(b, ' --> ', c)
#         return
#     else:
#         print(a, ' --> ', b)
#     move(n - 1, a, b, c)


def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
        return
    move(n - 1, a, c, b)
    print(a, '-->', c)
    move(n - 1, b, a, c)


move(4, 'A', 'B', 'C')


### 默认参数
# 请定义一个 greet() 函数，它包含一个默认参数，如果没有传入，打印 'Hello, world.'，如果传入，打印 'Hello, xxx.'

def greet(s='world'):
    print('hello,', s, '.')


greet()
greet('Bart')


### 定义可变参数
def fn(*args):
    print(args)


fn()
fn(1)
fn(1, 2)
fn(1, 2, '2')


# 任务
# 请编写接受可变参数的 average() 函数。
def average(*scores):
    sum = 0
    if scores.__len__() == 0:
        print(sum)
    else:
        for score in scores:
            sum += score
        print(sum / scores.__len__())


average(1, 2, 3)
average(101, 92, 133)
