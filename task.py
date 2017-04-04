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
def simple_factorial(number):
    if number == 1:
        return 1
    if number == 2:
        return 2
    return number * simple_factorial(number - 1)

n = 1
while True:
    n += 1
    if n % 1000 == 0:
        print('N equals %s' % n)

    if simple_factorial(n) % 2 ** n == 0:
        print('FOUND NUMBER = %s' % n)







