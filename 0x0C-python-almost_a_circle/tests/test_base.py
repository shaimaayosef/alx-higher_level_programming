#!/usr/bin/python3
"""Unittests for base
"""

import unittest
import os
from models.base import Base


class TestBase(unittest.TestCase):
    def test_create_instance(self):
        obj = Base()
        self.assertIsInstance(obj, Base)

    def test_create_instance_with_id(self):
        obj = Base(42)
        self.assertEqual(obj.id, 42)

    def test_create_multiple_instances(self):
        obj1 = Base()
        obj2 = Base()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_to_json_string(self):
        obj = Base(1)
        json_str = Base.to_json_string([obj.to_dictionary()])
        self.assertEqual(json_str, '[{"id": 1}]')

    def test_save_to_file(self):
        obj1 = Base(1)
        obj2 = Base(2)
        Base.save_to_file([obj1, obj2])
        with open("Base.json", "r") as file:
            content = file.read()
            self.assertEqual(content, '[{"id": 1}, {"id": 2}]')

    def test_from_json_string(self):
        json_str = '[{"id": 1}, {"id": 2}]'
        instances = Base.from_json_string(json_str)
        self.assertEqual(len(instances), 2)
        self.assertEqual(instances[0].id, 1)
        self.assertEqual(instances[1].id, 2)

    def test_create_instance_from_dictionary(self):
        obj_dict = {"id": 3}
        obj = Base.create(**obj_dict)
        self.assertIsInstance(obj, Base)
        self.assertEqual(obj.id, 3)

    def test_load_from_file(self):
        obj1 = Base(1)
        obj2 = Base(2)
        Base.save_to_file([obj1, obj2])
        instances = Base.load_from_file()
        self.assertEqual(len(instances), 2)
        self.assertEqual(instances[0].id, 1)
        self.assertEqual(instances[1].id, 2)

        # Clean up the created file
        os.remove("Base.json")

    def test_init_method_without_id(self):
        obj = Base()
        self.assertIsNotNone(obj.id)

    def test_init_method_with_id(self):
        obj = Base(42)
        self.assertEqual(obj.id, 42)


if __name__ == "__main__":
    unittest.main()
