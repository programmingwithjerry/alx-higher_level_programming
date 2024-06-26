#!/usr/bin/python3
import unittest
from models.base import Base
from models.square import Square
import json
import inspect

"""Generating test cases for the base module """


class test_base(unittest.TestCase):
    """Testing base """
    def test_id_none(self):
        """Providing no id"""
        b = Base()
        self.assertEqual(1, b.id)

    def test_id(self):
        """Providing a valid id"""
        b = Base(20)
        self.assertEqual(20, b.id)

    def test_id_zero(self):
        """Providing an id of 0"""
        b = Base(0)
        self.assertEqual(0, b.id)

    def test_id_negative(self):
        """Negative id"""
        b = Base(-10)
        self.assertEqual(-10, b.id)

    def test_id_dict(self):
        """Sending a dictionary as an id"""
        b = Base({"id": 50})
        self.assertEqual({"id": 50}, b.id)
    def test_id_string(self):
        """Sending a string as an id"""
        b = Base("Eneyellow")
        self.assertEqual("Eneyellow", b.id)

    def test_id_list(self):
        """Not an int id"""
        b = Base([1, 2, 3])
        self.assertEqual([1, 2, 3], b.id)

    def test_id_tuple(self):
        """Sending tuple"""
        b = Base((10,))
        self.assertEqual((50,), b.id)

    def test_to_json_type(self):
        """Testing the json string"""
        sq = Square(1)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string([json_dict])
        self.assertEqual(type(json_string), str)

    def test_to_json_value(self):
        """Testing the json string"""
        sq = Square(1, 0, 0, 306)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string([json_dict])
        self.assertEqual(json.loads(json_string),
                         [{"id": 306, "y": 0, "size": 1, "x": 0}])

    def test_to_json_None(self):
        """Testing the json string"""
        sq = Square(1, 0, 0, 306)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, "[]")

    def test_to_json_Empty(self):
        """Testing the json string"""
        sq = Square(1, 0, 0, 306)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")


class TestSquare(unittest.TestCase):
    """To test Base class' methods"""

    @classmethod
    def setUpClass(cls):
       """Set up class method for the doc tests"""
        cls.setup = inspect.getmembers(Base, inspect.isfunction)

    def test_module_docstring(self):
        """Tests if module docstring documentation exist"""
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_class_docstring(self):
        """Tests if class docstring documentation exist"""
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_func_docstrings(self):
        """Tests if methods docstring documntation exist"""
        for func in self.setup:
            self.assertTrue(len(func[1].__doc__) >= 1)
