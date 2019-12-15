import funkcje

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


# test_add()
# test_product()
# test_is_palindrom()
