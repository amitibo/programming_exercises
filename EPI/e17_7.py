"""Maximum water trapped.
"""

from sortedcontainers import SortedDict


def find_maximum_trapped(A):

    left_iter =  iter(range(len(A)))
    right_iter = iter(range(len(A)-1, -1, -1))

    left = next(left_iter)
    right = next(right_iter)

    areas = SortedDict()
    while left != right:

        area = (right-left) * min(A[left], A[right])

        areas[area] = (left, right)

        if A[left] < A[right]:
            left = next(left_iter)
        else:
            right = next(right_iter)

    return areas.values()[-1]


def main():

    tests = (
        (
            (1, 2, 1, 3, 4, 4, 5, 6, 2, 1, 3, 1, 3, 2, 1, 2, 4, 1),
            (4, 16)
            ),
    )

    for A, limits in tests:

        ans = find_maximum_trapped(A)
        assert ans == limits, f"Wrong answer {ans}. Expected {limits}"


if __name__ == "__main__":
    main()