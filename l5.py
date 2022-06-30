#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Fundamentals of Programming (Nao Hirokawa)
Term 1-2(Q2), 2022
Lecture 5

@Author: RHIE Suyeong(2250008. M.Phil. Student in Transdisciplinary Sciences)
"""


def even(x):
    """
    function for function input test
    :param x:
    :return:
    """
    return x % 2 == 0


def myfilter(f, l: list):
    filtered = []
    for a in l:
        if f(a):
            filtered.append(a)
    return filtered


def myfilter_test():
    """
    Use append to implement
    myfilter(p, L) = [x ∈ L | p(x)]
    which is list version of set comprehension {x ∈ L | p(x)}.
    def even(x):
        return x % 2 == 0
    L = [1,2,3,4,5,6]
    print(myfilter(even, L)) # [2 , 4 , 6]
    """
    assert myfilter(even, [1, 2, 3, 4, 5, 6]) == [2, 4, 6]


def myfilter_lambda_test():
    """
    Replace even with suitable lambda expression:
    print(myfilter(..., L)) # [2 , 4 , 6]
    """
    assert myfilter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6]) == [2, 4, 6]


def mymap(f, l):
    m = []
    for x in l:
        m.append(f(x))
    return m


def mymap_test():
    """
    Use append to reimplement mymap.
    def mymap(f, L):
        M = []
        for x in L:
            M = M + [f(x)]
        return M
    """
    assert mymap(lambda x: x * 2, [1, 2, 3]) == [2, 4, 6]


def concat(l: list):
    m = 0
    for a in l:
        m += a
    return m


def list_concat_test():
    """
    Implement the list concatenation:
    concat([L1,...,Ln])=L1 +···+Ln
    """
    assert concat([1, 2, 3, 4, 5]) == 15


def product(x: list, y: list):
    m = []
    for a in x:
        for b in y:
            m.append((a, b))
    return m


def list_product_test():
    """
    Implement the function that takes two lists to return their Cartesian product.
    For instance,
    product([1, 2, 3], [”a”, ”b”])
    = [(1, ”a”), (1, ”b”), (2, ”a”), (2, ”b”), (3, ”a”), (3, ”b”)]
    """
    assert product([1, 2, 3], ["a", "b"]) == [(1, "a"), (1, "b"), (2, "a"), (2, "b"), (3, "a"), (3, "b")]


def reverse(l: list):
    size = len(l)
    for i in range(size // 2):
        # swap
        l[i], l[size - i - 1] = l[size - i - 1], l[i]
    return l


def list_in_place_reverse_test():
    """
    Implement the in-place version of reverse:
    L = [10, 20, 30]
    reverse(L)
    print(L) # [30, 20, 10]
    """
    assert reverse([10, 20, 30]) == [30, 20, 10]


def bsort(l: list) -> list:
    index = len(l) - 1
    for loop_i in range(index):
        for sort_i in range(index - loop_i):
            if l[sort_i] > l[sort_i + 1]:
                l[sort_i], l[sort_i + 1] = l[sort_i + 1], l[sort_i]
    return l


def nested_loop_bubble_sort_test():
    """
    Use nested for-loop to implement the bubble sort algorithm:
    def bsort(L):
        for ...:
            for ...:
                if ...:
                    ....
    """
    assert bsort([4, 7, 5, 1, 3]) == [1, 3, 4, 5, 7]


myfilter_test()
myfilter_lambda_test()
mymap_test()
list_concat_test()
list_product_test()
list_in_place_reverse_test()
nested_loop_bubble_sort_test()
