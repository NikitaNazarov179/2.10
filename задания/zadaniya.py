#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


def sr_geom(*args):
    if args:
        values = [float(arg) for arg in args]
        n = len(values)
        pr = 1
        k = 0
        for k in range(n):
            pr *= values[k]
            k += 1
        g = math.pow(pr, 1 / k)
        return g
    else:
        return None


def sr_garm(*args):
    if args:
        values = [float(arg) for arg in args]
        n = len(values)
        s = 0
        for k in range(n):
            s += 1/values[k]
        g = n / s
        return g
    else:
        return None


def disp(**kwargs):
    n = len(kwargs.values())
    s = sum(kwargs.values())
    sigma = 0
    min_val = min(kwargs.values())
    for k, v in kwargs.items():
        if v == min_val:
            print(f"Наименьшая переменная {k} со значением {v}")
    for a in kwargs.values():
        sigma += (a - s) ** 2
    dev = (sigma / (n - 1)) ** 0.5
    print(f"Среднеквадратическое отклонение - {dev}")


if __name__ == "__main__":
    print(sr_geom(1, 2, 3, 4))
    print(sr_garm(1, 2, 3, 4))

    print('\n')
    disp(a=1, b=2, c=3, d=6, e=4, f=2)