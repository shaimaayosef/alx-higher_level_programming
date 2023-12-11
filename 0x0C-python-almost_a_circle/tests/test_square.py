#!/usr/bin/python3
"""Unittests for base
"""

import unittest
import io
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_create_square(self):
        square = Square(4)
        self.assertIsInstance(square, Square)
        self.assertEqual(square.size, 4)

    def test_create_square_with_invalid_size(self):
        with self.assertRaises(ValueError):
            square = Square(0)

    def test_area_method(self):
        square = Square(5)
        self.assertEqual(square.area(), 25)

    def test_display_method(self):
        square = Square(3)
        with unittest.mock.patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            square.display()
            expected_output = "###\n###\n###\n"
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_str_method(self):
        square = Square(3, 2, 1, 42)
        self.assertEqual(str(square), "[Square] (42) 2/1 - 3")

    def test_update_method(self):
        square = Square(1, 2, 3, 5)
        square.update(10, 20, 30, 50)
        self.assertEqual(square.id, 10)
        self.assertEqual(square.size, 20)
        self.assertEqual(square.x, 30)
        self.assertEqual(square.y, 50)

    def test_to_dictionary_method(self):
        square = Square(3, 1, 2, 10)
        expected_dict = {'id': 10, 'size': 3, 'x': 1, 'y': 2}
        self.assertEqual(square.to_dictionary(), expected_dict)

    def test_size_getter(self):
        square = Square(4)
        self.assertEqual(square.size, 4)

    def test_size_setter(self):
        square = Square(4)
        square.size = 8
        self.assertEqual(square.size, 8)

    def test_size_setter_invalid_value(self):
        square = Square(4)
        with self.assertRaises(ValueError):
            square.size = 0


if __name__ == "__main__":
    unittest.main()
