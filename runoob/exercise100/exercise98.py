# http://www.runoob.com/python/python-exercise-example98.html

# 题目：从键盘输入一个字符串，将小写字母全部转换成大写字母，然后输出到一个磁盘文件"test"中保存。

fp = open('test.txt', 'w')
string = input('please input a string:')
string = string.upper()
fp.write(string)
fp = open('test.txt', 'r')
print(fp.read())
fp.close()
