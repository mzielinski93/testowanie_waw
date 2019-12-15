from math import pi

# def circle_area(r):
#     if type(r) not in [int, float]:
#         return "Podales nieprawidlowy typ. Podaj liczbe"
#     elif r < 0:
#         return "Koło nie istnieje."
#     else:
#         return r ** 2 * pi


def circle_area(r):
    try:
        if r < 0:
            raise Exception("Promien nie moze byc ujemny")
        return pi * r **2
    except:
        return "Cos poszlo nie tak"



print(circle_area(1))
print(circle_area(0))
print(circle_area(-1))
print(circle_area(2+5j))
print(circle_area(True))
print(circle_area("asd"))
