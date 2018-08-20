# http://www.runoob.com/python/python-exercise-example30.html

# 题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。

def isHuiWenShu(num):
    if num < 10000 or num > 99999:
        return num, False

    a = int(num / 10000)
    b = int(num / 1000) % 10
    c = int(num / 100) % 10
    d = int(num / 10) % 10
    e = num % 10
    print(a,'-',b,'-',c,'-',d,'-',e)
    if a == e and b == d:
        return  num,True
    else:
        return  num,False


num = int(input("请输入一个五位数:"))

print(isHuiWenShu(num))
