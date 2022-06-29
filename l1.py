#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Fundamentals of Programming (Nao Hirokawa)
Term 1-2(Q2), 2022
Lecture 1

@Author: RHIE Suyeong(2250008. M.Phil. Student in Transdisciplinary Sciences)
"""


def python_test():
    """
    Set up Python and editor. Important!
    """
    print('Can you execute this code?')
    print('Hello world!')
    print('OK')


factorial = lambda x: x * factorial(x - 1) if (x > 0) else 1


def factorial_test() -> None:
    """
    Implement the factorial function:
    factorial(n) = n!
    """
    print('Test factorial for 1')
    assert factorial(1) == 1
    print('OK')
    print('Test factorial for 2')
    assert factorial(2) == 2
    print('OK')
    print('Test factorial for 4')
    assert factorial(4) == 24
    print('OK')
    print('Test factorial for 5')
    assert factorial(5) == 120
    print('OK')


fib = lambda n: n if n < 2 else fib(n - 1) + fib(n - 2)


def fib_test() -> None:
    """
    Implement fib(n) that computes the n-th Fibonacci number:
    """
    print('Test fib for 0')
    assert fib(0) == 0
    print('OK')
    print('Test fib for 2')
    assert fib(2) == 1
    print('OK')
    print('Test fib for 3')
    assert fib(3) == 2
    print('OK')
    print('Test fib for 7')
    assert fib(7) == 13
    print('OK')


def for_loop():
    x = 1
    s = 1
    for i in range(0, 4):
        x = x + x * s
        s = - s
    return x, s


def unfold_for_loop():
    x = 1
    # x = 1
    s = 1
    # x = 1, s = 1
    # loop 0
    x = 1 + 1 * 1
    # x = 2, s = 1
    s = - 1
    # x = 2, s = -1
    # loop 1
    x = 2 + 2 * -1
    # x = 0, s = -1
    s = - -1
    # x = 0, s = 1
    # loop 2
    x = 0 + 0 * 1
    # x = 0, s = 1
    s = - 1
    # x = 0, s = -1
    # loop 3
    x = 0 + 0 * 1
    # x = 0, s = -1
    s = - -1
    # x = 0, s = 1
    return x, s


def for_loop_with_analyzing():
    x = 1
    # x = 1
    s = 1
    # x = 1, s = 1
    # loop 0
    x = x + x * s
    # x = 2, s = 1
    s = - s
    # x = 2, s = -1
    # loop 1
    x = x + x * s
    # x = 0, s = -1
    s = - s
    # x = 0, s = 1
    # loop 2
    x = x + x * s
    # x = 0, s = 1
    s = - s
    # x = 0, s = -1
    # loop 3
    x = x + x * s
    # x = 0, s = -1
    s = - s
    # x = 0, s = 1
    return x, s


def unfold_for_loop_test():
    """
    Consider the following program:
        x=1
        s=1
        for i in range(0, 4):
            x = x + x * s
            s = - s
    1. Unfold for-loop, as we did on slide 20.
    slide 20:
        for i in range(0, 4):
            x = i * 10
            print(i, x)
        is unfolded to equivalent code:
            x = 0 * 10
            print(0, x)
            x = 1 * 10
            print(1, x)
            x = 2 * 10
            print(2, x)
            x = 3 * 10
            print(3, x)
    2. Analyze variable assignments for the unfolded code, as we did on slide 16.
    slide 16:
        x=1
        #x=1
        y=2
        # x = 1, y = 2
        z=x
        # x = 1, y = 2, z = 1
        x=y
        # x = 2, y = 2, z = 1
        y=z
        # x = 2, y = 1, z = 1
        print(x, y)
    :return: None
    """
    print('Test unfold_for_loop')
    assert unfold_for_loop() == for_loop()
    print('OK')


leibniz = lambda x: x # later


def leibniz_test():
    """
    Recall the Leibniz formula:
        π = 4−4/3+4/5−4/7+4/9−4/11 + ···
    Implement leibniz(n) that sums up the first n fractional numbers in the formula. For instance,
        leibniz(4) = 4-4/3+4/5-4/7
    :return: None
    """
    print('Test leibniz for 4')
    leibniz(4)
    print('OK')


python_test()
factorial_test()
fib_test()
unfold_for_loop_test()
leibniz_test()
