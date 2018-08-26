# http://www.runoob.com/python/python-get-prime-number.html

# 题目： 获取 100 以内的质数。

res = []
for x in range(2, 100):
    y = x
    for y in range(2, x):
        if x % y == 0:
            break
        if x % y != 0 and y + 1 == x:
            res.append(x)
    if x == y:
        res.append(x)
print(res)
