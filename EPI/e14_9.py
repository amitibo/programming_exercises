"""Test if three BST are totally ordered.
"""

import collections

graph = collections.namedtuple("graph", ("data", "left", "right"))


def test_order(possible_anc_desc_0, possible_anc_desc_1, middle):

    search0, search1 = possible_anc_desc_0, possible_anc_desc_1

    while (search0 is not possible_anc_desc_1) and (search0 is not middle) and \
          (search1 is not possible_anc_desc_0) and (search1 is not middle) and \
          (search0 or search1):

        if search0:
            search0 = search0.left if search0.data > middle.data \
                else search0.right

        if search1:
            search1 = search1.left if search1.data > middle.data \
                else search1.right

    if (search0 is not middle) and (search1 is not middle):
        return False


    def find_target(src, target):
        while src and src is not target:
            src = src.left if src.data > target.data else src.right

        return src is target

    return find_target(
        middle, possible_anc_desc_1 if search0 is middle else possible_anc_desc_0
    )

