# http://www.runoob.com/python/python-exercise-example85.html

# 题目：输入一个奇数，然后判断最少几个 9 除于该数的结果为整数。

import math

num = int(input("请输入一个奇数："))

index = 1

while (math.pow(10, index) - 1) % num != 0:
    index += 1
print("最少需要%d个 9 除于该数的结果为整数" % index)