#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Fundamentals of Programming (Nao Hirokawa)
Term 1-2(Q2), 2022
Exam 2021

@Author: RHIE Suyeong(2250008. M.Phil. Student in Transdisciplinary Sciences)
"""


"""Question 1:
Consider the following function on natural numbers:

def f(n):
    i=0
    k = 2 * n * n
    while k > 0:
        k = k - n
        i = i + 1
    return i

(a) Assuming that arithmetic operations take constant time,
we consider the time complexity of the function f on natural numbers:
Which of the following statements is correct? Indicate its number. (No justification is required.)

    (1) The time complexity of f(n) is in O(n) but not in O(1).
    (2) The time complexity of f(n) is in O(n^2) but not in O(n).
    (3) The time complexity of f(n) is in O(2n^2) but not in O(n^2).
    (4) The time complexity of f(n) is in O(4n^2) but not in O(2n^2).


(b) Write down a closed formula (e.g. 2n^3 + 3) that expresses f(n). (No justification is required.)

"""


"""Question 2:
Use recursion to re-implement the following function on natural numbers. Do not use for/while-loops.

def f(x):
    k=0
    while x > 0:
        x = x // 2
        k=k+1
    return k

Note that x//y computes the quotient of x and y. E.g. 30//3 = 10 and 31//3 = 10.
"""
f = lambda x: f(x // 2) + 1 if x > 0 else 0


"""Question 3:
Use for-loop to re-implement the following function. Do not use recursion.

def f(L, x):
    if L == []:
        return []
    M = f(L[1:], x)
    if L[0] > x:
        M.append(L[0])
    return M

Answer:
the function f is
'drop the elements which is smaller than x' (a > x)
'and reverse the list' M = f(L([1:], x))
"""
def f(L, x):
    M = []
    for i in range(len(L)):
        a = L.pop()
        if a > x:
            M.append(a)
    return M
print(f([3, 6, 1, 2, 3, 4, 5], 3))


"""Question 4:
Assume that we represent binary trees by nested lists as in our course.
The mirror image of a binary tree t is the tree resulting from swapping the left and
right branches of each node. The function mirror(t) destructively updates a given
binary tree t to the mirror image of t.

Implement mirror(t) in an in-place style. For instance, we have:

t = [[[], 1, [[], 2, []]], 3, [[], 4, []]]
mirror(t)
print(t)  # [[[], 4, []], 3, [[[], 2, []], 1, []]]

Intuitively, these correspond to the following figures:

    (3)            (3)
(1)    (4)      (4)    (1)
  (2)                (2)
"""
def mirror(t: list):
    if not t:
        return t
    else:
        (t[0], t[2]) = (mirror(t[2]), mirror(t[0]))
        return t
assert mirror([[[], 1, [[], 2, []]], 3, [[], 4, []]]) == [[[], 4, []], 3, [[[], 2, []], 1, []]]
print(mirror([[[], 1, [[], 2, []]], 3, [[], 4, []]]))


"""Qustion 5:
Implement the function segments([y1, y2, . . . , yn]) that returns the list consisting ofall sublists of form
[yk,yk+1,...,ym], where k and m are natural numbers with 1 <= k <= m <= n.
For example, segments([1, 2, 3]) = [[1], [1, 2], [1, 2, 3], [2], [2, 3], [3]]

holds. Note that the sublists need not to be listed in the above order.
"""
def segments(L: list):
    M = []
    for i in range(len(L)):
        temp = [L[i]]
        M.append(temp[:])
        if i < len(L):
            for j in range(i + 1, len(L)):
                temp.append(L[j])
                M.append(temp[:])
    return M
assert segments([1, 2, 3]) == [[1], [1, 2], [1, 2, 3], [2], [2, 3], [3]]
print(segments([1, 2, 3]))


"""Qustion 6:
Given a directed graph (V,E), a vertex x ∈ V is called a root if every vertex y ∈ V is reachable from
x, i.e., x=y or there exists a sequence z1,...,zn with n => 2 such that
x = z1, y = zn, and (z1, z2), (z2, z3), . . . , (zn−1, zn) ∈ E.
Let A be an adjacency list.

Implement root(A, x) that returns True if a vertex x is a root of the directed graph represented by A,
and False otherwise. For instance, we have:

A = { 1: [1,2,5], 2: [6],     3: [2],
      4: [1],     5: [2,4,6], 6: [3] }

print(root(A,1)) # True
print(root(A,2)) # False
print(root(A,3)) # False
print(root(A,4)) # True
print(root(A,5)) # True
print(root(A,6)) # False
"""