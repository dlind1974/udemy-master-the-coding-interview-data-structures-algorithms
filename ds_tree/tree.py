import json
from collections import namedtuple

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def __str__(self):
        return f"value: {self.value}; left: {self.left}; right: {self.right}"

NodeWithParent = namedtuple("NodeWithParent", "node parent")


def has_children(node):
    return node.left is not None or node.right is not None


def has_left_child(node):
    return node.left is not None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def _insert_left(self, parent_node, new_node):
        if parent_node.left is None:
            parent_node.left = new_node
        elif new_node.value < parent_node.left.value:
            self._insert_left(parent_node.left, new_node)
        else:
            self._insert_right(parent_node.left, new_node)

    def _insert_right(self, parent_node, new_node):
        if parent_node.right is None:
            parent_node.right = new_node
        elif new_node.value < parent_node.right.value:
            self._insert_left(parent_node.right, new_node)
        else:
            self._insert_right(parent_node.right, new_node)

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        elif value < self.root.value:
            self._insert_left(self.root, new_node)
        else:
            self._insert_right(self.root, new_node)

    def _lookup(self, parent_node, node, value) -> NodeWithParent:
        if node is None:
            return None, None

        if value == node.value:
            return node, parent_node
        elif value < node.value:
            return self._lookup(node, node.left, value)
        else:
            return self._lookup(node, node.right, value)

    def lookup(self, value):
        node, _ = self._lookup(None, self.root, value)
        return node

    def _search_swap_node(self, parent_node, node) -> NodeWithParent:
        if has_left_child(node):
            return self._search_swap_node(node, node.left)
        else:
            return node, parent_node

    def remove(self, value):
        # Find node to remove => remove_node
        # If remove_node has no children => delete the remove_node
        # If remove_node only have left node mark right node as swap_node
        # if remove_node has right child step swap_node pointer right
        #       if swap_node has no left children keep swap_node
        #       if swap_node has left children step left and mark new swap node
        #           repeat swap_node check
        # always keep track of swap_parent => attach final swap_node right children to wap_parent.left
        remove_node, remove_node_parent = self._lookup(None, self.root, value)
        print("**************************************")
        print(f"remove_node: {remove_node})")
        print(f"remove_node_parent: {remove_node_parent}")
        print("**************************************")

        swap_node = None
        if remove_node is None:
            return
        elif not has_children(remove_node):
            if remove_node_parent.left == remove_node:
                remove_node_parent.left = None
            else:
                remove_node_parent.right = None
            return
        elif remove_node.right is None:
            if remove_node_parent.left == remove_node:
                remove_node_parent.left = remove_node.left
            else:
                remove_node_parent.right = remove_node.left
            return
        else:
            swap_node, swap_node_parent = self._search_swap_node(remove_node, remove_node.right)

        if remove_node_parent is None:
            self.root = swap_node
        elif remove_node_parent.left == remove_node:
            remove_node_parent.left = swap_node
        elif remove_node_parent.right == remove_node:
            remove_node_parent.right = swap_node

        if swap_node_parent != remove_node:
            swap_node_parent.left = swap_node.right
        if remove_node.right != swap_node:
            swap_node.right = remove_node.right
        swap_node.left = remove_node.left


def traverse(node):
    if node is None:
        return None
    tree = {'value': node.value}
    tree['left'] = traverse(node.left) if node.left is not None else None
    tree['right'] = traverse(node.right) if node.right is not None else None
    return tree


if __name__ == "__main__":
    print("")
    # Usage example
    tree = BinarySearchTree()
    tree.insert(9)
    tree.insert(4)
    tree.insert(6)
    tree.insert(20)
    tree.insert(170)
    tree.insert(15)
    tree.insert(1)

    print(json.dumps(traverse(tree.root), indent=4))
    print(tree.lookup(20))

    #tree.remove(9)
    tree.remove(20)
    tree.remove(170)

    print(json.dumps(traverse(tree.root), indent=4))
