from typing import List


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(root: Node) -> str:
    """
    Serialize tree using preorder traversal depth-first search.

    :param root: Root note of a binary tree.
    :return: Serialized tree
    """
    serialized_tree = []
    _serialize_dfs_helper(root, serialized_tree)

    return " ".join(serialized_tree)


def _serialize_dfs_helper(node: Node, serialized_tree: List[str]) -> list[str]:
    serialized_tree.append(node.val)
    if node.left is not None:
        _serialize_dfs_helper(node.left, serialized_tree)
    else:
        serialized_tree.append("no_child")

    if node.right is not None:
        _serialize_dfs_helper(node.right, serialized_tree)
    else:
        serialized_tree.append("no_child")

    return serialized_tree


def deserialize(serialized_tree: str) -> Node:
    """
    Deserialize binary tree using preorder traversal depth-first search.

    :param serialized_tree: Preoder traversal string representation of a
    binary tree.
    :return: Deserialized tree
    """
    node_list = serialized_tree.split(" ")
    node_list.reverse()
    deserialized_tree = _deserialize_dfs_helper(node_list)
    return deserialized_tree


def _deserialize_dfs_helper(serialized_tree: List[str]) -> [Node, None]:
    if serialized_tree[-1] == "no_child":
        return "no_child"

    node = Node(serialized_tree.pop())
    node.left = _deserialize_dfs_helper(serialized_tree)
    node.right = _deserialize_dfs_helper(serialized_tree)

    return node
