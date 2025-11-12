"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    assert a != 0, ZeroDivisionError
    return b / a


def log(a, b):
    if b <= 0 or a == 1:
        raise ValueError
    return log(b, a)

def exp(a, b):
    return a ** b

