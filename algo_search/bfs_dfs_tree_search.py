import json
from ds_tree.tree import BinarySearchTree
from ds_tree.tree import traverse


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

    # print(json.dumps(traverse(tree.root), indent=4))
    #               9
    #       4               20
    #   1       6       15      170

    print(f"BFS: {tree.bfs()}")
    print(f"DFS in order: {tree.dfs_in_order()}")
    print(f"DFS pre order: {tree.dfs_pre_order()}")
    print(f"DFS post order: {tree.dfs_post_order()}")

