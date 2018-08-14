# https://www.imooc.com/learn/177  第四章 学习
# List类型

# 用[] 包起来的就是 list集合
list =  ['Michael','Bob','Tarcy']
print(list)

# 集合里面的类型可以不一致
list = [True, 1024, 'Part4']
print(list)

list = ['Adam', 95.5, 'Lisa', 85, 'Bart', 59]
print(list)

# 按索引访问list
print(list[0])
print(list[1])
print(list[2])

#- 1索引 表示 倒数第一个
print(list[-1])
print(list[-2])
print(list[-3])

# list 添加元素
# append表示添加在末尾
list.append('test')
print(list)

# insert(index,T)  插在第几个位置
list.insert(2,'Sencond')
print(list)

# list 删除元素
# pop() 删除最后一个元素
list.pop()
print(list)

# pop(index) 删除第几个元素
list.pop(2)
print(list)

# list 替换元素
list[1] = 'Second'
list[-1] = 'Last'
print(list)


