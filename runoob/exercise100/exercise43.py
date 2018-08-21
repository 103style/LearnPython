# http://www.runoob.com/python/python-exercise-example43.html

# 题目：模仿静态变量(static)另一案例。


class Num:
    nNum = 1

    def inc(self):
        self.nNum += 1
        print('nNum = %d' % self.nNum)


nNum = 2
inst = Num()
for i in range(3):
    nNum += 1
    print('The num = %d' % nNum)
    inst.inc()
