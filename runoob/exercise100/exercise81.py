# http://www.runoob.com/python/python-exercise-example81.html

# 题目：809*??=800*??+9*?? 其中??代表的两位数, 809*??为四位数，8*??的结果为两位数，9*??的结果为3位数。求??代表的两位数，及809*??后的结果。


for x in range(10, int(100 / 8) + 1):
    if x * 9 > 100 and 809 * x < 10000:
        print("??代表的两位数为%d，809*??=%d" % (x, 809 * x))
