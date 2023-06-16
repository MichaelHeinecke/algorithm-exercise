from algorithm_exercise.find_first_missing_integer_in_array \
    import find_first_missing_integer_in_array


def test_given_array_with_negative_number_first_missing_integer_is_found():
    array = [3, 4, -1, 1]
    expected_result = 2
    result = find_first_missing_integer_in_array(array)
    assert result == expected_result


def test_given_array_no_gap_in_range_starting_from_zero_first_missing_integer_is_found():
    array = [1, 2, 0]
    expected_result = 3
    result = find_first_missing_integer_in_array(array)
    assert result == expected_result


def test_given_array_no_gap_in_range_starting_from_one_first_missing_integer_is_found():
    array = [4, 3, 2, 1]
    expected_result = 5
    result = find_first_missing_integer_in_array(array)
    assert result == expected_result


def test_given_array_with_duplicates_first_missing_integer_is_found():
    array = [3, 3, 3]
    expected_result = 1
    result = find_first_missing_integer_in_array(array)
    assert result == expected_result


def test_given_array_with_negative_numbers_only_first_missing_integer_is_found():
    array = [-2, -7, -1]
    expected_result = 1
    result = find_first_missing_integer_in_array(array)
    assert result == expected_result


def test_given_array_with_zero_only_first_missing_integer_is_found():
    array = [0]
    expected_result = 1
    result = find_first_missing_integer_in_array(array)
    assert result == expected_result


def test_given_array_with_one_only_first_missing_integer_is_found():
    array = [1]
    expected_result = 2
    result = find_first_missing_integer_in_array(array)
    assert result == expected_result
