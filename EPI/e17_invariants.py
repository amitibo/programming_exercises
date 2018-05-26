"""
2-SUM
-----
"""


def has_two_sum(A, t):

    A = sorted(A)

    while len(A) > 0:
        e = A[0] + A[-1]

        if e == t:
            return True

        if e < t:
            A.pop(0)
        else:
            A.pop()

    return False


def main():

    tests = (
        (((-2, 1, 2, 4, 7, 11), 0), True),
        (((-2, 1, 2, 4, 7, 11), 6), True),
        (((-2, 1, 2, 4, 11, 7), 13), True),
        (((-2, 1, 2, 4, 7, 11), 10), False),
    )

    for (A, t), outcome in tests:
        assert has_two_sum(A, t) == outcome, "Failed test: {}".format((A, t, outcome))

if __name__ == "__main__":
    main()