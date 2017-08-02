#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

:mod:`lab_unittest` --- Module unittest
========================================

a. Create a series of unittest tests to verify the classes below.  Create the following tests:
  1. verify exceptions are generated as expected (for invalid shapes)
  2. verify that calculations are done correctly for the shape type
  3. verify names are set as expected
  4. test all the things!

"""

import math
import unittest

class InvalidShape(Exception):
    pass


class shape(object):
    def __init__(self):
        self.name = "generic shape"

    def area(self):
        raise InvalidShape

    def perimeter(self):
        raise InvalidShape


class circle(shape):
    def __init__(self):
        self.name = "circle"
        self.center = (0.0, 0.0)
        self.radius = 1.0

    def area(self):
        return math.pi * self.radius**2

    def circumference(self):
        return math.pi * self.radius * 2.0

    def perimeter(self):
        return self.circumference()


class square(shape):
    def __init__(self):
        self.name = "square"
        self.position = (0.0, 0.0)
        self.side = 1.0

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return self.side * 4


class TestInvalidShape(unittest.TestCase):
    def test_exception(self):
        self.assertRaises(Exception, InvalidShape())


class TestShape(unittest.TestCase):
    def test_init(self):
        self.assertEqual(shape().name, 'generic shape')

    def test_area(self):
        self.assertRaises(Exception, shape().area)

    def test_perimeter(self):
        self.assertRaises(Exception, shape().area)


class TestCircle(unittest.TestCase):
    def test_init(self):
        self.assertEqual(circle().name, 'circle')

    def test_area(self):
        self.assertEqual(circle().area(), math.pi)

    def test_circumference(self):
        self.assertEqual(circle().circumference(), math.pi * 2)

    def test_perimeter(self):
        self.test_circumference()


class TestSquare(unittest.TestCase):
    def test_init(self):
        self.assertEqual(square().name, 'square')

    def test_area(self):
        self.assertEqual(square().area(), 1)

    def test_perimeter(self):
        self.assertEqual(square().perimeter(), 4)


if __name__ == '__main__':
    unittest.main()
