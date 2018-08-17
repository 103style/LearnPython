# http://www.runoob.com/python/python-exercise-example4.html

# 题目：输入某年某月某日，判断这一天是这一年的第几天？


y = int(input("年份："))
m = int(input("月份："))
d = int(input("日期："))

print(y, '-', m, '-', d)

D = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if y % 400 == 0:
    D[1] = 29
elif y % 100 != 0 and y % 40 == 0:
    D[1] = 29
elif y % 10 != 0 and y % 4 == 0:
    D[1] = 29
print(D)

sum = 0
for x in range(0, m - 1):
    sum += D[x]
print('今天是今年的第 ',sum + d,'天')
