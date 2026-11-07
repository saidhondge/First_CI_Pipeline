
import importlib

module = importlib.import_module("23_sort_without_sort")
bubble_sort = module.bubble_sort


def test_unsorted_list():
    assert bubble_sort([5, 2, 8, 1, 3]) == [1, 2, 3, 5, 8]


def test_already_sorted_list():
    assert bubble_sort([1, 2, 3, 4]) == [1, 2, 3, 4]


def test_reverse_sorted_list():
    assert bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]


def test_empty_list():
    assert bubble_sort([]) == []


def test_negative_numbers():
    assert bubble_sort([-3, 5, -1, 0, 2]) == [-3, -1, 0, 2, 5]


def test_original_list_is_not_modified():
    numbers = [4, 2, 3, 1]
    bubble_sort(numbers)
    assert numbers == [4, 2, 3, 1]
