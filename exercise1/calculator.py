# Exercise 1: Basic Calculator Functions
from typing import Union

# Defining a Number type for cleaner type hints
Number = Union[int, float]

def add(a: Number, b: Number) -> Number:
    """
    Return the sum of a and b.
    """
    return a + b

def subtract(a: Number, b: Number) -> Number:
    """
    Return the result of subtracting b from a.
    """
    return a - b

def multiply(a: Number, b: Number) -> Number:
    """
    Return the product of a and b.
    """
    return a * b

def divide(a: Number, b: Number) -> Number:
    """
    Return the result of dividing a by b.
    Raises ValueError if b is 0.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# Example usage
if __name__ == "__main__":
    print("Addition: ", add(10, 5))  # 15
    print("Subtraction: ", subtract(10, 5))  # 5
    print("Multiplication: ", multiply(10, 5))  # 50
    print("Division: ", divide(10, 5))  # 2.0

