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


class TestRectangle_width(unittest.TestCase):
    """Unittests for testing of Rectangle width attribute."""

    def test_width_None(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 1)

    def test_str_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid", 1)

    def test_float_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(1.3, 1)

    def test_complex_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(complex(1), 2)

    def test_dict_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"Battery": 98, "School": 1}, 1)

    def test_bool_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("hello", 4)

    def test_list_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([1, 2, 3], 4)

    def test_set_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({1, 2, 3}, 4)

    def test_tuple_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((1, 2, 3), 4)

    def test_frozenset_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(frozenset({1, 2, 3, 1}), 4)

    def test_range_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(range(8), 4)

    def test_bytes_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(b'array', 3)

    def test_bytearray_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(bytearray(b'abcdefg'), 3)

    def test_memoryview_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(memoryview(b'abcedfg'), 5)

    def test_inf_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('inf'), 2)

    def test_nan_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('nan'), 2)

    def test_negative_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 2)

    def test_zero_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)


class TestRectangle_height(unittest.TestCase):
    """Unittests for testing initialization of Rectangle height attribute."""

    def test_height_None(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, None)

    def test_str_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "invalid")

    def test_float_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, 4.2)

    def test_complex_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, complex(2))

    def test_dict_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, {"Battery": 98, "School": 1})

    def test_list_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, [2, 3, 4])

    def test_set_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, {2, 3, 4})

    def test_tuple_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, (2, 3, 4))

    def test_frozenset_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, frozenset({2, 3, 4}))

    def test_range_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, range(8))

    def test_bytes_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, b'hello')

    def test_bytearray_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, bytearray(b'abcdefg'))

    def test_memoryview_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, memoryview(b'abcedfg'))

    def test_inf_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, float('inf'))

    def test_nan_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, float('nan'))

    def test_negative_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -1)

    def test_zero_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0)


class TestRectangle_x(unittest.TestCase):
    """Unittests for testing initialization of Rectangle x attribute."""

    def test_x_None(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, None)

    def test_str_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "invalid", 2)

    def test_float_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, 5.5, 9)

    def test_complex_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, complex(5))

    def test_dict_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, {"a": 1, "b": 2}, 2)

    def test_bool_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "hello", 2)

    def test_list_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, [1, 2, 3], 2)

    def test_set_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, {1, 2, 3}, 2)

    def test_tuple_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, (1, 2, 3), 2)

    def test_frozenset_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, frozenset({1, 2, 3, 1}))

    def test_range_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, range(5))

    def test_bytes_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, b'hello')

    def test_bytearray_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, bytearray(b'abcdefg'))

    def test_memoryview_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, memoryview(b'abcedfg'))

    def test_inf_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, float('inf'), 3)

    def test_nan_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, float('nan'), 3)

    def test_negative_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(1, 2, -3, 4)


class TestRectangle_y(unittest.TestCase):
    """Unittests for testing initialization of Rectangle y attribute."""

    def test_y_None(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, None)

    def test_str_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, "invalid")

    def test_float_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, 4.5)

    def test_complex_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, complex(4))

    def test_dict_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, {"prog": 1, "dev": 2})

    def test_list_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, [4, 5, 6])

    def test_set_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, {4, 5, 6})

    def test_tuple_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, (4, 5))

    def test_frozenset_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, frozenset({4, 5, 6}))

    def test_range_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, range(4))

    def test_bytes_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, b'Python')

    def test_bytearray_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, bytearray(b'abcdefg'))

    def test_memoryview_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, memoryview(b'abcedfg'))

    def test_inf_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, float('inf'))

    def test_nan_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, float('nan'))

    def test_negative_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(1, 2, 3, -4)


if __name__ == "__main__":
    unittest.main()
