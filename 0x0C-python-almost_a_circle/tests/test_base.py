#!/usr/bin/python3

import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_auto_id_increment(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
    def test_custom_id(self):
        b3 = Base(12)
        self.assertEqual(b3.id, 12)
