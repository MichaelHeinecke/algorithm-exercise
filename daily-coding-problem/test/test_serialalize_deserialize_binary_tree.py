import pytest

from src.serialalize_deserialize_binary_tree import Node, deserialize, \
    serialize


@pytest.fixture
def tree():
    return Node("root", Node("left", Node("left.left")), Node("right"))


@pytest.fixture
def serialized_tree():
    return "root left left.left no_child no_child no_child right " \
           "no_child no_child"


def test_deserializing_binary_tree_returns_expected_tree(serialized_tree):
    deserialized_tree = deserialize(serialized_tree)
    assert deserialized_tree.left.left.val == "left.left"


def test_serialize_tree_returns_expected_string(tree, serialized_tree):
    output_string = serialize(tree)
    assert output_string == serialized_tree
