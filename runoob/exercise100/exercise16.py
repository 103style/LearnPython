# http://www.runoob.com/python/python-exercise-example16.html

# 题目：输出指定格式的日期。

# same as [exercise10](https://github.com/103style/LearnPython/blob/master/runoob/exercise100/exercise10.py)

import  datetime

l = datetime.datetime.now()

print(l.strftime("%Y-%m-%d"))

print(l.strftime("%c"))