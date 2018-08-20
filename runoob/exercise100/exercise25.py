# http://www.runoob.com/python/python-exercise-example25.html

# 题目：求1+2!+3!+...+20!的和。

def getSum(res, max):
    if max == 1:
        print(res)
        return
    else:
        temp = 1
        for x in range(1, max + 1):
            temp *= x
        res += temp
    max -= 1
    getSum(res, max)


getSum(0,20)
