from functools import lru_cache


def compute_pow(base: int, exponent: int) -> int:
    """
    Compute base raised to the power of exponent.
    """
    return base ** exponent


@lru_cache(maxsize=128)
def compute_fib(n: int) -> int:
    """
    Compute the nth Fibonacci number using recursion with memoization.
    """
    if n < 2:
        return n
    return compute_fib(n - 1) + compute_fib(n - 2)


def compute_factorial(n: int) -> int:
    """
    Compute the factorial of n iteratively to avoid recursion limits.
    """
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
