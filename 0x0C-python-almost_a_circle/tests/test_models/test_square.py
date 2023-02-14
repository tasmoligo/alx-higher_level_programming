#!/usr/bin/python3
'''Defines the unittests for models/square.py
Test classes in order of appearance:
    class Test_Square_instantiation
    class Test_Square_dictionary
'''
import unittest
from models.square import Square
from models.base import Base


class Test_Square_instantiation(unittest.TestCase):
    '''Unittests for square instantiation'''

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


class Test_Square_dictionary(unittest.TestCase):
    '''Unittests for to_dictionary method'''

    def test_to_dictionary_output(self):
        s = Square(3, 4, 1, 2)
        correct = {'id': 2, 'x': 4, 'size': 3, 'y': 1}
        self.assertDictEqual(correct, s.to_dictionary())

    def test_dictionary_with_no_object_change(self):
        s1 = Square(4, 2, 1, 3)
        s2 = Square(1, 2, 4)
        s2.update(**s1.to_dictionary())
        self.assertNotEqual(s1, s2)

    def test_to_dictionary_arg(self):
        s = Square(3, 3, 3, 3)
        with self.assertRaises(TypeError):
            s.to_dictionary(1)


if __name__ == "__main__":
    unittest.main()
