# http://www.runoob.com/python3/python3-list.html


# len([1, 2, 3])	                        3	                            长度
# [1, 2, 3] + [4, 5, 6]	                [1, 2, 3, 4, 5, 6]	                组合
# ['Hi!'] * 4	                            ['Hi!', 'Hi!', 'Hi!', 'Hi!']	重复
# 3 in [1, 2, 3]	                        True	                        元素是否存在于列表中
# for x in [1, 2, 3]: print(x, end=" ")	1 2 3	                            迭代


#  嵌套列表
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]

print('a = ', a, ' n = ', n)
print('[a, n] = ', x)

# 1	len(list)
# 列表元素个数
#
# 2	max(list)
# 返回列表元素最大值
#
# 3	min(list)
# 返回列表元素最小值
#
# 4	list(seq)
# 将元组转换为列表


print('max(a) = ', max(a))
print('max(n) = ', max(n))
print('min(a) = ', min(a))
print('min(b) = ', min(n))

# 1	list.append(obj)
# 在列表末尾添加新的对象
a.append('a')
print('a.append(\'a\')   a = ', a)
#
# 2	list.count(obj)
# 统计某个元素在列表中出现的次数
print('a.count(\'a\') = ', a.count('a'))
#
# 3	list.extend(seq)
# 在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
a.extend(n)
print("a.extend(n),  a = ", a)

#
# 4	list.index(obj)
# 从列表中找出某个值第一个匹配项的索引位置
print("a.index('c') = ", a.index('c'))
#
# 5	list.insert(index, obj)
# 将对象插入列表
a.insert(1, 'd')
print("a.insert(1,'d')  a = ", a)

#
# 6	list.pop([index=-1]])
# 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
print('a = ', a)
a.pop()
print('a.pop()  a = ', a)
#
# 7	list.remove(obj)
# 移除列表中某个值的第一个匹配项
#
# 8	list.reverse()
# 反向列表中元素
a.reverse()
print('a.reverse(), a = ', a)
#
# 9	list.sort(cmp=None, key=None, reverse=False)
# 对原列表进行排序
b = [2, 5, 6, 8, 14, 2, 6, 2]
list.sort(b)
print('list.sort([2,5,6,8,14,2,6,2])  = ', b)
#
# 10	list.clear()
b.clear()
print('b.clear()   b = ', b)
# 清空列表
#
# 11	list.copy()
# 复制列表
s = a.copy()
print('s = a.copy()  s = ', s)
