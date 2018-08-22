# http://www.runoob.com/python/python-exercise-example56.html

# 题目：画图，学用circle画圆形。　　　


from tkinter import *

canvas = Canvas(width=800, height=600, bg='red')
canvas.pack(expand=YES, fill=BOTH)
k = 1
j = 1
for i in range(0, 16):
    canvas.create_oval(310 - k, 250 - k, 310 + k, 250 + k, width=1)
    k += j
    j += 0.8

help(canvas.create_oval)

mainloop()
