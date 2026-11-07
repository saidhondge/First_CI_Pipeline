import importlib

module = importlib.import_module("22_anagram_strings")
is_anagram = module.is_anagram


def test_basic_anagram():
    assert is_anagram("listen", "silent") is True


def test_not_anagram():
    assert is_anagram("hello", "world") is False


def test_uppercase_and_lowercase():
    assert is_anagram("Listen", "Silent") is True


def test_spaces_are_ignored():
    assert is_anagram("dormitory", "dirty room") is True


def test_empty_strings():
    assert is_anagram("", "") is True