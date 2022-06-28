#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Fundamentals of Programming (Nao Hirokawa)
Term 1-2(Q2), 2022
Lecture 9

@Author: RHIE Suyeong(2250008. M.Phil. Student in Transdisciplinary Sciences)
"""


"""Exercises
Implement the membership function member(x, t) that checks if binary search tree t contains label x.
"""


"""Exercises
Implement the function add(x, t) that adds x to binary search tree t.
"""


"""Exercises
implement succ(A, x) that lists all reachable vertices from vertex x in graph represented by adjacency list A

succ(A, 2) is computed in following way:
next(A, [2]) = [2, 1, 3]
next(A, [2, 1, 3]) = [2, 1, 3, 4, 5]
next(A,[2,1,3,4,5]) = [2,1,3,4,5] *fixed point*
∴ succ(A,2) = [2,1,3,4,5]
"""


"""
Implement delete(x, t) for binary search trees.
"""


"""
Complete making algorithm version of succ(A, x):
def succ(A, x):
    M = []
    W = [x]
    while W != []:
        u = W.pop()
        ...
        for v in ...:
            ...
    return M
"""