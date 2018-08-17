# http://www.runoob.com/python/python-exercise-example8.html

# 题目：输出 9*9 乘法口诀表。

for x in range(1, 10):
    for y in range(1, x + 1):
        print(("%d * %d = %d  ") % (x, y, x * y), end='')
    print('')

# 不换行输出  print('',end='')
