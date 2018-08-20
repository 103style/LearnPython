# http://www.runoob.com/python/python-exercise-example22.html

# 题目：两个乒乓球队进行比赛，各出三人。
# 甲队为a,b,c三人，乙队为x,y,z三人。已
# 抽签决定比赛名单。
# 有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。


print(ord('x'))
print(ord('z'))
print(ord('a'))
print(ord('A'))

L1 = ['x', 'y', 'z']
L2 = ['c', 'a', 'b']

L = []

for x in range(0,3):
    for y in range(0, 3):
        if x == 0  and y == 1:
            print(L2[x],'-',L1[y])
            L.append(L1[y])
        elif x==1 and y == 2:
            print(L2[x], '-', L1[y])
            L.append(L1[y])
        elif x == 2 and not(L1[y] in L):
            print(L2[x], '-', L1[y])