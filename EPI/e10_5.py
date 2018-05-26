"""Compute the median for online data.
"""

from collections import namedtuple
from sortedcontainers import SortedList


def calculate_the_median(stream):

    running_median = [stream[0]]

    sorted_stream = SortedList()
    sorted_stream.add(stream[0])
    median_index = 0

    for s in stream[1:]:
        sorted_stream.add(s)

        if len(sorted_stream) % 2 == 1:
            median_index += 1
            running_median.append(sorted_stream[median_index])
        else:
            running_median.append((sorted_stream[median_index]+sorted_stream[median_index+1])/2)

    return running_median


def main():

    tests = (
        (
            [1, 0,   3, 5, 2, 0,   1],
            [1, 0.5, 1, 2, 2, 1.5, 1]
        ),
    )

    for test, ans in tests:
        b = calculate_the_median(test)
        assert ans == b, f"Wrong answer {b}, expected {ans}"


if __name__ == "__main__":
    main()
