"""Test for palindromic permutations
"""

from collections import Counter, defaultdict


def test_palindromic(s):

    words_count = defaultdict(int)

    for c in s:
        words_count[c] = words_count[c] + 1

    odd_cnt = 0
    for i in words_count.values():
        odd_cnt += i % 2

    return odd_cnt < 2


def test_palindromic_compressed(s):

    return sum(v % 2 for v in Counter(s).values()) < 2


def main():

    tests = (
        ("editi", False),
        ("edified", True)
    )

    for s, a in tests:
        assert test_palindromic(s) == a, f"Failed {s}"
        assert test_palindromic_compressed(s) == a, f"Failed {s}"


if __name__ == "__main__":
    main()

