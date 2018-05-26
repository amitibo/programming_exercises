"""Compute the maximum product of all entries but one.
"""

import functools


def compute_max_product(A):

    min_idx = None
    negative_num = 0
    min_negative_idx = None

    for i, a in enumerate(A):
        if a < 0:
            negative_num += 1
            if min_negative_idx is None or a > A[min_negative_idx]:
                min_negative_idx = i
        elif min_idx is None or a < A[min_idx]:
            min_idx = i

    if negative_num % 2 == 0:
        remove_idx = min_idx
    else:
        remove_idx = min_negative_idx

    return functools.reduce(
        lambda a, b: a*b,
        (a for i, a in enumerate(A) if i != remove_idx)
    )


def main():
    A = [3, 2, -1, 4, -1, 6]

    assert compute_max_product(A) == 72, "wrong answer."


if __name__ == "__main__":
    main()