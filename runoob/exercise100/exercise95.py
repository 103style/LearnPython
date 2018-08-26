# http://www.runoob.com/python/python-exercise-example95.html

# 题目：字符串日期转换为易读的日期格式。
from dateutil import *

dt = parser.parse("Aug 28 2015 12:00AM")
print(dt)
