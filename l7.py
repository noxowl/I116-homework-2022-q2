#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Fundamentals of Programming (Nao Hirokawa)
Term 1-2(Q2), 2022
Lecture 7

@Author: RHIE Suyeong(2250008. M.Phil. Student in Transdisciplinary Sciences)
"""


"""Exercise - Printing Solution
implement print3x3(L): >>> print3x3([2,9,4,7,5,3,6,1,8])
2   9   4
7   5   3
6   1   8
"""


"""Exercise - Testing Solution Candidates
implement ok(L) that checks
if L = [x0,...,x8] is solution:
x0  x1  x2
x3  x4  x5
x6  x7  x8

ok([2,9,4,7,5,3,6,1,8]) = True
ok([2,9,4,7,5,3,6,8,1]) = False
ok([5,5,5,5,5,5,5,5,5]) = False
"""


"""Exercise - Generating Solution Candidates
use 9-nested for-loop to implement magic square solver:
x0  x1  x2
x3  x4  x5
x6  x7  x8

for x0 in ...:
    for x1 in ...:
        ...
        for x8 in ...:
            if ...:
                print3x3 (...)
"""


"""Exercise - Quiz
identify x2, x4,...,x8

2  9  x2
7  x4  x5
x6  x7  x8
"""


"""Exercise - Optimizing Our Solver
use 3-nested for-loop to implement magic square solver:
x0  x1  *x2
x3  *x4  *x5
*x6  *x7  *x8

for x0 in ...:
    for x1 in ...:
        for x3 in ...:
            if ...:
                print3x3 (...)
"""

