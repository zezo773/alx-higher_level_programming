#!/usr/bin/python3

import unittest
from models.rectangle import Rectangle
from models.base import Base

class TestRectangle(unittest.TestCase):
    def setUp(self):
        Base._Base__nb_objects = 0
    def test_id(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
    def test_raise_type(self):
        with self.assertRaises(TypeError):
            Rectangle(10, "2")
    def test_raise_value(self):
        r = Rectangle(10, 2)
        with self.assertRaises(ValueError):
            r.width = -10
    def test_area(self):
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)
    def test_str(self):
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")
    def test_update(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 10/10")
