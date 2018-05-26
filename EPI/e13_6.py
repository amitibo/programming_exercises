"""Render a Calendar
"""

from collections import namedtuple
import numpy as np


EndPoint = namedtuple("EndPoint", ("time", "type"))


def calc_concurrent_events(events):

    starts, ends = list(zip(*events))
    end_points = sorted([EndPoint(s, 1) for s in starts] +\
        [EndPoint(s, -1) for s in ends])
    changes = [e.type for e in end_points]

    return np.max(np.cumsum(changes))


def main():
    tests = (
        (
            (
                (4, 5), (9, 17), (2, 7), (8, 9), (12, 15), (1, 5), (6, 10), (11, 13), (14, 15)
                ),
            3
        ),
    )

    for test, ans in tests:
        bns = calc_concurrent_events(test)
        assert ans == bns, f"Not the expected answer {ans}. Got {bns}"


if __name__ == "__main__":
    main()
