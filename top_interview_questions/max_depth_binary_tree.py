# https://leetcode.com/problems/maximum-depth-of-binary-tree/description
#
# Given the root of a binary tree, return its maximum depth.
#
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth_recursive(root: TreeNode, current_level) -> int:
    if root is None:
        return current_level

    depth_left = max_depth_recursive(root.left, current_level + 1)
    depth_right = max_depth_recursive(root.right, current_level + 1)
    return max(depth_left, depth_right)


def max_depth(root: Optional[TreeNode]) -> int:
    return max_depth_recursive(root, 0)


def max_depth_clean(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


def create_tree_tc1() -> TreeNode:
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    return root


if __name__ == "__main__":
    tree = create_tree_tc1()
    print(max_depth(tree))
    print(max_depth_clean(tree))
