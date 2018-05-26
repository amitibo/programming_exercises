"""Computing an Alternation
"""

from itertools import chain


def alternation(a):
    a = sorted(a)
    mid = len(a) // 2
    return list(chain(*zip(a[:mid], a[-1:mid-1:-1])))


def main():
    tests = (
        (
            list(range(20)),
            [0, 19, 1, 18, 2, 17, 3, 16, 4, 15, 5, 14, 6, 13, 7, 12, 8, 11, 9, 10]
        ),
    )

    for test, ans in tests:
        bns = alternation(test)
        assert ans == bns, f"Not the expected answer {ans}. Got {bns}"


if __name__ == "__main__":
    main()
