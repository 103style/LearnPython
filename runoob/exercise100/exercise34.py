# http://www.runoob.com/python/python-exercise-example34.html

# 题目：练习函数调用。


def speak(content = 'hello world'):
    print(content)


def pardon(content):
    for x in range(0,2):
        speak(content)

pardon("this is just a test")