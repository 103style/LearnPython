# http://www.runoob.com/python/python-exercise-example87.html

# 题目：回答结果（结构体变量传递）。

class student:
    x = 0
    c = 0


def f(stu):
    stu.x = 20
    stu.c = 'c'


a = student()
a.x = 3
a.c = 'a'
f(a)
print(a.x, a.c)


def change(s = 0):
    s+=1


s = 10
print(s)
change(s)
print(s)