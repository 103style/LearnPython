# http://www.runoob.com/python/python-exercise-example99.html

# 题目：有两个磁盘文件A和B,各存放一行字母,要求把这两个文件中的信息合并(按字母顺序排列), 输出到一个新文件C中。

file1 = open('test.txt', 'r')
file2 = open('exercise97.text', 'r')

w1 = file1.read()
w2 = file2.read()

file = open('exercise99', 'w')

l = list(w1 + w2)
l.sort()
s = ''
file.write(s.join(l))

file = open('exercise99', 'r')
print(file.read())
