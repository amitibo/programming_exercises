"""Compute the LCA optimize for close ancestors.
"""

from collections import namedtuple

TreeNode = namedtuple("TreeNode", ("data", "left", "right", "parent"))


def compute_LCA(node_a, node_b):

    visited={}
    search0, search1 = node_a, node_b

    while True:

        if search0 in visited:
            return search0

        if search1 in visited:
            return search1

        visited[search0] = 1
        visited[search1] = 1

        if search0 is not None:
            search0 = search0.parent

        if search1 is not None:
            search1 = search1.parent


def compute_LCA_alternative(node_a, node_b):

    visited = set()

    search0, search1 = node_a, node_b

    while search0 or search1:

        if search0:
            if search0 in visited:
                return search0

            visited.add(search0)
            search0 = search0.parent

        if search1:
            if search1 in visited:
                return search1

            visited.add(search1)
            search1 = search1.parent

    raise ValueError("nodes not on same tree.")