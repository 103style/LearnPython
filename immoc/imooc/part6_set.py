# https://www.imooc.com/learn/177  第六章 学习

### set  set持有一系列元素，这一点和 list 很像，但是set的元素没有重复，而且是无序的，这点和 dict 的 key很像。


# set的内部结构和dict很像，唯一区别是不存储value，因此，判断一个元素是否在set中速度很快。

# set存储的元素和dict的key类似，必须是不变对象，因此，任何可变对象是不能放入set中的。

s = set(['A', 'B', 'C'])
print(s)

# 存在相同元素时
s = set(['A', 'B', 'B', 'C', 'C', 'C'])
print(s)
print(s.__len__())

# 判断是否存在
print('A' in s)
print('c' in s)

# 练习
weekdays = set(['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'])

test = ['Mon', 'MON', 'THU', 'sun']
for t in test:
    if t in weekdays:
        print(t, 'is a day')
    else:
        print(t, 'is not a day')

# 遍历set
for x in s:
    print(x)

# 任务
# 请用 for 循环遍历如下的set，打印出 name: score 来。

s = set([('Adam', 95), ('Lisa', 85), ('Bart', 59)])

for name in s:
    print(name[0], ':', name[1])


# 更新set
# 添加元素
s.add('T')
print('添加元素后：',s)
# 添加已有元素
s.add('A')
print('添加已有元素后：',s)

# 删除元素
s.remove('A')
print('删除元素后：',s)

# 删除不存在元素  会报错
s.remove('G')
print('删除不存在元素后：',s)
