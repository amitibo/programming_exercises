class TreeNode():

    def __init__(self, name=None, data=None, left=None, right=None):
        self.name = name
        self.data = data
        self.left = left
        self.right = right


def make_tree():

    E = TreeNode(name="E", data=0)
    D = TreeNode(name="D", data=28)
    C = TreeNode(name="C", data=271, left=D, right=E)
    H = TreeNode(name="H", data=17)
    G = TreeNode(name="G", data=3, left=H)
    F = TreeNode(name="F", data=516, right=G)
    B = TreeNode(name="B", data=6, left=C, right=F)
    M = TreeNode(name="M", data=641)
    L = TreeNode(name="L", data=401, right=M)
    N = TreeNode(name="N", data=257)
    K = TreeNode(name="K", data=1, left=L, right=N)
    J = TreeNode(name="J", data=2, right=K)
    P = TreeNode(name="P", data=28)
    O = TreeNode(name="O", data=271, right=P)
    I = TreeNode(name="I", data=6, left=J, right=O)
    A = TreeNode(name="A", data=314, left=B, right=I)

    return A
