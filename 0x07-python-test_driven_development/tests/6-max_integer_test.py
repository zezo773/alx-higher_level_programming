#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max(self):
        self.assertEqual(max_integer([5, -2, 100, 3]), 100)
