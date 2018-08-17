# http://www.runoob.com/python/python-exercise-example7.html

# 题目：将一个列表的数据复制到另一个列表中。

def copyList(L):
    return L[:]

L = [1,2,3]
print(copyList(L))