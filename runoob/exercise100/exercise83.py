# http://www.runoob.com/python/python-exercise-example83.html

# 题目：求0—7所能组成的奇数个数。

# 1,3,4,5

import math


def get_count(digit=1):
    if digit == 1:
        return 4
    elif digit == 2:
        return 7 * 4
    else:
        return 7 * math.pow(8, digit - 2) * 4


for x in range(1, 8):
    print(get_count(x))
