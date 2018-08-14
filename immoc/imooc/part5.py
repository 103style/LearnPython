# https://www.imooc.com/learn/177  第五章 学习

###  if 语句

# 注意: Python代码的缩进规则。具有相同缩进的代码被视为代码块，上面的3，4行 print 语句就构成一个代码块（但不包括第5行的print）。
# 如果 if 语句判断为 True，就会执行这个代码块。
# 缩进请严格按照Python的习惯写法：4个空格，不要使用Tab，更不要混合Tab和空格，否则很容易造成因为缩进引起的语法错误。

age = 20
if age >= 18:
    print('age = ', age)
    print("you are a adult")
print('end')

s = (1, 2, 3)
if s.__len__() > 3:
    print('s的长度大于三')
else:
    print('s的长度小于三')
print('end')

score = 80
if score >= 90:
    print('优秀')
elif score >= 80:
    print('良好')
elif score >= 60:
    print('一般')
else:
    print('有待加强')

### for 循环语句

for x in range(1,10):
    print(x)


names = ['xiaoming', 'xiaohong', 'xiaowang', 'xiaoli']
for name in names:
    print(name)

scores = [80, 85, 72, 79, 86, 95, 89, 62, 98, 56]
count = 0
for score in scores:
    count += score
print('一共', scores.__len__(), '人，分数总和为：', count)
print(count / scores.__len__())

years = (2000, 2001, 2002, 2003)
for year in years:
    print('今年是', year, '年')
    if year % 4 == 0:
        print(year, '年是闰年')
    else:
        print(year, '年是平年')

### while循环

max = 100
sum = 0
sum1 = 0
sum2 = 0
x = 0
while x < max:
    sum += x
    if x % 2 != 0:
        sum1 += x
    else:
        sum2 += x
    x += 1
print('100以内的奇数和是：', sum1)
print('100以内的偶数和是：', sum2)
print('100以内的数之和是：', sum)

## break语句
x = 1
sum = 0
while x < 50:
    x += 1
    if x > 25:
        print('break 语句触发')
        break
    else:
        print('未达到break条件', x)
print('end')

### continue语句

x = 0
sum = 0
while x < 100:
    x += 1
    if x % 2 == 0:
        continue
    else:
        sum += x
print('100以内的奇数和为：', sum)


## 多重循环
for x in range(1,20):
    for y in range(x+2,10):
        print(x,'+',y,'=', x + y)
