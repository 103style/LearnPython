# http://www.runoob.com/python/python-exercise-example3.html

# 题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？

S = {}
for x in range(1, 169):
    S[x * x] = x

R = []

for k in S.keys():
    if k - 168 in S:
        R.append(k - 168 - 100)

print(R)
