#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Fundamentals of Programming (Nao Hirokawa)
Term 1-2(Q2), 2022
Lecture 8

@Author: RHIE Suyeong(2250008. M.Phil. Student in Transdisciplinary Sciences)
"""


"""Exercise: Lexical Analysis
Implement lex:
lex("repeat 5 { forward 200 rotate 144 }")
    = ["repeat", "5", "{", "forward", "200", "rotate", "144", "}"]
lex("repeat 5 {forward 200 rotate 144}")
    = ["repeat", "5", "{", "forward", "200", "rotate", "144", "}"]
lex("repeat 5 {\n forward 200\n rotate 144\n}")
    = ["repeat", "5", "{", "forward", "200", "rotate", "144", "}"]
    
Hint:
def lex(s):
    L = [] 
    i=0
    while i < len(s):
        if s[i] in [" ", "\r", "\n", "\t"]:
            i = i + 1
        elif s[i] in ["{", "}"]:
            ...
        else:
            ...
    return L
"""



"""
Write a program that reads "tokyo.csv" to generate an HTML table (left figure). (see lecture slide l8-19p)
Hint: Use float; e.g. float("12.3") = 12.3
"""


"""
Modify "triangle.pyw" to draw a star (right figure). (see lecture slide l8-19p)

File: triangle.pyw
import tkinter
from math import sin, cos
def f(a):
    return (250 + 100 * cos(a), 250 - 100 & sin(a))
root = tkinter.Tk()
canvas = tkinter.Canvas(root, width=500, height=500, bg="#fff"
canvas.pack()
(x1, y1) = f(0)
(x2, y2) = f(120 * 3.14 / 180)
(x3, y3) = f(240 * 3.14 / 180)
canvas.create_line(x1, y1, x2, y2, fill="#000")
canvas.create_line(x2, y2, x3, y3, fill="#000")
canvas.create_line(x3, y3, x1, y1, fill="#000")
root.mainloop()
"""