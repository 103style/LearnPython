# -*- coding:utf-8 -*-


# https://www.imooc.com/learn/177  第三章 学习
# Python变量和数据类型

print(u'''
静夜思
床前明月光，
疑是地上霜。
举头望明月，
低头思故乡。
''')

print(10 / 4)

print(2.5 + 10/4)

print(2.5 + 10/4.0)


#1. 在计算 a and b 时，如果 a 是 False，
# 则根据与运算法则，整个结果必定为 False，因此返回 a；
# 如果 a 是 True，则整个计算结果必定取决与 b，因此返回 b。

#2. 在计算 a or b 时，如果 a 是 True，
# 则根据或运算法则，整个计算结果必定为 True，因此返回 a；
# 如果 a 是 False，则整个计算结果必定取决于 b，因此返回 b。

a = 'python'
print('hello,', a or 'world')
b = ''
print('hello,',b or 'world')
