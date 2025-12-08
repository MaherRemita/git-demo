# test_calculator.py
import pytest
from calculator import add, subtract,multiply

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(2, 5) == -3
    
def test_multiply():
    assert multiply(5, 3) == 15
    assert multiply(2, 5) == 10   
    