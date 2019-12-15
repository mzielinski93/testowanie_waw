def div(a, b):
    return a/b

# if div(10, 5) == 2:
#     print("PASSED")
# else:
#     raise Exception("FAILED")
#
# if div(10, 2) == 5:
#     print("PASSED")
# else:
#     raise Exception("FAILED")

# assert div(10, 5) == 2, "FAILED"
# assert div(10, 2) == 5, "FAILED"

#KOLJENA FUNKCJA
# def quad(a, b):
#     return (a + b) ** 2
#
#
# assert quad(2, 4) == 36, "FAILED"
# assert quad(1, 5) == 36, "FAILED"
# assert quad(8, 2) == 100, "FAILED"
# assert quad(0, 0) == 0, "FAILED"

#FUNKCJA ASSERT NIE DO TESTOWANIA ALE DO CZEGOS INNEGO
# def div(a, b):
#     try:
#         return a/b
#     except ZeroDivisionError:
#         print("Nie mozna dzielic przez zero")
#
# div(5, 0)

#LUB LUB LUB LUB LUB LUB LUB LUB LUB LUB
# def div(a, b):
#     assert b != 0, "Nie mozna dzielic przez zero"
#     return a/b
#
# div(5, 0)

#KOLEJNE ZADANIE
def con_str(str1, str2):
    return str1 + str2


assert con_str("Mama", "Tata") == "MamaTata", "FAILED"
assert con_str("Pies ", "Azor") == "Pies Azor", "FAILED"
assert con_str("", "") == "", "FAILED"