#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Fundamentals of Programming (Nao Hirokawa)
Term 1-2(Q2), 2022
Lecture 9

@Author: RHIE Suyeong(2250008. M.Phil. Student in Transdisciplinary Sciences)
"""


def member(x: int, t: list):
    if not t:
        return False
    else:
        if t[1] == x: 
            return True
        elif t[1] < x:
            return member(x, t[2])
        else:
            return member(x, t[0])


def member_test():
    """Exercises
    Implement the membership function member(x, t) that checks if binary search tree t contains label x.

    t = [[[],1,[]],2,[[[],3,[]],4,[[],5,[]]]]
    """
    t = [[[],1,[]],2,[[[],3,[]],4,[[],5,[]]]]
    assert member(3, t) == True
    assert member(7, t) == False


def add(x: int, t: list):
    if not t:
        return [[], x, []]
    else:
        if t[1] == x:
            return t
        elif t[1] < x:
            t[2] = add(x, t[2])
        else:
            t[0] = add(x, t[0])
    return t


def add_test():
    """Exercises
    Implement the function add(x, t) that adds x to binary search tree t.
    """
    t = [[[],1,[]],2,[[[],3,[]],4,[[],5,[]]]]
    assert add(6, t) == [[[],1,[]], 2, [[[],3,[]], 4 ,[[],5,[[], 6, []]]]]


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

member_test()
add_test()