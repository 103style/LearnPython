# https://www.imooc.com/learn/177  第四章 学习
# Tuple类型

# tuple是另一种有序的列表，中文翻译为“ 元组 ”。tuple 和 list 非常类似，但是，tuple一旦创建完毕，就不能修改了。
#一般用（）抱起来的就是tuple

t = ('xiaoming', 'xiaowang', 'xiaoli')
print(t)

print(t[0])
print(t[-1])

# 空元素
t = ()
print(t)

# 单元素 元组 需要添加逗号
# 正是因为用()定义单元素的tuple有歧义，所以 Python 规定，单元素 tuple 要多加一个逗号“,”，这样就避免了歧义：
s = (1)
print(s)
t = (1, )
print(t)
# 多元素 tuple 加不加这个额外的“,”效果是一样的：

t = (1, 2, 3,)
print(t)


# "可变"的tuple
t = (1, 2, ['xiaoming', 'xiaohong'])
L = t[2]
L[0] = 'xiaowang'
L[1] = 'xiaoli'
print(t)


# tuple一开始指向的list并没有改成别的list，
# 所以，tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。
# 即指向'a'，就不能改成指向'b'，指向一个list，就不能改成指向其他对象，但指向的这个list本身是可变的！