#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from array import array

def double_preceding(x: array) -> None:
    """Transforms the array by setting x[i] = 2 * x[i-1] and x[0] = 0.

    >>> x = array('i', [5, 10, 15])
    >>> double_preceding(x)
    >>> x
    array('i', [0, 10, 20])
    """

    if x:
        for i in range(-1, -len(x), -1):
            x[i] = 2 * x[i - 1]
        x[0] = 0

