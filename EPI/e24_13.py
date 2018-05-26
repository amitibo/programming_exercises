"""Postorder traversal without recursion
"""

from tree_utils import make_tree




def postorder_with_recursion(root):

    def postorder_helper(curr):

        if curr is None:
            return

        postorder_helper(curr.left)
        postorder_helper(curr.right)
        nodes.append(curr.name)

    nodes = []
    postorder_helper(root)
    return nodes


def postorder_without_recursion(root):

    def postorder_helper(curr):

        if curr is None:
            return

        postorder_helper(curr.left)
        postorder_helper(curr.right)
        nodes.append(curr.name)

    nodes = []
    postorder_helper(root)
    return nodes


def main():
    tree = make_tree()

    tests = (
        (
            tree,
            postorder_with_recursion(tree)
        ),
    )

    for test, ans in tests:
        bns = postorder_without_recursion(test)
        assert ans == bns, f"Not the expected answer {ans}. Got {bns}"


if __name__ == "__main__":
    main()


