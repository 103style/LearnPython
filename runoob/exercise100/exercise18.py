# http://www.runoob.com/python/python-exercise-example18.html

# 题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。

import math

a = int(input('请输入数字a:'))
n = int(input('请输出几个数相加：'))
print(a, '---', n)


def numSum(a, n):
    sum = 0
    for x in range(1, n + 1):
        for y in range(0, x ):
            sum += a * math.pow(10, y)

    return sum


print(numSum(a, n))
