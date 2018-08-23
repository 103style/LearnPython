# http://www.runoob.com/python/python-exercise-example68.html

# 题目：有n个整数，使其前面各数顺序向后移m个位置，最后m个数变成最前面的m个数

res = []
n = int(input("请输入数组的个数: "))
for x in range(n):
    res.append(int(input("请输入第%d个元素：" % (x + 1))))

m = int(input("请输入后移m个位置的值："))

m = m % n

start = res[0:n - m]
end = res[n - m:n]

for x in range(len(res)):
    if x < m:
        res[x] = end[x]
    else:
        res[x] = start[x - m]

print(res)

#
# 请输入数组的个数: 10
# 请输入第1个元素：1
# 请输入第2个元素：2
# 请输入第3个元素：3
# 请输入第4个元素：4
# 请输入第5个元素：5
# 请输入第6个元素：6
# 请输入第7个元素：7
# 请输入第8个元素：8
# 请输入第9个元素：9
# 请输入第10个元素：10
# 请输入后移m个位置的值：3
# [8, 9, 10, 1, 2, 3, 4, 5, 6, 7]