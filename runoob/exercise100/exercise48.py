# http://www.runoob.com/python/python-exercise-example48.html

# 题目：数字比较。

COMPARE =  lambda x, y: (x > y) * x + (x < y) * y

print(COMPARE(20, 10))


def compare(x,y):
    if x > y:
        return "%d比%d大" %(x,y)
    elif x == y:
        return "%d和%d相等" % (x, y)
    else:
        return "%d比%d小" % (x, y)

print(compare(20,10))
print(compare(10,10))
print(compare(10,20))