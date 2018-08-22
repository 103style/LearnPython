# http://www.runoob.com/python/python-exercise-example57.html

# 题目：画图，学用line画直线。


from tkinter import *

canvas = Canvas(width=400, height=400, bg='blue')
canvas.pack(expand=YES, fill=BOTH)
x0 = 0
y0 = 0
x1 = 200
y1 = 0
for i in range(20):
    canvas.create_line(x0, y0, x1, y1, width=1, fill='white')
    x0 = x0 + 5
    y0 = y0 + 5
    x1 = x1 + 5
    y1 = y1 + 5

canvas.create_line(x0, y0, x1, y1, width=1, fill='red')

for i in range(20):
    x0 = x0 - 5
    y0 = y0 + 5
    x1 = x1 - 5
    y1 = y1 + 5
    canvas.create_line(x0, y0, x1, y1, fill='black')

mainloop()
