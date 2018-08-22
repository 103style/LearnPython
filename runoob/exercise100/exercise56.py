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


help(canvas.pack)
#
# Help on method pack_configure in module tkinter:
#
# pack_configure(cnf={}, **kw) method of tkinter.Canvas instance
#     Pack a widget in the parent widget. Use as options:
#     after=widget - pack it after you have packed widget
#     anchor=NSEW (or subset) - position widget according to
#                               given direction
#     before=widget - pack it before you will pack widget
#     expand=bool - expand widget if parent size grows
#     fill=NONE or X or Y or BOTH - fill widget if widget grows
#     in=master - use master to contain this widget
#     in_=master - see 'in' option description
#     ipadx=amount - add internal padding in x direction
#     ipady=amount - add internal padding in y direction
#     padx=amount - add padding in x direction
#     pady=amount - add padding in y direction
#     side=TOP or BOTTOM or LEFT or RIGHT -  where to add this widget.


help(mainloop)
# Help on function mainloop in module tkinter:
#
# mainloop(n=0)
#     Run the main loop of Tcl.