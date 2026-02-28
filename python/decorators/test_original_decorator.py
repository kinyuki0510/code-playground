import pytest
from original_decorator import eat_decorator, eat_food


def test_decorator_prints_before_and_after(capsys):
    eat_food()
    captured = capsys.readouterr()
    lines = captured.out.strip().splitlines()
    assert lines[0] == "いただきます"
    assert lines[-1] == "ごちそうさまでした"


def test_decorator_calls_original_function(capsys):
    eat_food()
    captured = capsys.readouterr()
    assert "もぐもぐ..." in captured.out


def test_decorator_preserves_return_value():
    @eat_decorator
    def add(a, b):
        return a + b

    assert add(1, 2) == 3


def test_decorator_preserves_function_metadata():
    @eat_decorator
    def my_func():
        """my docstring"""

    assert my_func.__name__ == "my_func"
    assert my_func.__doc__ == "my docstring"
