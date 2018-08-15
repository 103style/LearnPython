# https://www.imooc.com/learn/177  第六章 学习

### dict

# dict的第一个特点是查找速度快，无论dict有10个元素还是10万个元素，查找速度都一样。
# 而list的查找速度随着元素增加而逐渐下降。
# 由于dict是按 key 查找，所以，在一个dict中，key不能重复。

# dict的第二个特点就是存储的key-value序对是没有顺序的！

# dict的第三个特点是作为 key 的元素必须不可变，
# Python的基本类型如字符串、整数、浮点数都是不可变的，都可以作为 key。但是list是可变的，就不能作为 key。


d = {
    'xiaoming': 12,
    'xiaohong': 15,
    'xiaoli': 18,
    'xiaowang': 16
}
print(d)

# 获取 字典 长度
print('d的长度是：',d.__len__())

# 直接取key  不存在会报KeyError 所以先判断是否存在
if 'xiaoming' in d:
    print(d['xiaoming'])
else:
    print('不存在')

# get方法
print('get(\'xiaowang\')=',d.get('xiaowang'))


# 更新dict
# 修改已有的key
d['xiaoming'] = 20
print(d)
# 修改未有的key
d['xiaomo'] = 19
print(d)

# 遍历 dict
for key in d:
    print(key, ':',  d[key])

