# https://www.imooc.com/learn/177  第十章 学习

# 列表生成式

# 要生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]，我们可以用range(1, 11)：
print(range(1, 11))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 但如果要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？方法一是循环：
L = []
for x in range(1, 11):
    L.append(x * x)
print(L)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print([x * x for x in range(1, 11)])

# 这种写法就是Python特有的列表生成式。利用列表生成式，可以以非常简洁的代码生成 list。


# 任务
# 请利用列表生成式生成列表 [1x2, 3x4, 5x6, 7x8, ..., 99x100]
print([x * (x + 1) for x in range(1, 101, 2)])

### 复杂表达式
# 使用for循环的迭代不仅可以迭代普通的list，还可以迭代dict。
d = {'Adam': 95, 'Lisa': 85, 'Bart': 59}
tds = ['<tr><td>%s</td><td>%s</td></tr>' % (name, score) for name, score in d.items()]
print('<table>')
print('<tr><th>Name</th><th>Score</th><tr>')
print('\n'.join(tds))
print('</table>')

d = {'Adam': 95, 'Lisa': 85, 'Bart': 59}


# 任务
# 在生成的表格中，对于没有及格的同学，请把分数标记为红色。
def generate_tr(name, score):
    if score < 60:
        return '<tr><td>%s</td><td style="color:red">%s</td></tr>' % (name, score)
    else:
        return '<tr><td>%s</td><td>%s</td></tr>' % (name, score)


tds = [generate_tr(name, score) for name, score in d.items()]
print('<table border="1">')
print('<tr><th>Name</th><th>Score</th><tr>')
print('\n'.join(tds))
print('</table>')


def sayHello(s='world'):
    print('Hello %s' % (s))


sayHello()
sayHello('Tina')

### 条件过滤

# 列表生成式的 for 循环后面还可以加上 if 判断。例如：
L = [x * x for x in range(1, 11)]
print(L)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# 如果我们只想要偶数的平方，不改动 range()的情况下，可以加上 if 来筛选：

L = [x * x for x in range(1, 11) if x % 2 == 0]
print(L)


# [4, 16, 36, 64, 100]
# 有了 if 条件，只有 if 判断为 True 的时候，才把循环的当前元素添加到列表中。


# 任务
# 请编写一个函数，它接受一个 list，然后把list中的所有字符串变成大写后返回，非字符串元素将被忽略。
# 提示：
# 1. isinstance(x, str) 可以判断变量 x 是否是字符串；
# 2. 字符串的 upper() 方法可以返回大写的字母。
#
# def change(L):
#     S = []
#     for t in enumerate(L):
#         print(t[0], '-', t[1])
#         if isinstance(t[1], str):
#             S.append(t[1].upper())
#         else:
#             S.append(t[1])
#     return S


def toUppers(L):
    return [x.upper() for x in L if isinstance(x, str)]


L = ['Hello', 'world', 101]
# print(change(L))

print(toUppers(L))

### 多层表达式

# for循环可以嵌套，因此，在列表生成式中，也可以用多层 for 循环来生成列表。

# 对于字符串 'ABC' 和 '123'，可以使用两层循环，生成全排列：
[m + n for m in 'ABC' for n in '123']

# ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']

# 翻译成循环代码就像下面这样：
L = []
for m in 'ABC':
    for n in '123':
        L.append(m + n)

    # 任务
    # 利用 3 层for循环的列表生成式，找出对称的 3 位数。例如，121 就是对称数，因为从右到左倒过来还是 121。

L = [x for x in range(100, 1000) if x % 10 == int(x / 100)]
print(L)

L = []
for x in range(100, 1000):
    if int(x / 100) == x % 10:
        L.append(x)
print(L)

### 2.8.0 和 3.7.0的语法问题
# print[int(str(x) + str(y) + str(z)) for x in range(1, 10) for y in range(0, 10) for z in range(0, 10) if x == z]
#
# print[100 * n1 + 10 * n2 + n3 for n1 in range(1, 10) for n2 in range(10) for n3 in range(10) if n1 == n3]

L = []
for x in range(1, 10):
    for y in range(0, 10):
        for z in range(0, 10):
            if x == z:
                L.append(100 * x + 10 * y + z)
print(L)
