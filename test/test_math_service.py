import pytest  # type: ignore
from services.math_service import compute_pow, compute_fib, compute_factorial


def test_compute_pow():
    assert compute_pow(2, 3) == '8'
    assert compute_pow(5, 0) == '1'
    assert compute_pow(10, 5) == '100000'


def test_compute_fib():
    assert compute_fib(0) == '0'
    assert compute_fib(1) == '1'
    assert compute_fib(2) == '1'
    assert compute_fib(10) == '55'


def test_compute_factorial():
    assert compute_factorial(0) == '1'
    assert compute_factorial(1) == '1'
    assert compute_factorial(5) == '120'
    assert compute_factorial(10) == '3628800'

# Edge cases
def test_fib_negative():
    with pytest.raises(TypeError):
        compute_fib(-1)

def test_factorial_negative():
    with pytest.raises(TypeError):
        compute_factorial(-5)
