# http://www.runoob.com/python3/python3-dictionary.html

# 字典是另一种可变容器模型，且可存储任意类型对象。
# 字典的每个键值(key=>value)对用冒号(:)分割，每个对之间用逗号(,)分割，整个字典包括在花括号({})中 ,
# 格式如下所示：
# d = {key1 : value1, key2 : value2 }


# 键必须是唯一的，但值则不必。
#
# 值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组。


# 访问字典里的值 示例
dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
print("dict['Name']: ", dict['Name'])
print("dict['Age']: ", dict['Age'])

# 如果字典没有对应的键  用键访问会报错
try:
    print(dict['test'])
except Exception as e:
    print("catch 到异常  dict['test']不存在")

# 修改字典
dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
# 更新 Age
dict['Age'] = 8
# 添加信息
dict['School'] = "菜鸟教程"
print("dict['Age']: ", dict['Age'])
print("dict['School']: ", dict['School'])
print(dict)
print()
# 删除字典元素
# 能删单一的元素也能清空字典，清空只需一项操作。
#
# 显示删除一个字典用del命令，如下实例：
dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
# 删除键 'Name'
del dict['Name']
print("del dict['Name'] : ", dict)
# 清空字典
dict.clear()
print('dict.clear()  : ', dict)
# 删除字典
del dict
try:
    print("dict['Age']: ", dict['Age'])
    print("dict['School']: ", dict['School'])
except Exception as r:
    print(r)
print()
# 字典键的特性
# 字典值可以是任何的 python 对象，既可以是标准的对象，也可以是用户定义的，但键不行。

# 1）不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住
# 2）键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行


# 内置函数

# 1	len(dict)
# 计算字典元素个数，即键的总数。
dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
print(len(dict))

# 2	str(dict)
# 输出字典，以可打印的字符串表示。
dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
print(str(dict))

# 3	type(variable)
# 返回输入的变量类型，如果变量是字典就返回字典类型。
dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
print(type(dict))
print()

# 内置方法
# 1	radiansdict.clear()
# 删除字典内所有元素
#
# 2	radiansdict.copy()
# 返回一个字典的浅复制
s = dict.copy()
print('s = dict.copy()  s = ', s)
#
# 3	radiansdict.fromkeys()
# 创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值

#
# 4	radiansdict.get(key, default=None)
# 返回指定键的值，如果值不在字典中返回default值
#
# 5	key in dict
# 如果键在字典dict里返回true，否则返回false
print("'Name' in dict   = ", 'Name' in dict)
#
# 6	radiansdict.items()
# 以列表返回可遍历的(键, 值) 元组数组
print('dict.items() = ', dict.items())

#
# 7	radiansdict.keys()
# 返回一个迭代器，可以使用 list() 来转换为列表
print('dict.keys() = ', dict.keys())
#
# 8	radiansdict.setdefault(key, default=None)
# 和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
#
# 9	radiansdict.update(dict2)
# 把字典dict2的键/值对更新到dict里
#
# 10	radiansdict.values()
# 返回一个迭代器，可以使用 list() 来转换为列表
print('dict.values() = ', dict.values())

#
# 11	pop(key[,default])
# 删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。
print(dict)
print(dict.pop('Name'))
print("dict.pop('Name')  : ", dict)
#
# 12	popitem()
# 随机返回并删除字典中的一对键和值(一般删除末尾对)。
print(dict.popitem())
print(dict.popitem())
print(dict)