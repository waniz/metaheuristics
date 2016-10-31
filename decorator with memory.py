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
    if i < 2:
        return 1
    return fib(i - 1) + fib(i - 2)


@memo
def simple_factorial(number):
    if number == 1:
        return 1
    if number == 2:
        return 2
    return number * simple_factorial(number - 1)

print(fib(6))
print(simple_factorial(100))
