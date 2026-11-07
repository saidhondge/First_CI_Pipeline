
import importlib

module = importlib.import_module("27_rotate_list")
rotate_list = module.rotate_list


def test_rotate_right():
    assert rotate_list([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]


def test_rotate_left():
    assert rotate_list([1, 2, 3, 4, 5], -2) == [3, 4, 5, 1, 2]


def test_rotation_greater_than_length():
    assert rotate_list([1, 2, 3], 5) == [2, 3, 1]


def test_empty_list():
    assert rotate_list([], 3) == []


def test_zero_rotation():
    assert rotate_list([1, 2, 3], 0) == [1, 2, 3]


def test_single_element():
    assert rotate_list([10], 5) == [10]


def test_original_list_is_not_modified():
    items = [1, 2, 3, 4]
    rotate_list(items, 2)
    assert items == [1, 2, 3, 4]
