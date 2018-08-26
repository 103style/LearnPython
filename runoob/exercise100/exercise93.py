# http://www.runoob.com/python/python-exercise-example93.html

# 题目：时间函数举例3。


import time

start = time.clock()
for i in range(10000):
    print(i)
end = time.clock()

# %6.3f的格式含义是，数字整体长度包括小数点为6位，保留三位小数。
print(end - start)

print('different is %6.3f' % (end - start))



help(time.clock)