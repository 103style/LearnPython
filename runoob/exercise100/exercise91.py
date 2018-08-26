# http://www.runoob.com/python/python-exercise-example91.html

# 题目：时间函数举例1.

import time

print("time.time() = ",time.time())
print("time.ctime(time.time()) = ",time.ctime(time.time()))
print("time.localtime(time.time()) = ",time.localtime(time.time()))
print("time.asctime(time.localtime(time.time())) = ",time.asctime(time.localtime(time.time())))
print("time.gmtime(time.time()) = ",time.gmtime(time.time()))
print("time.asctime(time.gmtime(time.time())) = ",time.asctime(time.gmtime(time.time())))


print("time.struct_time = ",time.struct_time)


help(time.strftime)
print(time.strftime("%Y%m%D"))


#
# Commonly used format codes:
#
# %Y  Year with century as a decimal number.
# %m  Month as a decimal number [01,12].
# %d  Day of the month as a decimal number [01,31].
# %H  Hour (24-hour clock) as a decimal number [00,23].
# %M  Minute as a decimal number [00,59].
# %S  Second as a decimal number [00,61].
# %z  Time zone offset from UTC.
# %a  Locale's abbreviated weekday name.
# %A  Locale's full weekday name.
# %b  Locale's abbreviated month name.
# %B  Locale's full month name.
# %c  Locale's appropriate date and time representation.
# %I  Hour (12-hour clock) as a decimal number [01,12].
# %p  Locale's equivalent of either AM or PM.
#
# Other codes may be available on your platform.  See documentation for
# the C library strftime function.