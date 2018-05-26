"""
"""

from collections import namedtuple
import heapq


def find_k_largest_elements_heap(heap, k):


    indices_heap = [(-heap[0], 0)]
    k_largest = []
    for i in range(k):
        val, ind = heapq.heappop(indices_heap)
        k_largest.append(-val)

        if len(heap) > (2*ind + 1):
            heapq.heappush(indices_heap, (-heap[2*ind + 1], (2*ind + 1)))

        if len(heap) > (2*ind + 2):
            heapq.heappush(indices_heap, (-heap[2*ind + 2], (2*ind + 2)))

    return k_largest



def main():

    tests = (
        (
            (
                (561, 314, 401, 28, 156, 359, 271, 11, 3),
                4
            ),
            (561, 314, 401, 359)
        ),
    )

    for test, ans in tests:
        heap, k = test
        bns = find_k_largest_elements_heap(heap, k)

        assert sorted(ans) == sorted(bns), f"Not expected answer {ans}. Got {bns}"


if __name__ == "__main__":
    main()
