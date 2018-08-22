# http://www.runoob.com/python/python-exercise-example55.html

# 题目：学习使用按位取反~。


# a = 0011 1100
#
# b = 0000 1101
#
# -----------------
#
# a&b = 0000 1100
#
# a|b = 0011 1101
#
# a^b = 0011 0001
#
# ~a  = 1100 0011

a = 60  # 0011 1100
print(a)
a = ~a
print(a) # 输出结果 -61 ，二进制解释： 1100 0011， 在一个有符号二进制数的补码形式。
print(~a)
