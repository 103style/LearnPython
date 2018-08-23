# http://www.runoob.com/python/python-exercise-example62.html

# 题目：查找字符串。

str = input("请输出一个字符串：")

w = input("请输入查找该字符串中的是否存在的片段：")

r = str.find(w)

if r == -1:
    print("%s中不存在%s片段" % (str, w))
else:
    print("%s中存在%s片段" %(str,w))