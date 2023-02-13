#!/usr/bin/python3
'''Defines unittest for models/rectangle.py
unittest classes:
    class TestRectangle_Instantiation
'''
import unittest
from models.rectangle import Rectangle


class TestRectangle_Instantiaton(unittest.TestCase):
    '''The unittest for Rectangle class'''

    def test_no_arg(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_two_args(self):
        a = Rectangle(1, 2)
        s = Rectangle(3, 4)
        self.assertEqual(a.id, s.id - 1)

    def test_three_args(self):
        a = Rectangle(1, 2, 3)
        s = Rectangle(4, 5, 6)
        self.assertEqual(a.id, s.id - 1)

    def test_four_args(self):
        a = Rectangle(1, 2, 3, 4)
        s = Rectangle(5, 6, 7, 8)
        self.assertEqual(a.id, s.id - 1)

    def test_five_args(self):
        self.assertEqual(5, Rectangle(1, 2, 3, 4, 5).id)

    def test_more_than_five_args(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_width_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(1, 3, 0, 5, 2).__width)

    def test_height_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(1, 3, 0, 5, 2).__height)

    def test_x_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(1, 3, 0, 3, 2).__x)

    def test_y_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(1, 3, 0, 5, 2).__y)

    def test_width_getter(self):
        r = Rectangle(4, 3, 8, 4, 2)
        self.assertEqual(4, r.width)

    def test_width_setter(self):
        r = Rectangle(4, 3, 8, 4, 2)
        r.width = 15
        self.assertEqual(15, r.width)

    def test_height_getter(self):
        r = Rectangle(3, 5, 7, 9, 11)
        self.assertEqual(5, r.height)

    def test_height_setter(self):
        r = Rectangle(3, 5, 7, 9, 11)
        r.height = 13
        self.assertEqual(13, r.height)

    def test_x_getter(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(3, r.x)

    def test_x_setter(self):
        r = Rectangle(1, 2, 3, 4, 5)
        r.x = 11
        self.assertEqual(11, r.x)

    def test_y_getter(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(4, r.y)

    def test_y_setter(self):
        r = Rectangle(1, 2, 3, 4, 5)
        r.y = 12
        self.assertEqual(12, r.y)


if __name__ == "__main__":
    unittest.main()
