# http://www.runoob.com/python/python-exercise-example11.html

# 题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，
# 小兔子长到第三个月后每个月又生一对兔子，
# 假如兔子都不死，问每个月的兔子总数为多少？


#  1,1,2,3,5,8,13,21

#  可以知道第三个月的兔子 =  前两个月兔子之和

L = [1, 1]
for x in range(1, 10):
    L.append(L[-1] + L[-2])

print(L)
