"""Test tree balanced."""

from collections import namedtuple

TreeElement = namedtuple("TreeElement", ("data", "left", "right"))
Status = namedtuple("Status", ("height", "balanced"))


def is_balanced_tree(root: TreeElement):

    def check_balanced(node: TreeElement):

        if node is None:
            return Status(0, True)

        left_status = check_balanced(node.left)
        if not left_status.balanced:
            return Status(-1, False)

        right_status = check_balanced(node.right)
        if not right_status.balanced:
            return Status(-1, False)

        if abs(left_status.height - right_status.height) > 1:
            return Status(-1, False)

        return Status(
            max(left_status.height, right_status.height),
            True
        )

    return check_balanced(root).balanced


def main():
    pass


if __name__ == "__main__":
    main()