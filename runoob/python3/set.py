# http://www.runoob.com/python3/python3-set.html

# 集合（set）是一个无序不重复元素的序列。
# 可以使用大括号 { } 或者 set() 函数创建集合，
#
# 注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# 这里演示的是去重功能
print(basket)

# 快速判断元素是否在集合内
print('orange' in basket)

print("'crabgrass' in basket  = ", 'crabgrass' in basket)

# 下面展示两个集合间的运算.
a = set('abracadabra')
b = set('alacazam')
print('a = ', a)
print('b = ', b)

# 集合a中包含元素
print('a - b = ', a - b)

# 集合a或b中包含的所有元素
print('a | b  = ', a | b)

# 集合a和b中都包含了的元素
print('a & b = ', a & b)

# 不同时包含于a和b的元素
print('a ^ b = ', a ^ b)

print('basket = ', basket)
# 添加元素
# 将元素 x 添加到集合 s 中，如果元素已存在，则不进行任何操作
basket.add('milk')
print("basket.add('milk') = ", basket)

# update也可以添加元素，且参数可以是列表，元组，字典等
basket.update('ice')
print("basket.update('ice') = ", basket)

# 移除元素
basket.remove('milk')
print("basket.remove('milk') = ", basket)

basket.discard('i')
print("basket.discard('i') = ", basket)

basket.pop()
print('basket.pop() = ', basket)

# 计算集合元素个数
print('len(basket) = ', len(basket))

# 判断元素是否在集合中存在
print("'milk' in basket = ", 'milk' in basket)
print("'c' in basket = ", 'c' in basket)

basket.clear()
print("basket.clear() = ", basket)
