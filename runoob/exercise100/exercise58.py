# http://www.runoob.com/python/python-exercise-example58.html

# 题目：画图，学用rectangle画方形。　　　


from tkinter import *

help(Canvas.create_rectangle)
# rectangle(int left, int top, int right, int bottom)
# 参数说明：(left ，top )为矩形的左上坐标，(right,bottom)为矩形的右下坐标，两者可确定一个矩形的大小


root = Tk()
root.title('Canvas')

canvas = Canvas(width=600, height=600, bg='green')
x0 = 100
y0 = 100
y1 = 500
x1 = 500
for i in range(40):
    canvas.create_rectangle(x0, y0, x1, y1)
    x0 += 5
    y0 += 5
    x1 -= 5
    y1 -= 5

canvas.pack()
root.mainloop()
