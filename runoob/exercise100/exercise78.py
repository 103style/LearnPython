# http://www.runoob.com/python/python-exercise-example78.html

# 题目：找到年龄最大的人，并输出。请找出程序中有什么问题。


person = {"li": 18, "wang": 50, "zhang": 20, "sun": 22}

keys = person.keys()

max = 0
name = ''
for x in keys:
    if max < person[x]:
        max = person[x]
        name = x
print("年龄最大的是%s，年龄是%d"% (name, max))
