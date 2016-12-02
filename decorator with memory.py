from functools import wraps


def cache(func):
    cacher = {}

    @wraps(func)
    def wrap(*args):
        if args not in cacher:
            cacher[args] = func(*args)
        return cacher[args]
    return wrap


@cache
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


@cache
def simple_factorial(number):
    if number == 1:
        return 1
    if number == 2:
        return 2
    return number * simple_factorial(number - 1)


print(fib(100))
print(fib_modify(100)[0] + fib_modify(100)[1])
print(simple_factorial(200))
