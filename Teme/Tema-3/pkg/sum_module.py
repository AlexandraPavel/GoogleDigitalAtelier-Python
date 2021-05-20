def sum_of_all(n):
    if n == 0:
        return 0
    return n + sum_of_all(n - 1)


def sum_even(n):
    if n == 0:
        return 0
    if n % 2 == 1:
        n = n - 1
    return n + sum_even(n - 2)


def sum_odd(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n % 2 == 0:
        n = n - 1
    return n + sum_odd(n - 2)
