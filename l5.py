#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Fundamentals of Programming (Nao Hirokawa)
Term 1-2(Q2), 2022
Lecture 5

@Author: RHIE Suyeong(2250008. M.Phil. Student in Transdisciplinary Sciences)
"""


"""
Use append to implement
myfilter(p, L) = [x ∈ L | p(x)]
which is list version of set comprehension {x ∈ L | p(x)}.
def even(x):
    return x % 2 == 0
L = [1,2,3,4,5,6]
print(myfilter(even, L)) # [2 , 4 , 6]
"""


"""
Replace even with suitable lambda expression:
print(myfilter(..., L)) # [2 , 4 , 6]
"""

"""
Use append to reimplement mymap.
def mymap(f, L):
    M = []
    for x in L:
        M = M + [f(x)]
    return M
"""


"""
Implement the list concatenation:
concat([L1,...,Ln])=L1 +···+Ln
"""


"""
Implement the function that takes two lists to return their Cartesian product.
For instance,
product([1, 2, 3], [”a”, ”b”])
= [(1, ”a”), (1, ”b”), (2, ”a”), (2, ”b”), (3, ”a”), (3, ”b”)]
"""


"""
Implement the in-place version of reverse:
L = [10, 20, 30]
reverse(L)
print(L) # [30, 20, 10]
"""


"""
Use nested for-loop to implement the bubble sort algorithm:
def bsort(L):
    for ...:
        for ...:
            if ...:
                ....
"""