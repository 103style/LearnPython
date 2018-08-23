# http://www.runoob.com/python/python-exercise-example67.html

# 题目：输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组。

res = []
l = int(input("请输入数组的个数: "))
for x in range(l):
    res.append(int(input("请输入第%d个元素：" % (x + 1))))


temp = res[:]
temp.sort()
min = temp[0]
max = temp[-1]

for x in range(1,len(res)-1):
    if res[x] == min:
        temp = res[0]
        res[0] = min
        res[x] = temp
    if res[x] == max:
        temp = res[-1]
        res[-1] = max
        res[x] = temp


print(res)
