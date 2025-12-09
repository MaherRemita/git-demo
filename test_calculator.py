# test_calculator.py
import pytest
from calculator import add, subtract, division, multiply, power


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(2, 5) == -3

def test_division():
    assert division(10, 2) == 5.0
    assert division(7, 2) == 3.5
    assert division(-10, 5) == -2.0
    assert division(0, 5) == 0.0
    
def test_multiply():
    assert multiply(5, 3) == 15
    assert multiply(2, 5) == 10

def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(9, 0.5) == 3
    assert power(-2, 3) == -8
