from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0

    leftDepth = maxDepth(root.left)
    rightDepth = maxDepth(root.right)

    return max(leftDepth, rightDepth) + 1


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    root.right.right.right = TreeNode(8)
    root.right.left.right = TreeNode(7)

    print("The max depth is:", maxDepth(root))
