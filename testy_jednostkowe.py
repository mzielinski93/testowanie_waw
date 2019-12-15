#KOLEJNE ZADANIE
# def add(x, y):
#     return x+y
#
# def test_add():
#     assert add(3, 5) == 8
#     assert add(7, -1) == 6
#     assert round(add(4.3, 5.6), 2) == 9.9
#
#
# test_add()
#
#KOLEJNE ZADANIE Z TESTEM JEDNOSTKOWYM
def product(x, y):
    return x * y

def test_product():
    assert product(3, 5) == 15
    assert product(1, 0) == 0
    assert product(-8, 2.5) == -20


test_product()