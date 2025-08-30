#!/usr/bin/python3

import unittest
from models.rectangle import Rectangle
from models.base import Base
from models.square import Square

class TestRectangle(unittest.TestCase):
    def setUp(self):
        Base._Base__nb_objects = 0
    def test_square(self):
        s1 = Square(5)
        self.assertEqual(s1.area(), 25)
    def test_size(self):
        s1 = Square(5)
        self.assertEqual(str(s1.size), '5')
