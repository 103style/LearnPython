# http://www.runoob.com/python/python-exercise-example63.html

# 题目：画椭圆。　


# 椭圆（Ellipse）是平面内到定点F1、F2的距离之和等于常数（大于|F1F2|）的动点P的轨迹，F1、F2称为椭圆的两个焦点。其数学表达式为：|PF1|+|PF2|=2a（2a>|F1F2|）。 [1]

# 当焦点在x轴时，椭圆的标准方程是：x^2/a^2+y^2/b^2=1，(a>b>0)；
# 当焦点在y轴时，椭圆的标准方程是：y^2/a^2+x^2/b^2=1，(a>b>0)；
# 其中a^2-c^2=b^2
# 推导:PF1+PF2>F1F2(P为椭圆上的点 F为焦点)

from tkinter import *

root = Tk()
root.title("椭圆联系")
canvas = Canvas(width=600, height=600, bg='red')

help(canvas.create_oval)
canvas.create_oval(120, 20, 280,40)


top = 130
bottom = 130

for i in range(20):
    canvas.create_oval(250 - top, 250 - bottom, 250 + top, 250 + bottom)
    top -= 5
    bottom += 5



canvas.pack()

root.mainloop()
