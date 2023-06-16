from algorithm_exercise.sum_of_array_items_equals_number import \
    sum_of_array_items_equals_number


def test_sum_of_array_items_equals_number_returns_true():
    array = [10, 15, 3, 7]
    number = 17
    assert sum_of_array_items_equals_number(array, number) is True


def test_sum_of_array_items_does_not_equal_number_returns_false():
    array = [9, 15, 3, 7]
    number = 17
    assert sum_of_array_items_equals_number(array, number) is False


def test_array_contains_number_divided_by_2_returns_false():
    array = [10, 1, 3, 4]
    number = 20
    assert sum_of_array_items_equals_number(array, number) is False


def test_negative_number_and_items_returns_true():
    array = [-10, -5, 3, 4]
    number = -15
    assert sum_of_array_items_equals_number(array, number) is True
