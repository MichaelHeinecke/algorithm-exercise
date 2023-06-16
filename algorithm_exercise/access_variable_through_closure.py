"""
cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last
element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4))
returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

Implement car and cdr.
"""
from typing import Callable


def cons(a, b) -> Callable:
    def pair(f):
        return f(a, b)
    return pair


def car(func: Callable) -> Callable:
    def return_left(left, right):
        return left
    return func(return_left)


def cdr(func: Callable) -> Callable:
    def return_right(left, right):
        return right
    return func(return_right)
