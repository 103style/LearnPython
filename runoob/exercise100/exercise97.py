# http://www.runoob.com/python/python-exercise-example97.html

# 题目：从键盘输入一些字符，逐个把它们写到磁盘文件上，直到输入一个 # 为止。

w = ''

file = open('exercise97.text','w')
while(w != '#'):
    w = input("请输入一个字符：")
    file.write(w)
file = open('exercise97.text','r')
print(file.read())