# http://www.runoob.com/python/python-exercise-example94.html

# 题目：时间函数举例4,一个猜数游戏，判断一个人反应快慢。

import random
import time

play_it = input('do you want to play it.(\'y\' or \'n\')')
while play_it == 'y':
    c = int(input('input a character:\n'))
    i = random.randint(0, 2 ** 32) % 100
    print(i)
    print('please input number you guess:\n')

    #  DeprecationWarning: time.clock has been deprecated in Python 3.3 and will be removed from Python 3.8: use time.perf_counter or time.process_time instead
    # start = time.clock()
    start = time.perf_counter()
    a = time.time()
    guess = int(input('input your guess:\n'))
    while guess != i:
        if guess > i:
            print('大了')
        else:
            print('小了')
        guess = int(input('input your guess:\n'))

    end = time.perf_counter()
    b = time.time()
    var = (end - start) / 18.2
    print(var)

    # print 'It took you %6.3 seconds' % time.difftime(b,a))
    if var < 15:
        print('you are very clever!')

    elif var < 25:
        print('you are normal!')

    else:
        print('you are stupid!')

    print('Congradulations')

    print('The number you guess is %d' % i)

    play_it = input('do you want to play it.')
