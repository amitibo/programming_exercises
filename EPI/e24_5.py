"""Compute the longest contiguous increasing subarray.
"""


def longest_subarray(A):

    indices = [0, 0]

    start_idx = 0
    end_idx = 0
    max_substring_len = 0

    while end_idx < len(A) - (indices[1] - indices[0]):
        if A[end_idx+1] > A[end_idx]:
            end_idx += 1
        else:
            if end_idx - start_idx > (indices[1] - indices[0]):
                indices = [start_idx, end_idx]

            start_idx = end_idx + 1
            end_idx = start_idx + (indices[1] - indices[0])

    return indices


def main():
    A = [2, 11, 3, 5, 13, 7, 19, 17, 23]

    assert longest_subarray(A) == [2, 4], "Wrong answer"


if __name__ == "__main__":
    main()