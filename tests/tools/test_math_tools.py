import math
from demo_server.tools.math_tools import (
    add_fn, subtract_fn, multiply_fn, divide_fn, fibonacci_fn
)

def test_add():
    assert add_fn(2, 3) == 5
    assert add_fn(-1.5, 1.5) == 0

def test_subtract():
    assert subtract_fn(10, 7) == 3
    assert subtract_fn(0, 3) == -3

def test_multiply():
    assert multiply_fn(4, 5) == 20
    assert multiply_fn(-2, 3) == -6

def test_divide():
    assert divide_fn(8, 2) == 4
    assert divide_fn(7, 0) is None
    assert math.isclose(divide_fn(7, 3), 7/3)

def test_fibonacci_bounds():
    assert fibonacci_fn(-5) == []          
    assert len(fibonacci_fn(500)) == 50   

def test_fibonacci_values():
    assert fibonacci_fn(1) == [0]
    assert fibonacci_fn(5) == [0, 1, 1, 2, 3]
