"""Find the k-th largest element.
"""

import operator
import random


def find_k_largest(A, k):

    def find_new_pivot(left, right, pivot_idx):

        new_pivot_idx = left
        pivot_value  = A[pivot_idx]
        A[right], A[pivot_idx] = A[pivot_idx], A[right]

        for i in range(left, right):
            if A[i] > pivot_value:
                A[i], A[new_pivot_idx] = A[new_pivot_idx], A[i]
                new_pivot_idx += 1

        A[new_pivot_idx], A[right] = A[right], A[new_pivot_idx]

        return new_pivot_idx

    left, right = 0, len(A) - 1

    while True:

        pivot_idx = random.randint(left, right)
        new_pivot_idx = find_new_pivot(left, right, pivot_idx)

        if new_pivot_idx == k-1:
            return A[new_pivot_idx]
        elif new_pivot_idx > k-1:
            right = new_pivot_idx
        else:
            left = new_pivot_idx


def main():

    A = list(range(100))
    random.shuffle(A)

    answer = find_k_largest(A, 5)
    assert answer == 95, f"Wrong answer: {answer}"


if __name__ == "__main__":
    main()