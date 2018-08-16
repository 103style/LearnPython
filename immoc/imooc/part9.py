# https://www.imooc.com/learn/177  第九章 学习

# 迭代
# 在Python中，如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们成为迭代（Iteration）。
#
# 因为 Python 的 for循环不仅可以用在list或tuple上，还可以作用在其他任何可迭代对象上。
#
# 因此，迭代操作就是对于一个集合，无论该集合是有序还是无序，我们用 for 循环总是可以依次取出集合的每一个元素。
#
# 注意: 集合是指包含一组元素的数据结构，我们已经介绍的包括：
# 1. 有序集合：list，tuple，str和unicode；
# 2. 无序集合：set
# 3. 无序集合并且具有 key-value 对：dict
# 而迭代是一个动词，它指的是一种操作，在Python中，就是 for 循环。
#
# 迭代与按下标访问数组最大的不同是，后者是一种具体的迭代实现方式，而前者只关心迭代结果，根本不关心迭代内部是如何实现的。


# 任务
# 请用for循环迭代数列 1-100 并打印出7的倍数。

for x in range(1, 101):
    if x % 7 == 0:
        print(x)

### 索引迭代

# Python中，迭代永远是取出元素本身，而非元素的索引。

# 对于有序集合，元素确实是有索引的。有的时候，我们确实想在 for 循环中拿到索引，怎么办？

# 方法是使用 enumerate() 函数：
L = ['Adam', 'Lisa', 'Bart', 'Paul']

for index, name in enumerate(L):
    print(index, '-', name)
# 0 - Adam
# 1 - Lisa
# 2 - Bart
# 3 - Paul

for t in enumerate(L):
    index = t[0]
    name = t[1]
    print(index, '-', name)

# 可见，索引迭代也不是真的按索引访问，而是由 enumerate() 函数自动把每个元素变成 (index, element) 这样的tuple，再迭代，就同时获得了索引和元素本身。


# 任务
# zip()函数可以把两个 list 变成一个 list：
#
# >>> zip([10, 20, 30], ['A', 'B', 'C'])
# [(10, 'A'), (20, 'B'), (30, 'C')]
# 在迭代 ['Adam', 'Lisa', 'Bart', 'Paul'] 时，如果我们想打印出名次 - 名字（名次从1开始)，请考虑如何在迭代中打印出来。
#
# 提示：考虑使用zip()函数和range()函数

L = ['Adam', 'Lisa', 'Bart', 'Paul']
for index, name in zip(range(1, len(L) + 1), L):
    print(index, '-', name)

### 迭代dict的value
d = {'Adam': 95, 'Lisa': 85, 'Bart': 59}

print(d.values())

print(d.__iter__())
for x in d.__iter__():
    print(x)
# values() 方法实际上把一个 dict 转换成了包含 value 的list。
# 但是 itervalues() 方法不会转换，它会在迭代过程中依次从 dict 中取出 value，所以 itervalues() 方法比 values() 方法节省了生成 list 所需的内存。


# 任务
# 给定一个dict：
#
# d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }
#
# 请计算所有同学的平均分。

d = {'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74}

sum = 0
for x in d.values():
    sum += x
print(sum / d.__len__())

### 迭代dict的key和value

#  items()
print(d.items())

for key, value in d.items():
    print(key, '-', value)

# 任务
# 请根据dict：
#
# d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }
#
# 打印出 name : score，最后再打印出平均分 average : score。

d = {'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74}

sum = 0
for key, value in d.items():
    sum += value
    print(key, "-", value)
print('averger : ', sum / len(d))
