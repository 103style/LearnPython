# http://www.runoob.com/python/python-exercise-example26.html

# 题目：利用递归方法求5!。

def getFactorial(start=1, num=1):
    if num == 1:
        print(start)
        return
    else:
        start *= num
        num -= 1
        getFactorial(start, num)


getFactorial(1, 5)
