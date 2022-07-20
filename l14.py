#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Fundamentals of Programming (Nao Hirokawa)
Term 1-2(Q2), 2022
Lecture 14

@Author: RHIE Suyeong(2250008. M.Phil. Student in Transdisciplinary Sciences)
"""


"""Exercises 1: Variable Scope
What is output?

def f(x):
    if not x > 0:
        x=1
    else:
        x=2

x = 5
f(x)
print(x)

# Answer
output: x = 5
reason:
x = 5
x is variable id 1. x is 5.
f(x) x has passed to function f()

inside f(x)...
if not x > 0: -> if x < 0 so we don't need to see it.
else:
    x = 2
this x is same variable id 1. now x is 2.

but after this execution, the function is over and
new value x = 2 is discarded (you must return for save change)

now we back to outer scope and x is 5.
"""


"""Exercise 2: Destructive Updates
What is output?

L = [0,1,2]
M = L
L[1] = L[2]
M[0] = M[1]
print(L)

# Answer
output: [2, 2, 2]
reason:
L[0, 1, 2]
M = L[0, 1, 2]
M(L)[0, 1, 2], L[0, 1, 2]
L[0, '1', 2][1] <- L[0, 1, '2'][2]
L[0, 2, 2]
M(L)[0, 2, 2]
M(L)['0', 2, 2] <- M(L)[0, '2', 2]
M(L)[2, 2, 2], L[2, 2, 2]
L is [2, 2, 2]

* one more...
The lists are *mutable* and integers(Ex.1) are *immutable*
so, if you change int x value... it is new reference value.
x = 1 # x == 1
y = x # y == 1
assert (x is y) == True
x += 2 # x == 3, y == 1
assert (x is y) != True

x = [1, 2, 3] # x == [1, 2, 3]
y = x # y == [1, 2, 3]
assert (x is y) == True
x.pop() # x == [1, 2], y == [1, 2]
assert (x is y) == True

* what is assert statement?
https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement
"""


"""Exercise 3: Control Flow
What is output?

def f(x, y):
    while x < y:
        x = x - y
    return x

print(f(2018, 10))

# Answer
output: 2018
reason:
f(2018, 10) -> x = 2018, y = 10
while 2018 < 10: -> nothing to do. exit.
return 2018
"""


"""Exercise 4: Higher-Order Funcitons
What is output?

def map(f, L):
    M = []
    for x in L:
        M.append(f(x))
    return M

print(map(lambda x: x * x, [1, 2, 3]))

# Answer
output: [1, 4, 9]
"""


"""Exercise 5: Time Complexities
What is the time complexity of the following program?
Here we assume that arithmetic operations (=, +, ∗) run in O(1).

for i in range(0, n * n):
    for j in range(0, 2 * n):
        x = x + i + j

O(n)? O(n^2)? O(n^3)? O(n^4)? O(n^5)?

# Answer
Nested for loop: O(n^2)
and also n^3, n^5 are O(n^2) in Big-O notation.

O(1): Constant complexity
O(n): Linear complexity (single for loop)
O(log n): Logarithmic complexity (Binary Tree/BST)
O(n^2): Quadratic complexity (nested for loop, insertion sort, bubble sort, selection sort)
O(2^n): Exponential complexity (recurrent fibonacci(called twice at execute))
"""


"""Exercise 6: Numerical Computations
def f(x):
    return x * x

def g(d):
    return (f(1 + d) - f(1)) / d

print(g(1e-11)) # 2.000
print(g(1e-12)) # 2.000
print(g(1e-13)) # 1.998
print(g(1e-14)) # 1.998
print(g(1e-15)) # 2.220


The function g(d) approximates f′(1) by using the formula:

f′(1) ≈ frac{f(1 + d) − f(1)}{d} for enough small number d > 0.

Explain why g(1e-15) is less precise than the earlier values.

# Answer
"""


"""Exercise 7: Data Structures
We represent binary trees by nested lists. For instance,

    u = [[[ ],1,[ ]],2,[[[ ],3,[ ]],4,[[ ],5,[ ]]]]

denotes the tree:
        (2)
    (1)        (4)
            (3)    (5)

Implement depth(t) that computes the depth of binary tree t.
For instance, depth([]) = 0, depth([[],1,[]]) = 1, and depth(u) = 3.

# Answer
"""
def depth(t: list):
    if not t:
        return 0
    else:
        left = depth(t[0])
        right = depth(t[2])
        if left < right:
            return right + 1
        else:
            return left + 1


def depth_test():
    assert depth([]) == 0
    assert depth([[], 1, []]) == 1
    assert depth([[[ ],1,[ ]],2,[[[ ],3,[ ]],4,[[ ],5,[ ]]]]) == 3


"""Exercise 8: Algorithms

Implement the bubble sort function bsort(L).

L = [2,4,6,1,2,3]
bsort(L)
print(L) #[1,2,2,3,4,6]

# Answer
"""
def bsort(L: list):
    _sorted = False
    while not _sorted:
        _sorted = True
        for i in range(len(L) - 1):
            if L[i] > L[i + 1]:
                _sorted = False
                (L[i], L[i + 1]) = (L[i + 1], L[i])


def bsort_test():
    assert bsort([2,4,6,1,2,3]) == [1,2,2,3,4,6]
    L = [2,4,6,1,2,3]
    bsort(L)
    print(L)