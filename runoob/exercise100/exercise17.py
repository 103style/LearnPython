# http://www.runoob.com/python/python-exercise-example17.html

# 题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。

def getTypeCount(s = ''):
    word = 0
    num = 0
    space = 0
    other = 0
    for x in range(0, s.__len__()):
        temp = s[x]
        if temp.isalpha():
            word += 1
        elif temp.isdigit():
            num += 1
        elif temp.isspace():
            space += 1
        else:
            other += 1
    return word, num, space, other


s = "As1 2asd@$% %545sad s11312454"
print(getTypeCount(s))
