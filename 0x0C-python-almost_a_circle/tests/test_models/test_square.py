#!/usr/bin/python3
'''Defines the unittests for models/square.py
Test classes in order of appearance:
    class Test_Square_instantiation(unittest.TestCase):
'''
import unittest
from models.square import Square
from models.base import Base

class Test_Square_instantiation(unittest.TestCase):
    def test_base(self):
        self.assertIsInstance(Square(5), Base)

    def test_rectangle(self):
        self.assertIsInstance(Square(3), Square)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Square()

    def test_one_arg(self):
        s1 = Square(1)
        s2 = Square(9)
        self.assertEqual(s1.id, s2.id - 1)

    def test_two_args(self):
        s1 = Square(1, 2)
        s2 = Square(2, 1)
        self.assertEqual(s1.id, s2.id - 1)

    def test_three_args(self):
        s1 = Square(1, 2, 3)
        s2 = Square(3, 2, 1)
        self.assertEqual(s1.id, s2.id - 1)

    def test_four_args(self):
        self.assertEqual(4, Square(1, 2, 3, 4).id)

    def test_more_than_four_args(self):
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)


if __name__ == "__main__":
    unittest.main()
