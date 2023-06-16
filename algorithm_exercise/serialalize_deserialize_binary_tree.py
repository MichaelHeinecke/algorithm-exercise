"""
Given the root to a binary tree, implement serialize(root), which serializes the tree
into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class:

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
"""
from typing import List


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def serialize(self) -> str:
        """
        Serialize tree using preorder traversal depth-first search.

        :return: Serialized tree
        """
        serialized_tree = []
        self._serialize_dfs_helper(self.root, serialized_tree)

        return " ".join(serialized_tree)

    def _serialize_dfs_helper(
        self, node: Node, serialized_tree: List[str]
    ) -> List[str]:
        serialized_tree.append(node.val)
        if node.left is not None:
            self._serialize_dfs_helper(node.left, serialized_tree)
        else:
            serialized_tree.append("no_child")

        if node.right is not None:
            self._serialize_dfs_helper(node.right, serialized_tree)
        else:
            serialized_tree.append("no_child")

        return serialized_tree

    def deserialize(self, serialized_tree: str) -> Node:
        """
        Deserialize binary tree using preorder traversal depth-first search.

        :param serialized_tree: Pre-oder traversal string representation of a
        binary tree.
        :return: Deserialized tree
        """
        node_list = serialized_tree.split(" ")
        node_list.reverse()
        deserialized_tree = self._deserialize_dfs_helper(node_list)
        return deserialized_tree

    def _deserialize_dfs_helper(self, serialized_tree: List[str]) -> [Node, str]:
        if serialized_tree[-1] == "no_child":
            return "no_child"

        node = Node(serialized_tree.pop())
        node.left = self._deserialize_dfs_helper(serialized_tree)
        node.right = self._deserialize_dfs_helper(serialized_tree)
        return node
