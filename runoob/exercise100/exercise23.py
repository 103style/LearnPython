# http://www.runoob.com/python/python-exercise-example23.html

# 题目：打印出如下图案（菱形）:
#
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *


for x in range(0, 7):
    if x >= 4:
        for y in range(0, x - 3):
            print(' ', end='')
        for y in range(0, 7 - 2 * (x - 3)):
            print('x', end='')
        print()
    else:
        for y in range(1, 4 - x):
            print(' ', end='')
        for y in range(0, 2 * x + 1):
            print('x', end='')
        print()
