# http://www.runoob.com/python/python-exercise-example66.html

# 题目：输入3个数a,b,c，if 按大小顺序输出.

res = []
for x in range(3):
    res.append(int(input("请依次输入三个数：")))

res.sort()
print(res)

