"""Compute the Greatest Common Divisior.
"""

import collections
import copy
import random
from tqdm import trange


def calc_GCD_slow(x, y):

    while x > y:
        x = x - y

    if x == y:
        return x
    else:
        return calc_GCD(y, x)


def calc_GCD(x, y):

    if x == y:
        return x

    if x & 1 == 0 and y & 1 == 0:
        return calc_GCD(x >> 1, y >> 1) << 1

    if x & 1 == 0:
        x = x >> 1
    elif y & 1 == 0:
        y = y >> 1

    if x > y:
        return calc_GCD(y, x-y)
    else:
        return calc_GCD(y-x, x)


def main():
    print(calc_GCD(24, 300))


if __name__ == "__main__":
    main()