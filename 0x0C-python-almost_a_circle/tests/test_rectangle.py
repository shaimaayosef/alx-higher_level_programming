#!/usr/bin/python3
# pylint: disable=line-too-long
"""Defines unittest for models/rectangle.py.
"""

import unittest
import os
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_create_rectangle(self):
        rect = Rectangle(2, 3)
        self.assertIsInstance(rect, Rectangle)
        self.assertEqual(rect.width, 2)
        self.assertEqual(rect.height, 3)

    def test_create_rectangle_with_invalid_width(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(-1, 3)

    def test_area_method(self):
        rect = Rectangle(4, 5)
        self.assertEqual(rect.area(), 20)

    def test_display_method(self):
        rect = Rectangle(3, 2)
        with unittest.mock.patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            rect.display()
            expected_output = "###\n###\n"
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_str_method(self):
        rect = Rectangle(4, 6, 2, 1, 42)
        self.assertEqual(str(rect), "[Rectangle] (42) 2/1 - 4/6")

    def test_update_method(self):
        rect = Rectangle(1, 2, 3, 4, 5)
        rect.update(10, 20, 30, 40, 50)
        self.assertEqual(rect.id, 10)
        self.assertEqual(rect.width, 20)
        self.assertEqual(rect.height, 30)
        self.assertEqual(rect.x, 40)
        self.assertEqual(rect.y, 50)

    def test_to_dictionary_method(self):
        rect = Rectangle(3, 4, 1, 2, 10)
        expected_dict = {'id': 10, 'width': 3, 'height': 4, 'x': 1, 'y': 2}
        self.assertEqual(rect.to_dictionary(), expected_dict)


if __name__ == "__main__":
    unittest.main()
