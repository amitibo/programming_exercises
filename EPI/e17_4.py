"""
3-SUM
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


def has_three_sum(A, t):

    A = sorted(A)

    return any(has_two_sum(A, t - a) for a in A)


def main():

    tests = (
        (((11, 2, 5, 7, 3), 21), True),
        (((11, 2, 5, 7, 3), 22), False),
    )

    for (A, t), outcome in tests:
        assert has_three_sum(A, t) == outcome, "Failed test: {}".format((A, t, outcome))

if __name__ == "__main__":
    main()