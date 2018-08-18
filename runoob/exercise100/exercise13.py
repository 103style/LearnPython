# http://www.runoob.com/python/python-exercise-example13.html

# 题目：打印出所有的"水仙花数"，
# 所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。
# 例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。

res = []

x = 102
a = int(x / 100)
b = int(x % 100 / 10)
c = x % 10
print(a, '-', b, '-', c)
for x in range(100, 1000):
    a = int(x / 100)
    b = int(x % 100 / 10)
    c = x % 10
    if a * a * a + b * b * b + c * c * c == x:
        res.append(x)
print(res)
