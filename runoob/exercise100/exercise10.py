# http://www.runoob.com/python/python-exercise-example10.html

# 题目：暂停一秒输出，并格式化当前时间。

import time
import datetime

l = datetime.datetime.now()
print(l)
time.sleep(1)

# 格式化为：  YYYY-MM-DD
print('YYYY-MM-DD为： ',l.strftime("%Y-%m-%d"))

# 格式化为：  YYYY-MM-DD HH:MM:SS
print('YYYY-MM-DD HH:MM:SS为： ',l.strftime("%Y-%m-%d %H:%M:%S"))

# 年月日 时分秒 星期简写
print('年月日 时分秒 星期简写 为： ',l.strftime("%Y-%m-%d %H:%M:%S %a"))

# 年月日 时分秒 星期全拼
print('年月日 时分秒 星期全拼 为： ',l.strftime("%Y-%m-%d %H:%M:%S %A"))

# 标准的日期格式串
print('标准的日期格式串为： ',l.strftime("%c"))

# 年份前面两位数字
print('年份前面两位数字为： ',l.strftime("%C"))

# 十进制表示的每月的第几天
print('十进制表示的每月的第几天为： ',l.strftime("%d"))

# 月/天/年
print('月/天/年为： ',l.strftime("%D"))

# 在两字符域中，十进制表示的每月的第几天
print('在两字符域中，十进制表示的每月的第几天为： ',l.strftime("%e"))

# 年-月-日
print('年-月-日为： ',l.strftime("%F"))

# 年份的后两位数字，使用基于周的年
print('年份的后两位数字，使用基于周的年为： ',l.strftime("%g"))

# 年分，使用基于周的年
print('年分，使用基于周的年为： ',l.strftime("%G"))

# 简写的月份名
print('简写的月份名为： ',l.strftime("%h"))

# 24小时制的小时
print('24小时制的小时为： ',l.strftime("%H"))

# 12小时制的小时
print('12小时制的小时为： ',l.strftime("%I"))

# 十进制表示的每年的第几天
print('十进制表示的每年的第几天 为： ',l.strftime("%j"))


# 格式化参数

# %a 星期几的简写
# %A 星期几的全称
# %b 月分的简写
# %B 月份的全称
# %c 标准的日期的时间串
# %C 年份的前两位数字
# %d 十进制表示的每月的第几天
# %D 月/天/年
# %e 在两字符域中，十进制表示的每月的第几天
# %F 年-月-日
# %g 年份的后两位数字，使用基于周的年
# %G 年分，使用基于周的年
# %h 简写的月份名
# %H 24小时制的小时
# %I 12小时制的小时
# %j 十进制表示的每年的第几天
# %m 十进制表示的月份
# %M 十时制表示的分钟数
# %n 新行符
# %p 本地的AM或PM的等价显示
# %r 12小时的时间
# %R 显示小时和分钟：hh:mm
# %S 十进制的秒数
# %t 水平制表符
# %T 显示时分秒：hh:mm:ss
# %u 每周的第几天，星期一为： 第一天 （值从0到6，星期一为： 0）
# %U 第年的第几周，把星期日做为： 第一天（值从0到53）
# %V 每年的第几周，使用基于周的年
# %w 十进制表示的星期几（值从0到6，星期天为： 0）
# %W 每年的第几周，把星期一做为： 第一天（值从0到53）
# %x 标准的日期串
# %X 标准的时间串
# %y 不带世纪的十进制年份（值从0到99）
# %Y 带世纪部分的十制年份
# %z，%Z 时区名称，如果不能得到时区名称则返回空字符。
# %% 百分号
