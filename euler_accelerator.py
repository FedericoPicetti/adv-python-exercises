"""This module contains the Euler Accelerator for series.
It also implements two generators for series converging to pi and e."""

def pi_series():
    sum = 4
    div = 1
    while True:
        yield sum
        div += 2
        sum -= 4 / div
        yield sum
        div += 2
        sum += 4 / div


def e_series():
    s = 1
    i = 0
    fact = 1
    while True:
        yield s
        i += 1
        fact *= i
        s += 1 / fact


def firstn(g, n):
    for i in range(n):
        yield next(g)


def euler_accelerator(g):
    a = next(g)
    b = next(g)
    c = next(g)
    while True:
        yield c - ((c - b) ** 2) / (a - 2 * b + c)
        a = b
        b = c
        c = next(g)


if __name__ == '__main__':
   print("exact value for pi :- {0:.16}".format(3.14159265358979))
   print("old(pi) :-", list(firstn(pi_series(), 7)))
   print("new(pi) :-", list(firstn(euler_accelerator(pi_series()), 7)))
   print("exact value for e :- {0:.16}".format(2.71828182845904))
   print("old(e) :-", list(firstn(e_series(), 7)))
   print("new(e) :-", list(firstn(euler_accelerator(e_series()), 7)))
