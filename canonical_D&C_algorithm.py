from bisect import bisect_right, bisect_left


def divide_and_conquer(S, divide, combine):
    if len(S) == 1:
        return S
    L, R = divide(S)
    A = divide_and_conquer(L, divide, combine)
    B = divide_and_conquer(R, divide, combine)
    return combine(A, B)


a = [0, 2, 3, 5, 6, 8, 8, 9]
print(bisect_right(a, 5), bisect_left(a, 5))
