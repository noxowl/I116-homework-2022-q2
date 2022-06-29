#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Fundamentals of Programming (Nao Hirokawa)
Term 1-2(Q2), 2022
Lecture 3

@Author: RHIE Suyeong(2250008. M.Phil. Student in Transdisciplinary Sciences)
"""


member = lambda x, y: [x == y[i] for i in range(len(y))]


def member_test():
    """
    Implement the membership function for lists:
                                   
    member(x, [y1, y2, ..., yn]) = True if x = yi for some i
                                   False otherwise
    :return: None
    """
    print('Test member for [1, 2, 3] with condition 1')
    assert member(1, [1, 2, 3]) == [True, False, False]
    print('OK')


gcd_sub_recursion = lambda x, y: x if x == y else gcd_sub_recursion(x - y if (x > y) else x, y - x if (x < y) else y)


def gcd_sub_while(x: int, y: int) -> int:
    while x != y:
        if x > y:
            x -= y
        else:
            y -= x
    return x


def gcd_subtraction_test():
    """Euclidean Algorithm: Subtraction Version
    gcd(x, x) = x
    gcd(x, y) = gcd(x − y, y) if x > y
    gcd(x, y) = gcd(x, y − x) if y > x

    Example
    gcd(24, 32) = gcd(24, 8) = gcd(16, 8) = gcd(8, 8) = 8

    in light of above observation, implement gcd
    1 by using recursion, and also
    2 by using while-loop
    :return: None
    """
    print('Test gcd_sub_recursion for 24, 32')
    assert gcd_sub_recursion(24, 32) == 8
    print('OK')
    print('Test gcd_sub_while for 24, 32')
    assert gcd_sub_while(24, 32) == 8
    print('OK')


gcd_rem_recursion = lambda x, y: x if not y else gcd_rem_recursion(y, x % y)


def gcd_rem_while(x: int, y: int) -> int:
    while y > 0:
        x, y = y, x % y
    return x


def gcd_remainder_test():
    """Euclidean Algorithm: Remainder Version
    gcd(x, 0) = x
    gcd(x, y) = gcd(y, x % y) if y > 0

    Example
    gcd(24, 32) = gcd(32, 24) = gcd(24, 8) = gcd(8, 0) = 8

    in light of above observation, implement gcd
    1 by using recursion
    2 by using while-loop
    :return: None
    """
    print('Test gcd_recursion for 24, 32')
    assert gcd_rem_recursion(24, 32) == 8
    print('OK')
    print('Test gcd_rem_while for 24, 32')
    assert gcd_rem_while(24, 32) == 8
    print('OK')


def bisection_test():
    """
    Use recursion to reimplement the bisection algorithm.
    if f is continuous, a < b, and f(a)f(b) < 0 then
    f(x) = 0 / for some a < x < b

    given function f and a0, b0 ∈ R with a0 < b0, we define
                   
    (an+1, bn+1) = (an, cn) if f(an)f(cn) < 0
                   (cn, bn) otherwise
    where cn = (an + bn) / 2


    def f(x):
        return x * x - 2


    def bisection(a, b):
        e = 0.00000001
        while abs(a - b) > e:
            c = (a + b) / 2
            if f(a) * f(c) <= 0:
                b = c
            else:
                a = c
        return (a + b) / 2


    print(bisection(0,3)) # 1.41421355959028
    :return: None
    """
    pass


def root_test():
    """
    Use the bisection method to implement root(z) that approximates √z, where z 0.
    Hint: Given a non-negative real number z, you have to find numbers a and b such that a <= √z <= b holds.
    You may take a = 0. What about b? Use z to construct an upper-bound b of √z.
    :return: None
    """
    pass


member_test()
gcd_subtraction_test()
gcd_remainder_test()
