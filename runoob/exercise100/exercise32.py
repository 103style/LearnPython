# http://www.runoob.com/python/python-exercise-example32.html

# 题目：按相反的顺序输出列表的值。

def invert(list):
    for x in range(0, len(list)):
        print(list[-1 - x])

    for x in list[::-1]:
        print(x)


L = [1, 2, 3, 4, 5, 6, 7, 8, 9]

invert(L)