from functools import lru_cache


def compute_pow(base: int, exponent: int) -> str:
    """
    Compute base raised to the power of exponent.
    """
    return str(base ** exponent)


@lru_cache(maxsize=128)
def compute_fib(n: int) -> str:
    """
    Compute the nth Fibonacci number 
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n < 2:
        return str(n)
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return str(b)


def compute_factorial(n: int) -> str:
    """
    Compute the factorial of n iteratively to avoid recursion limits.
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return str(result)
