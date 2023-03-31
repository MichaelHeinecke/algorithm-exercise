from src.product_of_array_items import multiply_array_items_without_self, \
    multiply_array_items_without_self_no_division


def test_array_items_are_multiplied_correctly_1():
    input_array = [1, 2, 3, 4, 5]
    expected_output_array = [120, 60, 40, 30, 24]
    assert multiply_array_items_without_self(
        input_array) == expected_output_array


def test_array_items_are_multiplied_correctly_2():
    input_array = [3, 2, 1]
    expected_output_array = [2, 3, 6]
    assert multiply_array_items_without_self(
        input_array) == expected_output_array


def test_array_items_are_multiplied_correctly_no_division_1():
    input_array = [1, 2, 3, 4, 5]
    expected_output_array = [120, 60, 40, 30, 24]
    assert multiply_array_items_without_self_no_division(
        input_array) == expected_output_array


def test_array_items_are_multiplied_correctly_no_division_2():
    input_array = [3, 2, 1]
    expected_output_array = [2, 3, 6]
    assert multiply_array_items_without_self_no_division(
        input_array) == expected_output_array
