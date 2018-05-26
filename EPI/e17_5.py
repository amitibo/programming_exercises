"""Find the Majority element in an array.
"""

def find_majority(A):

    candidate = None
    count = 0

    for a in A:
        if count == 0:
            candidate = a
        elif candidate == a:
            count += 1
        else:
            count -= 1

    return candidate


def main():
    tests = (
        ("bacaabaaca", "a"),
    )

    for A, t in tests:
        assert find_majority(A) == t, "Failed test: {}".format((A, t))


if __name__ == "__main__":
    main()