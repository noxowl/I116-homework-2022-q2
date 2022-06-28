#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Fundamentals of Programming (Nao Hirokawa)
Term 1-2(Q2), 2022
Lecture 3

@Author: RHIE Suyeong(2250008. M.Phil. Student in Transdisciplinary Sciences)
"""


"""
Implement the membership function for lists: 
							   
member(x, [y1, y2, ..., yn]) = True if x = yi for some i
							   False otherwise
"""


"""
gcd(x, 0) = x
gcd(x, y) = gcd(y, x % y) if y > 0

Example
gcd(24, 32) = gcd(32, 24) = gcd(24, 8) = gcd(8, 0) = 8

in light of above observation, implement gcd
1 by using recursion
2 by using while-loop
"""


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
"""


"""
Use the bisection method to implement root(z) that approximates √z, where z 0.
Hint: Given a non-negative real number z, you have to find numbers a and b such that a <= √z <= b holds. 
You may take a = 0. What about b? Use z to construct an upper-bound b of √z.
"""

