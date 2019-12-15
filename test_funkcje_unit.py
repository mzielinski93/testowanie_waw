import math
import unittest

import funkcje

class TestCircleArea(unittest.TestCase):

    def test_area(self):
        """test area when radius >=0"""
        self.assertAlmostEqual(funkcje.circle_area(1), math.pi) #zgodnosc do 7 miejsc po przecinku
        self.assertEqual(funkcje.circle_area(0), 0)
        self.assertAlmostEqual(funkcje.circle_area(2.1), math.pi * (2.1**2))


    def test_values(self):
        self.assertRaises(ValueError, funkcje.circle_area, -2)


    def test_types(self):
        #make sure type error is raises then neccesary
        self.assertRaises(TypeError, funkcje.circle_area, 3+5j)
        self.assertRaises(TypeError, funkcje.circle_area, True)
        self.assertRaises(TypeError, funkcje.circle_area, "asd")