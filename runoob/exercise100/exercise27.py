# http://www.runoob.com/python/python-exercise-example27.html

# 题目：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。


def invert(str, index=0):
    if (index == len(str)):
        return
    print(str[len(str) - index - 1])
    index += 1
    invert(str, index)


s = input("请输入一个5个字符:")

invert(s)
