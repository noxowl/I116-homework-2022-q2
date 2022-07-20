#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Fundamentals of Programming (Nao Hirokawa)
Term 1-2(Q2), 2022
Lecture 8

@Author: RHIE Suyeong(2250008. M.Phil. Student in Transdisciplinary Sciences)
"""


def lex(s: str) -> list:
    blank = [" ", "\r", "\n", "\t"]
    braces = ["{", "}"]
    result = []
    i = 0
    while i < len(s):
        if s[i] in blank:
            i += 1
        elif s[i] in braces:
            result.append(s[i])
            i += 1
        else:
            j = i
            while i < len(s):
                if s[i] in blank + braces:
                    break
                i = i + 1
            result.append(s[j:i])
    return result


def lex_test():
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
    assert lex("repeat 5 { forward 200 rotate 144 }") \
        == ["repeat", "5", "{", "forward", "200", "rotate", "144", "}"]
    assert lex("repeat 5 {forward 200 rotate 144}") \
        == ["repeat", "5", "{", "forward", "200", "rotate", "144", "}"]
    assert lex("repeat 5 {\n forward 200\n rotate 144\n}") \
        == ["repeat", "5", "{", "forward", "200", "rotate", "144", "}"]


def html_generation():
    """
    Write a program that reads "tokyo.csv" to generate an HTML table (left figure). (see lecture slide l8-19p)
    Hint: Use float; e.g. float("12.3") = 12.3
    """
    with open('tokyo.csv') as f:
        pass
        # use HTMLGenerator in l4.py


import tkinter
from math import sin, cos
def draw_star():
    """
    Modify "triangle.pyw" to draw a star (right figure). (see lecture slide l8-19p)

    File: triangle.pyw
        import tkinter
        from math import sin, cos
        def f(a):
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
    f = lambda x: (250 + 100 * cos(x), 250 - 100 * sin(x))
    tk = tkinter.Tk()
    canvas = tkinter.Canvas(tk, width=500, height=500, bg='#fff')
    canvas.pack()
    (x1, y1) = f(144 * 0 * 3.14 / 180)
    (x2, y2) = f(144 * 1 * 3.14 / 180)
    (x3, y3) = f(144 * 2 * 3.14 / 180)
    (x4, y4) = f(144 * 3 * 3.14 / 180)
    (x5, y5) = f(144 * 4 * 3.14 / 180)
    canvas.create_line(x1, y1, x2, y2, fill="#000")
    canvas.create_line(x2, y2, x3, y3, fill="#000")
    canvas.create_line(x3, y3, x4, y4, fill="#000")
    canvas.create_line(x4, y4, x5, y5, fill="#000")
    canvas.create_line(x5, y5, x1, y1, fill="#000")
    tk.mainloop()


lex_test()
draw_star()
