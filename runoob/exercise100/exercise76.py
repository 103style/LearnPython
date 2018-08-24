# http://www.runoob.com/python/python-exercise-example76.html

# 题目：编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n


n = int(input("请输出一个整数："))

start = 1

if n % 2 == 0:
    start = 2

sum = 0
for i in range(start, n + 1, 2):
    print(i)
    sum += 1 / i
print(sum)
