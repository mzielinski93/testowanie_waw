from math import pi

def add(x, y):
    return x+y


def product(x, y):
    return x * y


def is_palindrom(string):
    return string.lower().replace(" ", "") == string[::-1].lower().replace(" ", "")


def circle_area(r):
        if r < 0:
            raise ValueError("The radius cannot be negative")
        if type(r) not in [int, float]:
            raise TypeError("The radius be a non-negative real number.")

        return pi * r**2
