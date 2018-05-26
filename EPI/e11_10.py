"""Find the missing and duplicate element in an array.
"""

import functools
import random


N = 1000


def find_missing_duplicate(A):

    xor_N = functools.reduce(lambda v, i: v ^ i[0] ^ i[1], enumerate(A), 0)
    sum_N = functools.reduce(lambda v, i: v - i[0] + i[1], enumerate(A), 0)

    #
    # Find the missing bit.
    #
    missing_bit, h = xor_N & (~(xor_N - 1)), 0

    for i, a in enumerate(A):
        if i & missing_bit:
            h ^= i
        if a & missing_bit:
            h ^= a

    s = functools.reduce(lambda v, i: v+1 if i == h else v, A, 0)

    if s == 0:
        return h + sum_N, h
    else:
        return h, h - sum_N


def main():

    A = list(range(N))
    random.shuffle(A)

    idx = random.randint(0, N)
    old_value = A[idx]
    new_value = (old_value + N // 2) % N
    A[idx] = new_value

    n, o = find_missing_duplicate(A)

    assert new_value == n and old_value == o, f"{new_value} =? {n}, {old_value} =? {o}"


if __name__ == "__main__":
    main()