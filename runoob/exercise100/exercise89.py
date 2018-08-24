# http://www.runoob.com/python/python-exercise-example89.html

# 题目：某个公司采用公用电话传递数据，数据是四位的整数，在传递过程中是加密的，
# 加密规则如下：每位数字都加上5,然后用和除以10的余数代替该数字，再将第一位和第四位交换，第二位和第三位交换。
# 编写加密程序

num = int(input("请输入一个四位整数："))

a = int(num / 1000)
b = int(num / 100) % 10
c = int(num / 10) % 10
d = num % 10

a = (a + 5) % 10
b = (b + 5) % 10
c = (c + 5) % 10
d = (d + 5) % 10

print(int(str(d) + str(c) + str(b) + str(a)))
