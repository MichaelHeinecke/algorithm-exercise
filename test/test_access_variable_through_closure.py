import pytest

from algorithm_exercise.access_variable_through_closure import cons, car, cdr


@pytest.fixture
def pair():
    return cons(3, 4)


def test_given_pair_returns_first_pair_element(pair):
    expected_result = 3
    result = car(pair)
    assert result == expected_result


def test_given_cons_car_returns_second_pair_element(pair):
    expected_result = 4
    result = cdr(pair)
    assert result == expected_result
