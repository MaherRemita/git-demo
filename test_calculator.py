# test_calculator.py
import pytest
from calculator import add, subtract, division, multiply, power


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(5, 0) == 5
    assert add(-2, -3) == -5
    assert add(2.5, 3.5) == 6.0
    assert add(1e6, 1e6) == 2e6

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(2, 5) == -3
    assert subtract(0, 0) == 0
    assert subtract(5, 0) == 5
    assert subtract(5, -3) == 8
    assert subtract(-5, -3) == -2
    assert subtract(5.5, 2.5) == 3.0
    assert subtract(1e6, 5e5) == 5e5

def test_division():
    assert division(10, 2) == 5.0
    assert division(7, 2) == 3.5
    assert division(-10, 5) == -2.0
    assert division(0, 5) == 0.0
    assert division(10, -2) == -5.0
    assert division(-10, -2) == 5.0
    assert division(0.0, 1.0) == 0.0
    assert division(1e6, 2) == 5e5
    with pytest.raises(ZeroDivisionError):
        division(10, 0)
    with pytest.raises(ZeroDivisionError):
        division(0, 0)

def test_multiply():
    assert multiply(5, 3) == 15
    assert multiply(2, 5) == 10
    assert multiply(0, 5) == 0
    assert multiply(5, 0) == 0
    assert multiply(-5, 3) == -15
    assert multiply(-5, -3) == 15
    assert multiply(2.5, 4) == 10.0
    assert multiply(1e3, 1e3) == 1e6

def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(9, 0.5) == 3
    assert power(-2, 3) == -8
    assert power(-2, 2) == 4
    assert power(2, -1) == 0.5
    assert power(0, 5) == 0
    assert power(0, 0) == 1  # As per Python's pow(0, 0)
    assert power(4, 0.5) == 2.0
    assert power(27, 1/3) == 3.0
    assert power(1, 100) == 1
    