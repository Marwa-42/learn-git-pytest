# Exercise 1: Basic Calculator Functions
from typing import Union

Number = Union[int, float]

def add(a: Number, b: Number) -> Number:
    """ Retourne la somme de a et b. """
    return a + b

def subtract(a: Number, b: Number) -> Number:
    """ Retourne la soustraction de b à a. """
    return a - b

def multiply(a: Number, b: Number) -> Number:
    """ Retourne le produit de a et b. """
    return a * b

def divide(a: Number, b: Number) -> Number:
    """ Retourne le résultat de a divisé par b. 
        Lève une erreur si b est 0. """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
