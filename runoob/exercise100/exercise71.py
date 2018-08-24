# http://www.runoob.com/python/python-exercise-example71.html


# 题目：编写input()和output()函数输入，输出5个学生的数据记录。

# stu
# num : string
# name : string
# score[4]: list


def input_std():
    count = int(input("请输入学生的总数："))
    res = []
    for i in range(count):
        temp = []
        temp.append(input("请输入第%d个学生的编号：" % (i + 1)))
        temp.append(input("请输入第%d个学生的名字：" % (i + 1)))
        size = int(input("请输入学生的科目总数："))
        scores = []
        for j in range(size):
            scores.append(input("请输入第%d个学生第%d门课的分数：" % (i + 1, j + 1)))
        temp.append(scores)
        res.append(temp)

    return res

def output(res):
    print(res)


output(input_std())

