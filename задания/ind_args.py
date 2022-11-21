#!/usr/bin/env python3
# -*- coding^ utf-8 -*-


def sum_after_positive(*args):
    """""
    Сумму аргументов, расположенных 
    после первого положительного аргумента.
    """""
    if args:
        pos = 0
        summ = 0
        print(args)
        for i in args:
            if i > 0:
                pos = i
        for i in args[pos+2:]:
           summ += i
        return summ
    else:
        return None


if __name__ == '__main__':
    print(sum_after_positive(-1, -45, -34, -567, -4, -47, 1, 7, 8, 5, -1))
