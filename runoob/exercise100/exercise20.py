# http://www.runoob.com/python/python-exercise-example20.html

# 题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？

h = 100


def getHeight(count, height):
    if count == 1:
        return height, height / 2
    else:
        num = height
        for x in range(2, count + 1):
            num += height
            height /= 2
        return num, height / 2


print(getHeight(10, 100))
