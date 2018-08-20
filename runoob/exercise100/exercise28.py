# http://www.runoob.com/python/python-exercise-example28.html

# 题目：有5个人坐在一起，问第五个人多少岁？他说比第4个人大2岁。
# 问第4个人岁数，他说比第3个人大2岁。
# 问第三个人，又说比第2人大两岁。
# 问第2个人，说比第一个人大两岁。
# 最后问第一个人，他说是10岁。请问第五个人多大？


def getAge(start=10, temp=2, count=5):
    for x in range(1, count):
        start += temp
    return start


print(getAge())
