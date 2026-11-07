
import importlib
import pytest

module = importlib.import_module("25_max_min_list")
find_max_min = module.find_max_min


def test_positive_numbers():
    assert find_max_min([10, 20, 5, 40, 15]) == (40, 5)


def test_negative_numbers():
    assert find_max_min([-10, -20, -5, -40]) == (-5, -40)


def test_single_element():
    assert find_max_min([25]) == (25, 25)


def test_duplicate_numbers():
    assert find_max_min([5, 5, 5, 5]) == (5, 5)


def test_mixed_numbers():
    assert find_max_min([-10, 0, 15, -5, 20]) == (20, -10)


def test_empty_list():
    with pytest.raises(ValueError):
        find_max_min([])
