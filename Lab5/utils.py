"""Simple calculator functions for CI/CD lab"""


def add(a: int, b: int) -> int:
    """Returns the sum of a and b."""
    return a + b


def subtract(a: int, b: int) -> int:
    """Returns the difference between a and b."""
    return a - b


def multiply(a: int, b: int) -> int:
    """Returns the product of a and b."""
    return a * b


def divide(a: int, b: int) -> float:
    """Returns the result of dividing a by b."""
    return a / b


def to_binary(num: int) -> str:
    """Converts an integer 0–100 to binary string. Raises ValueError if out of range."""
    if not isinstance(num, int):
        raise TypeError("Input must be an integer.")
    if not (0 <= num <= 100):
        raise ValueError("Number must be between 0 and 100.")
    return bin(num)[2:]
