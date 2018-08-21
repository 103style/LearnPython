# http://www.runoob.com/python/python-exercise-example47.html

# 题目：两个变量值互换。

def change(a, b):
    temp = a
    a = b
    b = temp
    return a, b

print(change(5,15))
