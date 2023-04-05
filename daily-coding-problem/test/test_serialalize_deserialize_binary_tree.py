import pytest

from src.serialalize_deserialize_binary_tree import Node, BinaryTree


@pytest.fixture
def tree() -> BinaryTree:
    binary_tree = BinaryTree()
    binary_tree.root = Node("root")
    binary_tree.root.left = Node("left")
    binary_tree.root.left.left = Node("left.left")
    binary_tree.root.right = Node("right")
    return binary_tree


@pytest.fixture
def serialized_tree():
    return "root left left.left no_child no_child no_child right no_child no_child"


def test_deserializing_binary_tree_returns_expected_tree(tree, serialized_tree):
    deserialized_tree = tree.deserialize(serialized_tree)
    assert deserialized_tree.left.left.val == "left.left"


def test_serialize_tree_returns_expected_string(tree, serialized_tree):
    output_string = tree.serialize()
    assert output_string == serialized_tree
