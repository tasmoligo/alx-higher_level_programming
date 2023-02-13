#!/usr/bin/python3
'''
Defines unittests for base.py
unittest classes:
    class TestBase_Instantation
'''

import unittest
from models.base import Base


class TestBase_Instantiation(unittest.TestCase):
    def test_no_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_id_none(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_over_one_args(self):
        with self.assertRaises(TypeError):
            print(Base(1, 2).id)

    def test_private_nb_instances(self):
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_instances)

    def test_string_id(self):
        self.assertEqual("Battery street", Base("Battery street").id)

    def test_float_id(self):
        self.assertEqual(2.3, Base(2.3).id)

    def test_complex_id(self):
        self.assertEqual(complex(3), Base(complex(3)).id)

    def test_dict_id(self):
        self.assertEqual({"Battery": 98, "school": 1}, Base({"Battery": 98, "
                                                             "school": 1}).id)

    def test_bool_id(self):
        self.assertEqual(True, Base(True).id)

    def test_inf_id(self):
        self.assertEqual(float('inf'), Base(float('inf')).id)

    def test_NaN_id(self):
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

    def test_list_id(self):
        self.assertEqual([1, 2, 3], Base([1, 2, 3]).id)

    def test_tuple_id(self):
        self.assertEqual((1, 2), Base((1, 2)).id)

    def test_set_id(self):
        self.assertEqual({1, 2, 3}, Base({1, 2, 3}).id)


if __name__ == "__main__":
    unittest.main()
