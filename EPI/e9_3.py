"""Compute the LCA in a binary tree.
"""

from collections import namedtuple

TreeElement = namedtuple("TreeElement", ("data", "left", "right"))


def compute_LCA(root=TreeElement, a=TreeElement, b=TreeElement):

    def find_path(current, target, path=[]):
        if current is None:
            return False

        path.append(current)
        if current is target:
            return True

        if find_path(current.left, target, path) or \
           find_path(current.right, target, path):
            return True

        path.pop(-1)
        return False


    patha, pathb = [], []
    find_path(root, a, patha)
    find_path(root, a, pathb)

    lca = root
    for i, j in zip(patha[1:], pathb[1:]):
        if i is not j:
            return lca
        lca = i


Status = namedtuple("Status", ("count", "LCA"))

def compute_LCA_alternative(root=TreeElement, a=TreeElement, b=TreeElement):

    def check_LCA(node):

        if node is None:
            return Status(0, None)

        cnt = 0
        if node in (a, b):
            cnt += 1

        status_a =  check_LCA(node.left)
        cnt += status_a.count

        if cnt == 2:
            if status_a.LCA is not None:
                return status_a
            return Status(2, node)

        status_b =  check_LCA(node.right)
        cnt += status_b.count

        if cnt == 2:
            if status_b.LCA is not None:
                return status_b
            return Status(2, node)

        return Status(cnt, None)

    return check_LCA(root)


def main():
    pass


if __name__ == "__main__":
    main()