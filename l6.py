#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Fundamentals of Programming (Nao Hirokawa)
Term 1-2(Q2), 2022
Lecture 6

@Author: RHIE Suyeong(2250008. M.Phil. Student in Transdisciplinary Sciences)
"""


"""Exercise: Quick Sort (Hoare 1960)
            [ ]                           if L = [ ]
qsort(L) =  qsort(L1) + [x] + qsort(L2)    if L = [x] + L′

where
    L1 =[y|y∈L′ andy􏳙x]
    L2 =[y|y∈L′ andy>x]
Note
    using notation like set comprehension
"""


"""Homework: Merge Sort
           L                      if len(L) 􏳙 1 
msort(L) = msort(L1) ⊗ msort(L2)   otherwise

where
    L = L1 + L2 with len(L1) = ⌊len(L)/2⌋
    L1 ⊗ L2 merges two sorted lists
Note
    divide problem into subproblems of same size
O(n log n)
"""


"""
Prove n3 ∈/ O(n2).
"""


"""
Implement merge(L1, L2) that computes L1 ⊗ L2.
"""


"""
Implement the merge sort algorithm msort(L).
"""


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
