from functools import wraps


def memo(func):
    cache = {}

    @wraps(func)
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap


@memo
def fib(i):
    # O(2^n/2)
    if i < 2:
        return 1
    return fib(i - 1) + fib(i - 2)


def fib_modify(i):
    # O(n)
    if i <= 1:
        return i, 0
    else:
        (a, b) = fib_modify(i - 1)
    return (a + b), a


@memo
def simple_factorial(number):
    if number == 1:
        return 1
    if number == 2:
        return 2
    return number * simple_factorial(number - 1)


print(fib(100))
print(fib_modify(100)[0] + fib_modify(100)[1])
print(simple_factorial(100))
