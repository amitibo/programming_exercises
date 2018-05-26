"""Find the closest entries in three sorted arrays.
"""

from sortedcontainers import SortedDict, SortedList, SortedListWithKey
from collections import namedtuple

element = namedtuple("element", ("val", "idx"))


def find_closest_elements_in_sorted_arrays(sorted_arrays):

    candidate_list = SortedListWithKey(key=lambda el: el.val)

    sorted_arrays = [iter(sorted_array) for sorted_array in sorted_arrays]

    for i, sorted_array in enumerate(sorted_arrays):
        candidate_list.add(element(next(sorted_array), i))

    intervals_dict = SortedDict()

    while True:
        min_val, idx = candidate_list[0]
        max_val, _ = candidate_list[-1]

        intervals_dict[max_val-min_val] = [e.val for e in candidate_list]

        candidate_list.pop(0)
        try:
            candidate_list.add(element(next(sorted_arrays[idx]), idx))
        except:
            return intervals_dict.values()[0]


def main():
    l0 = (5, 10, 15)
    l1 = (3, 6, 9, 12, 15)
    l2 = (8, 16, 24)

    print(
        find_closest_elements_in_sorted_arrays(
            (l0, l1, l2)
        )
    )


if __name__ == "__main__":
    main()

