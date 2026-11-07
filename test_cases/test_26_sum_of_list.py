
import importlib

module = importlib.import_module("26_sum_of_list")
sum_of_list = module.sum_of_list


def test_positive_numbers():
    assert sum_of_list([1, 2, 3, 4, 5]) == 15


def test_negative_numbers():
    assert sum_of_list([-1, -2, -3]) == -6


def test_mixed_numbers():
    assert sum_of_list([10, -5, 20, -10]) == 15


def test_empty_list():
    assert sum_of_list([]) == 0


def test_single_element():
    assert sum_of_list([25]) == 25


def test_zero_values():
    assert sum_of_list([0, 0, 0]) == 0
