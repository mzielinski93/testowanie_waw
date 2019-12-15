import funkcje
import pytest

def test_add():
    assert funkcje.add(3, 5) == 8
    assert funkcje.add(7, -1) == 6
    assert funkcje.add(4.3, 5.3) == 9.6


def test_product():
    assert funkcje.product(3, 5) == 15
    assert funkcje.product(1, 0) == 0
    assert funkcje.product(-8, 2.5) == -20


def test_is_palindrom():
    assert funkcje.is_palindrom("kajak")
    assert funkcje.is_palindrom("")
    assert funkcje.is_palindrom("Kobyla ma maly bok")


def test_circle_area():
    assert funkcje.circle_area(5) == 25 * funkcje.pi
    assert funkcje.circle_area(1.5) == 2.25 * funkcje.pi
    assert funkcje.circle_area(0.2) == 0.04 * funkcje.pi


def test_values():
    with pytest.raises(ValueError):
        funkcje.circle_area(-2)


def test_type():
    with pytest.raises(TypeError):
        funkcje.circle_area("asd")

