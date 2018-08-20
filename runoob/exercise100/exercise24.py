# http://www.runoob.com/python/python-exercise-example24.html

# 题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。


sum = 0
a = 1
b = 2
for x in range(0, 20):
    sum = sum + b / a
    temp = a + b
    a = b
    b = temp

print(sum)
