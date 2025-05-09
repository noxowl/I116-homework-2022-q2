#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Fundamentals of Programming (Nao Hirokawa)
Term 1-2(Q2), 2022
Lecture 2

@Author: RHIE Suyeong(2250008. M.Phil. Student in Transdisciplinary Sciences)
"""

from functools import reduce
average = lambda l: reduce(lambda x, y: x + y, l) / len(l)


def average_test() -> None:
    """
    implement average function:
    average([x1,x2,...,xn])= x1+x2+···+xn/n
    where, n > 0
    """
    print('Test average for [1, 2, 3, 4]')
    assert average([1, 2, 3, 4]) == 2.5
    print('OK')
    print('Test average for [0, 2, 3, 4]')
    assert average([0, 2, 3, 4]) == 2.25
    print('OK')


cal_double = lambda l: [x * 2 for x in l]


def double_test() -> None:
    """
    Implement the following function:
    double([x1,x2,...,xn]) = [2x1,2x2,...,2xn]
    """
    print('Test cal_double for [1, 2, 3, 4]')
    assert cal_double([1, 2, 3, 4]) == [2, 4, 6, 8]
    print('OK')


def matrix_addition(x: list, y: list) -> list:
    if len(x) != len(y): raise IndexError
    result = []
    for ri in range(len(x)):
        if len(x[ri]) != len(y[ri]): raise IndexError
        result.append([x[ri][ci] + y[ri][ci] for ci in range(len(x[ri]))])
    return result


def matrix_addition_test() -> None:
    """
    Implement matrix addition.
    """
    print('Test matrix_addition for [[1, 2], [3, 4]]')
    assert matrix_addition([[1, 2], [3, 4]], [[1, 2], [3, 4]]) == [[2, 4], [6, 8]]
    print('OK')
    print('Test matrix_addition for [[1, 2], [3, 4, 5]]')
    try:
        assert isinstance(matrix_addition([[1, 2], [3, 4]], [[1, 2], [3, 4, 5]]),
                          list) is False, 'IndexError not occurred. Failed.'
    except IndexError:
        print('IndexError raised. OK')


reverse = lambda l: [l.pop() for i in range(len(l))]


def reverse_test() -> None:
    """
    Implement the list reversing function reverse:
    reverse([1, 2, 3]) = [3, 2, 1]
    """
    print('Test reverse for [1, 2, 3]')
    assert reverse([1, 2, 3]) == [3, 2, 1]
    print('OK')


palindrome = lambda l: ''.join(l) == ''.join(l[::-1])


def palindrome_test() -> None:
    """
    Implement the function palindrome(L) that checks if the list L and the reversed version of L are identical:
    palindrome([”a”, ”n”, ”n”, ”a”]) = True
    palindrome([”a”, ”p”, ”p”, ”l”, ”e”]) = False
    """
    print('Test palindrome for ["a", "n", "n", "a"]')
    assert palindrome(["a", "n", "n", "a"]) is True
    print('OK')

    print('Test palindrome for ["a", "p", "p", "l", "e"]')
    assert palindrome(["a", "p", "p", "l", "e"]) is False
    print('OK')


ascending = lambda l: next(
    filter(lambda x: x is False, [l[i] <= l[i + 1 if i < len(l) - 1 else i] for i in range(len(l))]), True)


def ascending_test() -> None:
    """
    A list [x1, x2, . . . , xn] over numbers is called ascending if
    x1 <= x2 <= ··· <= xn holds. Implement the function ascending(L) that decides if the list L is ascending. E.g.,
    ascending([2, 4, 7]) = True
    ascending([2, 4, 7, 3]) = False
    """
    print('Test ascending for [2, 4, 7]')
    assert ascending([2, 4, 7]) is True
    print('OK')

    print('Test ascending for [9, 3, 7, 7, 9]')
    assert ascending([9, 3, 7, 7, 9]) is False
    print('OK')

    print('Test ascending for [2, 4, 7, 3]')
    assert ascending([2, 4, 7, 3]) is False
    print('OK')


from functools import reduce
maximum = lambda l: reduce(lambda x, y: x if (x > y) else y, l)


def maximum_test() -> None:
    """
    Implement maximum([x1, x2, . . . , xn]) that computes max{x1, x2, . . . , xn}.
    """
    print('Test maximum for [1, 2, 3]')
    assert maximum([1, 2, 3]) == 3
    print('OK')


join = lambda x, y: f'{y}'.join(x)


def join_test() -> None:
    """
    Implement the function join(L, s) that concatenates all elements in list L,
    separating with string s:
    join([”123”, ”45”, ”67”], ”ab”) = ”123ab45ab67”
    join([ ], ”, ”) = ””
    join([”a”], ” + ”) = ”a”
    join([”a”, ”b”], ” + ”) = ”a + b”
    join([”a”, ”b”, ”c”], ” + ”) = ”a + b + c”
    """
    print('Test join for ["123", "45", "67"] and "ab"')
    assert join(["123", "45", "67"], "ab") == "123ab45ab67"
    print('OK')

    print('Test join for [] and ","')
    assert join([], ",") == ""
    print('OK')

    print('Test join for ["a"] and "+"')
    assert join(["a"], "+") == "a"
    print('OK')

    print('Test join for ["a", "b"] and "+"')
    assert join(["a", "b"], "+") == "a+b"
    print('OK')

    print('Test join for ["a", "b", "c"], "+"')
    assert join(["a", "b", "c"], "+") == "a+b+c"
    print('OK')


average_test()
double_test()
matrix_addition_test()
reverse_test()
palindrome_test()
ascending_test()
maximum_test()
join_test()
