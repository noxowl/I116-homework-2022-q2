"""
Implement the factorial function:
factorial(n) = n!
"""
factorial = lambda x: x * factorial(x - 1) if (x > 0) else 1


def factorial_test() -> None:
    print('Test factorial for 1')
    assert factorial(1) == 1
    print('OK')
    print('Test factorial for 2')
    assert factorial(2) == 2
    print('OK')
    print('Test factorial for 4')
    assert factorial(4) == 24
    print('OK')
    print('Test factorial for 5')
    assert factorial(5) == 120
    print('OK')


"""
Implement fib(n) that computes the n-th Fibonacci number:
"""
fib = lambda n: n if n < 2 else fib(n - 1) + fib(n - 2)


def fib_test() -> None:
    print('Test fib for 0')
    assert fib(0) == 0
    print('OK')
    print('Test fib for 2')
    assert fib(2) == 1
    print('OK')
    print('Test fib for 3')
    assert fib(3) == 2
    print('OK')
    print('Test fib for 7')
    assert fib(7) == 13
    print('OK')


factorial_test()
fib_test()
