#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Fundamentals of Programming (Nao Hirokawa)
Term 1-2(Q2), 2022
Lecture 6

@Author: RHIE Suyeong(2250008. M.Phil. Student in Transdisciplinary Sciences)
"""


"""Exercises
Suppose that we use + and × to implement:
    f(x)=x^4+2x^3+3x^2+4x+5
Find an efficient implementation of f.
"""


"""Exercises
Prove 3n^3+2n^2+6 ∈ O(n^3).
Hint: Find c, k 􏰁 0 such that
    3n^3+2n^2+6 <= cn^3
holds for all n => k.
"""


def bsort(l: list):
    index = len(l) - 1
    while index:
        for i in range(index):
            if l[i] > l[i + 1]:
                l[i], l[i + 1] = l[i + 1], l[i]
        else:
            index -= 1
    return l


bsort_lambda_joke = lambda x: exec("def bsort(x):\n  index = len(x) - 1\n  while index:\n    for i in range(index):\n      if x[i] > x[i + 1]:\n        x[i], x[i + 1] = x[i + 1], x[i]\n    else: index -= 1\n  return x; bsort({0})".format(x))


def bubble_sort_test():
    """
    def bsort(L):
        confirmed = False
        while not confirmed:
            confirmed = True
            for i in range(0, len(L) - 1):
                if L[i] > L[i+1]:
                    (L[i], L[i+1]) = (L[i+1], L[i])
                    confirmed = False

    if > and swap run in constant time
        time complexity of bsort(L) is in O(n2) for n = len(L)

    :return: None
    """
    assert bsort([4, 7, 5, 1, 3]) == [1, 3, 4, 5, 7]
    # sample = [4, 7, 5, 1, 3]
    # print(bsort_lambda_joke(sample))
    # print(sample)


def qsort(l: list):
    if len(l) <= 1: return l
    pivot = l[len(l) // 2]
    less, equal, more = [], [], []
    for x in l:
        if x > pivot:
            more.append(x)
        elif x < pivot:
            less.append(x)
        else:
            equal.append(x)
    return qsort(less) + equal + qsort(more)


def quick_sort_test():
    """Exercise: Quick Sort (Hoare 1960)
                [ ]                           if L = [ ]
    qsort(L) =  qsort(L1) + [x] + qsort(L2)    if L = [x] + L′

    where
        L1 =[y|y∈L′ andy􏳙x]
        L2 =[y|y∈L′ andy>x]
    Note
        using notation like set comprehension
    """
    assert qsort([4, 7, 5, 1, 3]) == [1, 3, 4, 5, 7]


def msort(l: list):
    if len(l) <= 1: return l
    pivot = len(l) // 2
    x = msort(l[:pivot])
    y = msort(l[pivot:])
    # merge
    _sorted = []
    while x and y:
        if x[0] < y[0]:
            _sorted.append(x.pop(0))
        else:
            _sorted.append(y.pop(0))
    _sorted.extend(x if x else y)
    return _sorted



def merge_sort_test():
    """Homework: Merge Sort
    Implement the merge sort algorithm msort(L).

               L                      if len(L) 􏳙 1
    msort(L) = msort(L1) ⊗ msort(L2)   otherwise

    where
        - L = L1 + L2 with len(L1) = ⌊len(L)/2⌋
        - L1 ⊗ L2 merges two sorted lists
    Note
        - divide problem into subproblems of same size
        - O(n log n)
    """
    assert msort([4, 7, 5, 1, 3]) == [1, 3, 4, 5, 7]
    assert msort([1, 3, 4, 5, 11, 2, 5, 7, 13]) == [1, 2, 3, 4, 5, 5, 7, 11, 13]


"""
Prove n3 ∈/ O(n2).
"""


def merge(x: list, y: list) -> list:
    _sorted = []
    while x and y:
        if x[0] < y[0]:
            _sorted.append(x.pop(0))
        else:
            _sorted.append(y.pop(0))
    _sorted.extend(x if x else y)
    return _sorted


def merge_test():
    """
    Implement merge(L1, L2) that computes L1 ⊗ L2.
    """
    assert merge([1, 3, 4, 5, 11], [2, 5, 7, 13]) == [1, 2, 3, 4, 5, 5, 7, 11, 13]


import random
import time
def sorts_test():
    """
    Create a list consisting of 10000 elements to run bsort, qsort, and msort on
    the list, and then measure their running times.

    import random
    import time
    # ...
    L = [ random.randint(0,10000) for i in range(0,10000) ]
    start = time.time()
    bsort(L)
    print(L)
    print(time.time() - start)
    """
    bsort_random_list = [random.randint(0, 10000) for i in range(0, 10000)]
    bsort_start = time.time()
    bsort(bsort_random_list)
    bsort_running_time = time.time() - bsort_start

    qsort_random_list = [random.randint(0, 10000) for i in range(0, 10000)]
    qsort_start = time.time()
    qsort(qsort_random_list)
    qsort_running_time = time.time() - qsort_start

    msort_random_list = [random.randint(0, 10000) for i in range(0, 10000)]
    msort_start = time.time()
    msort(msort_random_list)
    msort_running_time = time.time() - msort_start

    # print(f'bsort sort result: {bsort_random_list}')
    # print(f'qsort sort result: {qsort_random_list}')
    # print(f'msort sort result: {msort_random_list}')
    print(f'bsort running time: {bsort_running_time}')
    print(f'qsort running time: {qsort_running_time}')
    print(f'msort running time: {msort_running_time}')


bubble_sort_test()
quick_sort_test()
merge_sort_test()
merge_test()
sorts_test()
