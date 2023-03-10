#!/usr/bin/python3
def raise_exception():
    x = "27"
    y = 789
    if not isinstance(x, int) or not isinstance(y, int):
        raise TypeError("x and y must be integers")
