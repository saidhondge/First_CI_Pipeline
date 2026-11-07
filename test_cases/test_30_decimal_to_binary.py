import importlib
import pytest

module = importlib.import_module("30_decimal_to_binary")
decimal_to_binary = module.decimal_to_binary


def test_zero():
    assert decimal_to_binary(0) == "0"


def test_one():
    assert decimal_to_binary(1) == "1"


def test_small_number():
    assert decimal_to_binary(5) == "101"


def test_eight():
    assert decimal_to_binary(8) == "1000"


def test_larger_number():
    assert decimal_to_binary(25) == "11001"


def test_negative_number():
    with pytest.raises(ValueError):
        decimal_to_binary(-5)


def test_original_integer_unchanged():
    number = 10
    assert decimal_to_binary(number) == "1010"
    assert number == 10