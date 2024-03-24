# https://leetcode.com/problems/validate-binary-search-tree/

# Idea 1: DFS, Do a Depth First Traversal in-order to see that new value is always higher that the
# previous value

# Idea 2: BFS,


from typing import Optional, List


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def traverse_in_order(node : TreeNode, traversal_output) -> bool:
    if node.left is not None:
        ok = traverse_in_order(node.left, traversal_output)
        if not ok:
            return False

    if len(traversal_output) > 0 and node.val < traversal_output[-1]:
        return False
    traversal_output.append(node.val)

    if node.right is not None:
        ok = traverse_in_order(node.right, traversal_output)
        if not ok:
            return False

    return True


def is_valid_bst(root: Optional[TreeNode]) -> bool:
    traversal = []
    return traverse_in_order(root, traversal)


def build_test_tree_1():
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    return root


def build_test_tree_2():
    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(6)
    return root


def build_test_tree_3():
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(6)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(7)
    return root


if __name__ == "__main__":
    test_tree_1 = build_test_tree_1()
    print(is_valid_bst(test_tree_1))

    test_tree_2 = build_test_tree_2()
    print(is_valid_bst(test_tree_2))

    # input = [5, 4, 6, None, None, 3, 7]
    test_tree_3 = build_test_tree_3()
    print(is_valid_bst(test_tree_3))

