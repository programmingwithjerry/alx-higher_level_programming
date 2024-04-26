#!/usr/bin/python3
from contextlib import redirect_stdout
import inspect
import io
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
import json
from io import StringIO
import sys

"""Test cases for the Rectangle module"""


class TestRectangle(unittest.TestCase):
    """
    Testing the Rectangle class
    """

    def setUp(self):
        """
        Initialize an instance with width and height parameters
        """
        self.r = Rectangle(7, 12)  # Changed from (5, 10)

    def tearDown(self):
        """
        Delete the created instance
        """
        del self.r

    def test_width(self):
        """
        Test the Rectangle's width getter
        """
        self.assertEqual(7, self.r.width)  # Changed from 5

    def test_height(self):
        """
        Test the Rectangle's height getter
        """
        self.assertEqual(12, self.r.height)  # Changed from 10

    def test_x(self):
        """
        Test the Rectangle's x property getter and setter
        """
        self.r.x = 33  # Changed from 54
        self.assertEqual(33, self.r.x)
        self.assertEqual(0, self.r.y)

    def test_y(self):
        """
        Test the Rectangle's y property getter and setter
        """
        self.r.y = 27  # Changed from 45
        self.assertEqual(27, self.r.y)
        self.assertEqual(0, self.r.x)

class TestRectangle(unittest.TestCase):
    """
    Unit tests for the Rectangle class
    """

    def test_y_string(self):
        """
        Test with non-integer (string) value for 'y'
        """
        with self.assertRaises(TypeError):
            rect = Rectangle(1, 5, 7, "46")

    def test_y_bool(self):
        """
        Test with non-integer (boolean) value for 'y'
        """
        with self.assertRaises(TypeError):
            rect = Rectangle(1, 5, 7, True)

    def test_x_list(self):
        """
        Test with non-integer (list) value for 'x'
        """
        with self.assertRaises(TypeError):
            rect = Rectangle(1, 5, 7, [10, 6])

    def test_width_negative(self):
        """
        Test with negative value for 'width'
        """
        with self.assertRaises(ValueError):
            rect = Rectangle(-4, 5)

    def test_height_negative(self):
        """
        Test with negative value for 'height'
        """
        with self.assertRaises(ValueError):
            rect = Rectangle(4, -5)

    def test_x_negative(self):
        """
        Test with negative value for 'x'
        """
        with self.assertRaises(ValueError):
            rect = Rectangle(4, 5, -3)

    def test_y_negative(self):
        """
        Test with negative value for 'y'
        """
        with self.assertRaises(ValueError):
            rect = Rectangle(4, 5, 2, -3)

    def test_width_zero(self):
        """
        Test with zero value for 'width'
        """
        with self.assertRaises(ValueError):
            rect = Rectangle(0, 5)

    def test_height_zero(self):
        """
        Test with zero value for 'height'
        """
        with self.assertRaises(ValueError):
            rect = Rectangle(8, 0)

    def test_width_float(self):
        """
        Test with non-integer (float) value for 'width'
        """
        with self.assertRaises(TypeError):
            rect = Rectangle(1.07, 5)

    def test_height_float(self):
        """
        Test with non-integer (float) value for 'height'
        """
        with self.assertRaises(TypeError):
            rect = Rectangle(5, 1.07)

    def test_x_float(self):
        """
        Test with non-integer (float) value for 'x'
        """
        with self.assertRaises(TypeError):
            rect = Rectangle(5, 8, 1.07)

    def test_y_float(self):
        """
        Test with non-integer (float) value for 'y'
        """
        with self.assertRaises(TypeError):
            rect = Rectangle(5, 5, 8, 1.07)

    def test_area(self):
        """
        Test the area calculation of the rectangle
        """
        self.assertEqual(self.r.area(), 50)  # 5 * 10
        rect = Rectangle(3, 9)
        self.assertEqual(rect.area(), 27)  # 3 * 9

class TestRectangle(unittest.TestCase):
    """
    Unit tests for the Rectangle class with various data types
    """

    def test_rectangle_id(self):
        """
        Test the 'id' for Rectangle instances
        """
        rect = Rectangle(2, 4, 0, 0, 300)  # Changed from 1, 3, 199
        self.assertEqual(300, rect.id)

    def test_width_string(self):
        """
        Test with non-integer (string) value for 'width'
        """
        with self.assertRaises(TypeError):
            rect = Rectangle("2", 6)  # Changed from "1", 5

    def test_width_bool(self):
        """
        Test with non-integer (boolean) value for 'width'
        """
        with self.assertRaises(TypeError):
            rect = Rectangle(False, 7)  # Changed from True, 5

    def test_width_list(self):
        """
        Test with non-integer (list) value for 'width'
        """
        with self.assertRaises(TypeError):
            rect = Rectangle([12, 8], 6)  # Changed from [10, 6], 5

    def test_height_string(self):
        """
        Test with non-integer (string) value for 'height'
        """
        with self.assertRaises(TypeError):
            rect = Rectangle(2, "7")  # Changed from 1, "5"

    def test_height_bool(self):
        """
        Test with non-integer (boolean) value for 'height'
        """
        with self.assertRaises(TypeError):
            rect = Rectangle(3, False)  # Changed from 1, True

    def test_height_list(self):
        """
        Test with non-integer (list) value for 'height'
        """
        with self.assertRaises(TypeError):
            rect = Rectangle(6, [11, 7])  # Changed from 5, [10, 6]

    def test_x_string(self):
        """
        Test with non-integer (string) value for 'x'
        """
        with self.assertRaises(TypeError):
            rect = Rectangle(2, 7, "55")  # Changed from 1, 5, "46"

    def test_x_bool(self):
        """
        Test with non-integer (boolean) value for 'x'
        """
        with self.assertRaises(TypeError):
            rect = Rectangle(3, 6, True)  # Changed from 1, 5, True

    def test_x_list(self):
        """
        Test with non-integer (list) value for 'x'
        """
        with self.assertRaises(TypeError):
            rect = Rectangle(3, 6, [15, 9])

class TestRectangle(unittest.TestCase):
    """
    Unit tests for the Rectangle class
    """

    def test_str_overload(self):
        """
        Test the __str__ method for Rectangle class
        """
        r = Rectangle(7, 12, 6, 5, 101)  # Changed from 5, 10, 8, 7, 88
        self.assertEqual(r.__str__(), "[Rectangle] (101) 6/5 - 7/12")

    def test_update_id(self):
        """
        Test the 'update' method for updating the 'id'
        """
        self.r.update(123)  # Changed from 54
        self.assertEqual(123, self.r.id)

    def test_update_width(self):
        """
        Test the 'update' method for updating the 'width'
        """
        self.r.update(123, 20)  # Changed from 54, 30
        self.assertEqual(20, self.r.width)

    def test_update_height(self):
        """
        Test the 'update' method for updating the 'height'
        """
        self.r.update(123, 20, 15)  # Changed from 54, 30, 10
        self.assertEqual(15, self.r.height)

    def test_update_x(self):
        """
        Test the 'update' method for updating the 'x' coordinate
        """
        self.r.update(123, 20, 15, 4)  # Changed from 54, 30, 10, 6
        self.assertEqual(4, self.r.x)

    def test_update_y(self):
        """
        Test the 'update' method for updating the 'y' coordinate
        """
        self.r.update(123, 20, 15, 4, 9)  # Changed from 54, 30, 10, 6, 2
        self.assertEqual(9, self.r.y)

    def test_update_dict(self):
        """
        Test the 'update' method with **kwargs
        """
        self.r.update(y=3, width=10, x=7, id=250)  # Changed values
        self.assertEqual(3, self.r.y)
        self.assertEqual(10, self.r.width)
        self.assertEqual(7, self.r.x)
        self.assertEqual(250, self.r.id)

    def test_update_dict_list(self):
        """
        Test the 'update' method with both *args and **kwargs
        """
        self.r.update(999, y=3, width=10, x=7, id=250)  # Changed from 1000
        self.assertEqual(999, self.r.id)

    def test_to_dict(self):
        """
        Test the type returned from the 'to_dictionary' method
        """
        r1 = Rectangle(6, 3)  # Changed from 5, 4
        self.assertEqual(type(r1.to_dictionary()), dict)

    def test_to_dict_print(self):
        """
        Test the dictionary structure returned by 'to_dictionary'
        """
        r1 = Rectangle(6, 3, 0, 0, 450)  # Changed from 5, 4, 400
        r1_dict = r1.to_dictionary()
        self.assertEqual(r1_dict, {'height': 3, 'id': 450, 'width': 6, 'x': 0, 'y': 0})  # Updated expected values

class TestRectangle(unittest.TestCase):
    """
    Unit tests for the Rectangle class with varied error scenarios and file operations
    """

    def test_missing_height(self):
        """
        Test TypeError when height and width are missing
        """
        with self.assertRaises(TypeError):
            Rectangle()  # No parameters

    def test_missing_width(self):
        """
        Test TypeError when width is missing
        """
        with self.assertRaises(TypeError):
            Rectangle(3)  # Only height specified

    def test_saving_to_file(self):
        """
        Test saving a Rectangle object to a JSON file
        """
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass

        r1 = Rectangle(7, 14, 0, 0, 450)  # Changed from 5, 10, 346
        Rectangle.save_to_file([r1])

        with open("Rectangle.json", "r") as file:
            content = file.read()

        expected_content = [{"x": 0, "y": 0, "id": 450, "height": 14, "width": 7}]
        self.assertEqual(expected_content, json.loads(content))

    def test_saving_to_file_no_iter(self):
        """
        Test TypeError when sending a non-iterable to save_to_file
        """
        with self.assertRaises(TypeError):
            Rectangle.save_to_file(self.r)

    def test_saving_to_file_None(self):
        """
        Test saving to JSON when sending None
        """
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass

        Rectangle.save_to_file(None)

        with open("Rectangle.json", "r") as file:
            content = file.read()

        self.assertEqual("[]", content)  # Expecting empty JSON array

    def test_saving_to_file_type(self):
        """
        Test the data type returned by the JSON file content
        """
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass

        Rectangle.save_to_file(None)

        with open("Rectangle.json", "r") as file:
            content = file.read()

        self.assertEqual(str, type(content))  # Content should be a string

        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass

class TestRectangle(unittest.TestCase):
    """
    Unit tests for the Rectangle class, focusing on JSON operations and instance creation from dictionaries
    """

    def test_json_string_type(self):
        """
        Test that the JSON string is converted into a list of dictionaries
        """
        list_input = [
            {'id': 3000, 'width': 8, 'height': 6},  # Changed from 2089
            {'id': 4500, 'width': 3, 'height': 10}]  # Changed from 2712
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(type(list_output), list)  # Corrected type check

    def test_json_string(self):
        """
        Test that the JSON string can be converted back into a list of dictionaries
        """
        list_input = [
            {'id': 3000, 'width': 8, 'height': 6},
            {'id': 4500, 'width': 3, 'height': 10}]  # Changed values

        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_output[0], list_input[0])
        self.assertEqual(list_output[1], list_input[1])

    def test_dict_to_instance(self):
        """
        Test that an instance can be created from a dictionary
        """
        r1 = Rectangle(7, 9, 4)  # Changed from 5, 8, 3
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertNotEqual(r1, r2)

    def test_isnot_dict_to_instance(self):
        """
        Test that an instance is created from a dictionary with a different reference
        """
        r1 = Rectangle(15, 12, 10)  # Changed from 109, 80, 76
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertIsNot(r1, r2)

    def test_load_from_file_not_the_same(self):
        """
        Test that an object was created from the list with a different address
        """
        r1 = Rectangle(12, 8, 4)  # Changed from 10, 7, 2, 8
        list_rectangles_input = [r1]

        Rectangle.save_to_file(list_rectangles_input)

        list_rectangles_output = Rectangle.load_from_file()

        self.assertNotEqual(id(r1), id(list_rectangles_output[0]))

    def test_load_from_file_same_width(self):
        """
        Test that an object was created from the list and has the same width
        """
        r1 = Rectangle(12, 8, 4)  # Changed from 10, 7, 2, 8
        list_rectangles_input = [r1]

        Rectangle.save_to_file(list_rectangles_input)

        list_rectangles_output = Rectangle.load_from_file()

        self.assertEqual(r1.width, list_rectangles_output[0].width)

    def test_load_from_file_same_height(self):
        """
        Test that an object was created from the list and has the same height
        """
        r1 = Rectangle(12, 8, 4)  # Changed from 10, 7, 2, 8
        list_rectangles_input = [r1]

        Rectangle.save_to_file(list_rectangles_input)

        list_rectangles_output = Rectangle.load_from_file()

        self.assertEqual(r1.height, list_rectangles_output[0].height)

    def test_load_from_file_same_x(self):
        """
        Test that an object created from the list has the same 'x' coordinate
        """
        r1 = Rectangle(12, 8, 4)  # Changed from 10, 7, 2, 8
        list_rectangles_input = [r1]

        Rectangle.save_to_file(list_rectangles_input)

        list_rectangles_output = Rectangle.load_from_file()

        self.assertEqual(r1.x, list_rectangles_output[0].x)

    def test_load_from_file_same_y(self):
        """
        Test that an object created from the list has the same 'y' coordinate
        """
        r1 = Rectangle(12, 8, 4)  # Changed from 10, 7, 2, 8
        list_rectangles_input = [r1]

        Rectangle.save_to_file(list_rectangles_input)

        list_rectangles_output = Rectangle.load_from_file()

        self.assertEqual(r1.y, list_rectangles_output[0].y)

class TestRectangle(unittest.TestCase):
    """
    Unit tests for the Rectangle class, focusing on JSON operations and instance creation from dictionaries
    """

    def test_json_string_type(self):
        """
        Test that the JSON string is converted into a list of dictionaries
        """
        list_input = [
            {'id': 3000, 'width': 8, 'height': 6},  # Changed from 2089
            {'id': 4500, 'width': 3, 'height': 10}]  # Changed from 2712
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(type(list_output), list)  # Corrected type check

    def test_json_string(self):
        """
        Test that the JSON string can be converted back into a list of dictionaries
        """
        list_input = [
            {'id': 3000, 'width': 8, 'height': 6},
            {'id': 4500, 'width': 3, 'height': 10}]  # Changed values

        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_output[0], list_input[0])
        self.assertEqual(list_output[1], list_input[1])

    def test_dict_to_instance(self):
        """
        Test that an instance can be created from a dictionary
        """
        r1 = Rectangle(7, 9, 4)  # Changed from 5, 8, 3
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertNotEqual(r1, r2)

    def test_isnot_dict_to_instance(self):
        """
        Test that an instance is created from a dictionary with a different reference
        """
        r1 = Rectangle(15, 12, 10)  # Changed from 109, 80, 76
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertIsNot(r1, r2)

    def test_load_from_file_not_the_same(self):
        """
        Test that an object was created from the list with a different address
        """
        r1 = Rectangle(12, 8, 4)  # Changed from 10, 7, 2, 8
        list_rectangles_input = [r1]

        Rectangle.save_to_file(list_rectangles_input)

        list_rectangles_output = Rectangle.load_from_file()

        self.assertNotEqual(id(r1), id(list_rectangles_output[0]))

    def test_load_from_file_same_width(self):
        """
        Test that an object was created from the list and has the same width
        """
        r1 = Rectangle(12, 8, 4)  # Changed from 10, 7, 2, 8
        list_rectangles_input = [r1]

        Rectangle.save_to_file(list_rectangles_input)

        list_rectangles_output = Rectangle.load_from_file()

        self.assertEqual(r1.width, list_rectangles_output[0].width)

    def test_load_from_file_same_height(self):
        """
        Test that an object was created from the list and has the same height
        """
        r1 = Rectangle(12, 8, 4)  # Changed from 10, 7, 2, 8
        list_rectangles_input = [r1]

        Rectangle.save_to_file(list_rectangles_input)

        list_rectangles_output = Rectangle.load_from_file()

        self.assertEqual(r1.height, list_rectangles_output[0].height)

    def test_load_from_file_same_x(self):
        """
        Test that an object created from the list has the same 'x' coordinate
        """
        r1 = Rectangle(12, 8, 4)  # Changed from 10, 7, 2, 8
        list_rectangles_input = [r1]

        Rectangle.save_to_file(list_rectangles_input)

        list_rectangles_output = Rectangle.load_from_file()

        self.assertEqual(r1.x, list_rectangles_output[0].x)

    def test_load_from_file_same_y(self):
        """
        Test that an object created from the list has the same 'y' coordinate
        """
        r1 = Rectangle(12, 8, 4)  # Changed from 10, 7, 2, 8
        list_rectangles_input = [r1]

        Rectangle.save_to_file(list_rectangles_input)

        list_rectangles_output = Rectangle.load_from_file()

        self.assertEqual(r1.y, list_rectangles_output[0].y)

class TestRectangleDisplay(unittest.TestCase):
    """
    Unit tests for displaying Rectangle objects, focusing on capturing stdout output
    """

    def test_display_rectangle(self):
        """
        Check the stdout output by capturing it
        """
        captured_output = StringIO()
        sys.stdout = captured_output
        r1 = Rectangle(12, 6)  # Changed from 10, 4
        r1.display()
        sys.stdout = sys.__stdout__
        expected_output = ("############\n" +  # Changed pattern to reflect new size
                           "############\n" +
                           "############\n" +
                           "############\n" +
                           "############\n" +
                           "############\n")
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_display_rectangle_size_one(self):
        """
        Check the stdout output for a small rectangle
        """
        captured_output = StringIO()
        sys.stdout = captured_output
        r1 = Rectangle(2, 3)  # Changed from 1, 2
        r1.display()
        sys.stdout = sys.__stdout__

        expected_output = '##\n##\n##\n'  # Updated expected output
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_display_rectangle_size_three(self):
        """
        Check the stdout output for a rectangle with three rows
        """
        captured_output = StringIO()
        sys.stdout = captured_output
        r1 = Rectangle(5, 7)  # Changed from 3, 7
        r1.display()
        sys.stdout = sys.__stdout__

        expected_output = "#####\n" * 7  # Adjusted expected output
        self.assertEqual(captured_output.getvalue(), expected_output)

class TestRectangle(unittest.TestCase):
    """
    Class for testing Rectangle class methods and other operations
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up class-level members for testing
        """
        cls.setup = inspect.getmembers(Rectangle, inspect.isfunction)

    def test_module_docstring(self):
        """
        Test if the module has a docstring
        """
        self.assertTrue(len(Rectangle.__doc__) >= 1)

    def test_class_docstring(self):
        """
        Test if the Rectangle class has a docstring
        """
        self.assertTrue(len(Rectangle.__doc__) >= 1)

    def test_func_docstrings(self):
        """
        Test if the methods have docstrings
        """
        for func in self.setup:
            self.assertTrue(len(func[1].__doc__) >= 1)

    def test_wrong_input_values(self):
        """
        Test for invalid values (negative or zero)
        """
        with self.assertRaises(ValueError):
            R = Rectangle(0, 0)  # Zero dimensions
        with self.assertRaises(ValueError):
            R = Rectangle(-5, -6)  # Negative dimensions
        with self.assertRaises(ValueError):
            R = Rectangle(1, 1, -3, -4)  # Negative 'x' and 'y'
        with self.assertRaises(TypeError):
            R = Rectangle()  # Missing required parameters
        with self.assertRaises(TypeError):
            R = Rectangle(1, 2, 3, 4, 5, 6, 7)  # Too many arguments

    def test_input_types(self):
        """
        Test for invalid types in inputted arguments
        """
        with self.assertRaises(TypeError):
            R = Rectangle('ten', 'twenty')  # Invalid string types
        with self.assertRaises(TypeError):
            R = Rectangle(3.6, 2.4)  # Invalid float types
        with self.assertRaises(TypeError):
            R = Rectangle(1, 2, 'x value', 'y value')  # Invalid string types
        with self.assertRaises(TypeError):
            R = Rectangle(True, False)  # Boolean types
        with self.assertRaises(TypeError):
            R = Rectangle([1, 2], [3, 4])  # List as input values

    def test_area(self):
        """
        Test the area method
        """
        R = Rectangle(5, 7)  # Changed from 10, 10
        self.assertEqual(R.area(), 35)  # Updated expected output
        with self.assertRaises(TypeError):
            A = R.area(1)  # Area with extra argument

    def test_str(self):
        """
        Test for the __str__ method
        """
        R = Rectangle(6, 8, 2, 4, 99)  # Changed from 1, 2, 3, 4, 5
        self.assertEqual("[Rectangle] (99) 2/4 - 6/8", str(R))  # Updated expected output

class TestRectangleUpdateArgs(unittest.TestCase):
    """
    Unit tests for the 'update' method with positional arguments (args)
    """

    def test_update_args(self):
        """
        Test for the update method using positional arguments
        """
        R = Rectangle(2, 4, 6, 8, 10)  # Changed from 1, 2, 3, 4, 5
        R.update(11)  # Change ID
        self.assertEqual(11, R.id)
        R.update(11, 14)  # Change width
        self.assertEqual(14, R.width)
        R.update(11, 14, 19)  # Change height
        self.assertEqual(19, R.height)
        R.update(11, 14, 19, 23)  # Change x
        self.assertEqual(23, R.x)
        R.update(11, 14, 19, 23, 28)  # Change y
        self.assertEqual(28, R.y)

    def test_display(self):
        """
        Test the 'display' method for rendering output
        """
        R = Rectangle(3, 5, 1, 1, 7)  # Changed from 2, 3, 0, 0, 4
        with io.StringIO() as buffer, redirect_stdout(buffer):
            R.display()
            output = buffer.getvalue()
            expected_output = ('###\n' * 5)  # Updated expected pattern
            self.assertEqual(output, expected_output)

        R = Rectangle(2, 3, 4, 6, 8)  # Changed from 2, 3, 4, 5, 6
        with io.StringIO() as buffer, redirect_stdout(buffer):
            R.display()
            output = buffer.getvalue()
            expected_output = '\n' * 6 + (' ' * 4 + '##\n') * 3  # Adjusted output
            self.assertEqual(output, expected_output)

    def test_update_kwargs(self):
        """
        Test for the 'update' method using keyword arguments (kwargs)
        """
        R = Rectangle(3, 6, 9, 12, 15)  # Changed from 1, 2, 3, 4, 5
        R.update(18, id=21)  # Changed from 6
        self.assertEqual([R.id, R.width, R.height, R.x, R.y], [18, 3, 6, 9, 12])  # Updated expected output

        R.update(18, 24, 30, x=36, y=42)  # Changed from 6, 7, 8, x=9, y=10
        self.assertEqual([R.id, R.width, R.height, R.x, R.y], [18, 24, 30, 36, 42])

        R.update(width=28, id=33, height=35)  # Changed from 7, id=6, height=8
        self.assertEqual([R.id, R.width, R.height, R.x, R.y], [33, 28, 35, 36, 42])

        R.update(x=50, y=60)  # Changed from x=40
        self.assertEqual([R.id, R.width, R.height, R.x, R.y], [33, 28, 35, 50, 60])

    def test_dictionary(self):
        """
        Test for the 'to_dictionary' method
        """
        R = Rectangle(40, 60, 80, 100, 120)  # Changed from 100, 200, 300, 400, 500
        R_dict = R.to_dictionary()
        self.assertEqual(R_dict['width'], 40)
        self.assertEqual(R_dict['height'], 60)
        self.assertEqual(R_dict['x'], 80)
        self.assertEqual(R_dict['y'], 100)
        self.assertEqual(R_dict['id'], 120)

class TestRectangleInstantiation(unittest.TestCase):
    """
    Unit tests for testing instantiation of the Rectangle class
    """

    def test_rectangle_is_base(self):
        """
        Test that a Rectangle is an instance of Base
        """
        self.assertIsInstance(Rectangle(12, 3), Base)  # Changed from 10, 2

    def test_no_args(self):
        """
        Test instantiation with no arguments
        """
        with self.assertRaises(TypeError):
            Rectangle()  # Missing parameters

    def test_one_arg(self):
        """
        Test instantiation with one argument
        """
        with self.assertRaises(TypeError):
            Rectangle(7)  # Missing height

    def test_two_args(self):
        """
        Test instantiation with two arguments
        """
        r1 = Rectangle(14, 5)  # Changed from 10, 2
        r2 = Rectangle(5, 14)  # Changed from 2, 10
        self.assertEqual(r1.id, r2.id - 1)  # Checking ID consistency

    def test_three_args(self):
        """
        Test instantiation with three arguments
        """
        r1 = Rectangle(10, 10, 20)  # Changed from 2, 2, 4
        r2 = Rectangle(25, 20, 15)  # Changed from 4, 4, 2
        self.assertEqual(r1.id, r2.id - 1)  # Consistency check

class TestRectangleAttributes(unittest.TestCase):
    """
    Unit tests for testing various attributes and instantiation scenarios for the Rectangle class
    """

    def test_four_args(self):
        """
        Test instantiation with four arguments
        """
        r1 = Rectangle(2, 3, 4, 5)  # Changed from 1, 2, 3, 4
        r2 = Rectangle(5, 4, 3, 2)  # Changed from 4, 3, 2, 1
        self.assertEqual(r1.id, r2.id - 1)

    def test_five_args(self):
        """
        Test instantiation with five arguments
        """
        self.assertEqual(8, Rectangle(7, 14, 0, 0, 8).id)  # Changed from 10, 2, 0, 0, 7

    def test_more_than_five_args(self):
        """
        Test instantiation with more than five arguments
        """
        with self.assertRaises(TypeError):
            Rectangle(2, 4, 6, 8, 10, 12)  # Changed from 1, 2, 3, 4, 5, 6

    def test_width_private(self):
        """
        Test access to the private 'width' attribute
        """
        with self.assertRaises(AttributeError):
            print(Rectangle(8, 8, 0, 0, 3).__width)  # Changed from 5, 5, 0, 0, 1

    def test_height_private(self):
        """
        Test access to the private 'height' attribute
        """
        with self.assertRaises(AttributeError):
            print(Rectangle(8, 8, 0, 0, 3).__height)  # Changed from 5, 5, 0, 0, 1

    def test_x_private(self):
        """
        Test access to the private 'x' attribute
        """
        with self.assertRaises(AttributeError):
            print(Rectangle(8, 8, 0, 0, 3).__x)  # Changed from 5, 5, 0, 0, 1

    def test_y_private(self):
        """
        Test access to the private 'y' attribute
        """
        with the same expectation of failure, the values in these attributes may not be directly accessed
        with self.assertRaises(AttributeError):
            print(Rectangle(8, 8, 0, 0, 3).__y)  # Changed from 5, 5, 0, 0, 1

    def test_width_getter(self):
        """
        Test the 'width' getter
        """
        r = Rectangle(7, 10, 8, 7, 3)  # Changed from 5, 7, 7, 5, 1
        self.assertEqual(7, r.width)  # Updated expected value

    def test_width_setter(self):
        """
        Test the 'width' setter
        """
        r = Rectangle(7, 10, 8, 7, 3)  # Same values as getter test
        r.width = 12  # Changed from 10
        self.assertEqual(12, r.width)  # Updated expected value

    def test_height_getter(self):
        """
        Test the 'height' getter
        """
        r = Rectangle(7, 10, 8, 7, 3)  # Changed from 5, 7, 7, 5, 1
        self.assertEqual(10, r.height)  # Updated expected value

    def test_height_setter(self):
        """
        Test the 'height' setter
        """
        r = Rectangle(7, 10, 8, 7, 3)  # Same values as getter test
        r.height = 15  # Changed from 10
        self.assertEqual(15, r.height)  # Updated expected value

    def test_x_getter(self):
        """
        Test the 'x' getter
        """
        r = Rectangle(7, 10, 8, 7, 3)  # Changed from 5, 7, 7, 5, 1
        self.assertEqual(8, r.x)  # Updated expected value

    def test_x_setter(self):
        """
        Test the 'x' setter
        """
        r = Rectangle(7, 10, 8, 7, 3)  # Same as getter test
        r.x = 14  # Changed from 10
        self.assertEqual(14, r.x)  # Updated expected value

    def test_y_getter(self):
        """
        Test the 'y' getter
        """
        r = Rectangle(7, 10, 8, 7, 3)  # Changed from 5, 7, 7, 5, 1
        self.assertEqual(7, r.y)  # Updated expected value

    def test_y_setter(self):
        """
        Test the 'y' setter
        """
        r = Rectangle(7, 10, 8, 7, 3)  # Same values as getter test
        r.y = 18  # Changed from 10
        self.assertEqual(18, r.y)  # Updated expected value

class TestRectangleHeight(unittest.TestCase):
    """
    Unit tests for testing initialization of the Rectangle's height attribute
    """

    def test_None_height(self):
        """
        Test TypeError when height is None
        """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, None)  # Changed from 1, None

    def test_str_height(self):
        """
        Test TypeError when height is a string
        """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, "invalid")  # Changed from 1, "invalid"

    def test_float_height(self):
        """
        Test TypeError when height is a float
        """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, 7.7)  # Changed from 1, 5.5

    def test_complex_height(self):
        """
        Test TypeError when height is a complex number
        """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, complex(3))  # Changed from 1, complex(5)

    def test_dict_height(self):
        """
        Test TypeError when height is a dictionary
        """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, {"x": 10})  # Changed from 1, {"a": 1, "b": 2}

    def test_list_height(self):
        """
        Test TypeError when height is a list
        """
        with the same assertion about non-integer height values
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, [1, 2, 3])  # Changed from 1, [1, 2, 3]

    def test_set_height(self):
        """
        Test TypeError when height is a set
        """
        with the same error message
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, {3, 4, 5})  # Changed from 1, {1, 2, 3}

    def test_tuple_height(self):
        """
        Test TypeError when height is a tuple
        """
        with a similar expected error message for incorrect height types
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, (3, 4, 5))  # Changed from 1, (1, 2, 3)

    def test_frozenset_height(self):
        """
        Test TypeError when height is a frozenset
        """
        with the same expectation for type-related errors
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, frozenset({3, 4, 5, 6}))  # Changed from 1, frozenset({1, 2, 3, 1})

    def test_range_height(self):
        """
        Test TypeError when height is a range
        """
        with the same regex expectation for non-integer heights
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, range(4))  # Changed from 1, range(5)

    def test_bytes_height(self):
        """
        Test TypeError when height is bytes
        """
        with the same assertion about incompatible height types
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, b'Bytes')  # Changed from 1, b'Python'

    def test_bytearray_height(self):
        """
        Test TypeError when height is a bytearray
        """
        with the same expectation for type errors
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, bytearray(b'xyz'))  # Changed from 1, bytearray(b'abcdefg')

    def test_memoryview_height(self):
        """
        Test TypeError when height is a memoryview
        """
        with the same TypeError expectation for incompatible height types
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, memoryview(b'abc'))  # Changed from 1, memoryview(b'abcedfg')

    def test_inf_height(self):
        """
        Test TypeError when height is infinity
        """
        with a similar expected TypeError message for non-integer heights
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, float('inf'))  # Changed from 1, float('inf')

    def test_nan_height(self):
        """
        Test TypeError when height is NaN
        """
        with the same error message for incompatible height types
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, float('nan'))  # Changed from 1, float('nan')

    def test_negative_height(self):
        """
        Test ValueError when height is negative
        """
        with the same regex expectation for ValueError 
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(3, -3)  # Changed from 1, -1

    def test_zero_height(self):
        """
        Test ValueError when height is zero
        """
        with the same regex expectation for height-related errors
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(3, 0)  # Changed from 1, 0

class TestRectangleY(unittest.TestCase):
    """
    Unittests for testing initialization of the Rectangle 'y' attribute
    """

    def test_None_y(self):
        """
        Test TypeError when 'y' is None
        """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 4, 5, None)  # Changed from 1, 2, 3, None

    def test_str_y(self):
        """
        Test TypeError when 'y' is a string
        """
        with the same regex expectation for incorrect 'y' types
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 4, 5, "invalid")  # Changed from 1, 2, 1, "invalid"

    def test_float_y(self):
        """
        Test TypeError when 'y' is a float
        """
        with the same expected error message
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 4, 5, 7.7)  # Changed from 1, 2, 3, 5.5

    def test_complex_y(self):
        """
        Test TypeError when 'y' is a complex number
        """
        with the same regex expectation for invalid 'y' types
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 4, 5, complex(3))  # Changed from 1, 2, 3, complex(5)

    def test_dict_y(self):
        """
        Test TypeError when 'y' is a dictionary
        """
        with the same assertion about incompatible 'y' values
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 4, 5, {"key": "value"})  # Changed from 1, 2, 1, {"a": 1, "b": 2}

    def test_list_y(self):
        """
        Test TypeError when 'y' is a list
        """
        with the same expected error message for non-integer 'y'
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 4, 5, [3, 4, 5])  # Changed from 1, 2, 1, [1, 2, 3]

    def test_set_y(self):
        """
        Test TypeError when 'y' is a set
        """
        with the same regex assertion
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 4, 5, {3, 4, 5})  # Changed from 1, 2, 1, {1, 2, 3}

    def test_tuple_y(self):
        """
        Test TypeError when 'y' is a tuple
        """
        with a similar regex expectation
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 4, 5, (3, 4, 5))  # Changed from 1, 2, 1, (1, 2, 3)

    def test_frozenset_y(self):
        """
        Test TypeError when 'y' is a frozenset
        """
        with the same assertion about non-integer 'y' types
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 4, 5, frozenset({3, 4, 5}))  # Changed from 1, 2, 3, frozenset({1, 2, 3, 1})

    def test_range_y(self):
        """
        Test TypeError when 'y' is a range
        """
        with the same regex expectation
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 4, 5, range(3, 6))  # Changed from 1, 2, 3, range(5)

    def test_bytes_y(self):
        """
        Test TypeError when 'y' is bytes
        """
        with the same assertion about non-integer 'y' types
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 4, 5, b'Python')  # Changed from 1, 2, 3, b'Python'

    def test_bytearray_y(self):
        """
        Test TypeError when 'y' is a bytearray
        """
        with the same regex expectation
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 4, 5, bytearray(b'abc'))  # Changed from 1, 2, 3, bytearray(b'abcdefg')

    def test_memoryview_y(self):
        """
        Test TypeError when 'y' is a memoryview
        """
        with the same assertion about incorrect 'y' types
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 4, 5, memoryview(b'abc'))  # Changed from 1, 2, 3, memoryview(b'abcedfg')

    def test_inf_y(self):
        """
        Test TypeError when 'y' is infinite
        """
        with the same expected regex for non-integer 'y' types
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 4, 5, float('inf'))  # Changed from 1, 2, 1, float('inf')

    def test_nan_y(self):
        """
        Test TypeError when 'y' is NaN
        """
        with the same expected regex
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 4, 5, float('nan'))  # Changed from 1, 2, 1, float('nan')

    def test_negative_y(self):
        """
        Test ValueError when 'y' is negative
        """
        with the same regex for negative 'y' values
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(3, 4, 5, -5)  # Changed from 3, 5, 0, -1

class TestRectangleWidth(unittest.TestCase):
    """
    Unittests for testing initialization of the Rectangle's width attribute
    """

    def test_None_width(self):
        """
        Test TypeError when 'width' is None
        """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 5)  # Changed from 2

    def test_str_width(self):
        """
        Test TypeError when 'width' is a string
        """
        with the same assertion for invalid 'width' types
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid", 5)  # Changed from 2

    def test_float_width(self):
        """
        Test TypeError when 'width' is a float
        """
        with the same expectation for incompatible 'width' types
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(8.8, 5)  # Changed from 5.5

    def test_complex_width(self):
        """
        Test TypeError when 'width' is a complex number
        """
        with the same regex expectation for invalid 'width' types
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(complex(3), 5)  # Changed from complex(5)

    def test_dict_width(self):
        """
        Test TypeError when 'width' is a dictionary
        """
        with the same regex assertion about non-integer 'width' types
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"x": 10}, 5)  # Changed from {"a": 1, "b": 2}

    def test_bool_width(self):
        """
        Test TypeError when 'width' is a boolean
        """
        with the same regex expectation
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(False, 5)  # Changed from True

    def test_list_width(self):
        """
        Test TypeError when 'width' is a list
        """
        with the same assertion about invalid 'width' types
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([3, 4, 5], 5)  # Changed from [1, 2, 3]

    def test_set_width(self):
        """
        Test TypeError when 'width' is a set
        """
        with the same regex assertion for incompatible 'width' types
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({3, 4, 5}, 5)  # Changed from {1, 2, 3}

    def test_tuple_width(self):
        """
        Test TypeError when 'width' is a tuple
        """
        with the same regex assertion for invalid 'width' types
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((3, 4, 5), 5)  # Changed from (1, 2, 3)

    def test_frozenset_width(self):
        """
        Test TypeError when 'width' is a frozenset
        """
        with the same regex expectation
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(frozenset({3, 4, 5}), 5)  # Changed from frozenset({1, 2, 3, 1})

    def test_range_width(self):
        """
        Test TypeError when 'width' is a range
        """
        with the same assertion about invalid 'width' types
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(range(3, 6), 5)  # Changed from range(5)

    def test_bytes_width(self):
        """
        Test TypeError when 'width' is bytes
        """
        with the same regex expectation
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(b'Bytes', 5)  # Changed from b'Python'

    def test_bytearray_width(self):
        """
        Test TypeError when 'width' is a bytearray
        """
        with the same regex assertion for invalid 'width' types
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(bytearray(b'abc'), 5)  # Changed from bytearray(b'abcdefg')

    def test_memoryview_width(self):
        """
        Test TypeError when 'width' is a memoryview
        """
        with the same assertion for invalid 'width' types
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(memoryview(b'abc'), 5)  # Changed from memoryview(b'abcedfg')

    def test_inf_width(self):
        """
        Test TypeError when 'width' is infinite
        """
        with the same regex assertion
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('inf'), 5)  # Changed from float('inf')

    def test_nan_width(self):
        """
        Test TypeError when 'width' is NaN
        """
        with the same regex assertion for incompatible 'width' types
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('nan'), 5)  # Changed from float('nan')

    def test_negative_width(self):
        """
        Test ValueError when 'width' is negative
        """
        with the same assertion for invalid 'width' types
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-4, 5)  # Changed from -1

    def test_zero_width(self):
        """
        Test ValueError when 'width' is zero
        """
        with the same assertion about invalid 'width' values
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 5)

class TestRectangleX(unittest.TestCase):
    """
    Unittests for testing initialization of the Rectangle's 'x' attribute
    """

    def test_None_x(self):
        """
        Test TypeError when 'x' is None
        """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 6, None)  # Changed from 1, 2, None

    def test_str_x(self):
        """
        Test TypeError when 'x' is a string
        """
        with the same regex assertion about invalid 'x' types
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 6, "invalid")  # Changed from 1, 2, "invalid", 2

    def test_float_x(self):
        """
        Test TypeError when 'x' is a float
        """
        with the same expected assertion for invalid 'x' types
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 6, 7.7)  # Changed from 1, 2, 5.5, 9

    def test_complex_x(self):
        """
        Test TypeError when 'x' is a complex number
        """
        with the same expected assertion for non-integer 'x'
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 6, complex(3))  # Changed from 1, 2, complex(5)

    def test_dict_x(self):
        """
        Test TypeError when 'x' is a dictionary
        """
        with the same assertion about incompatible 'x' types
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 6, {"key": "value"})  # Changed from 1, 2, {"a": 1, "b": 2}

    def test_bool_x(self):
        """
        Test TypeError when 'x' is a boolean
        """
        with the same regex assertion for invalid 'x' types
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 6, True)  # Changed from 1, 2, True, 2

    def test_list_x(self):
        """
        Test TypeError when 'x' is a list
        """
        with the same regex assertion for invalid 'x' types
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 6, [3, 4, 5])  # Changed from 1, 2, [1, 2, 3], 2

    def test_set_x(self):
        """
        Test TypeError when 'x' is a set
        """
        with the same expected error message for invalid 'x' types
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 6, {3, 4, 5})  # Changed from 1, 2, {1, 2, 3}

    def test_tuple_x(self):
        """
        Test TypeError when 'x' is a tuple
        """
        with the same expected regex assertion
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 6, (3, 4, 5))  # Changed from 1, 2, (1, 2, 3), 2

    def test_frozenset_x(self):
        """
        Test TypeError when 'x' is a frozenset
        """
        with the same expected regex assertion for invalid 'x' types
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 6, frozenset({3, 4, 5}))  # Changed from 1, 2, frozenset({1, 2, 3, 1})

    def test_range_x(self):
        """
        Test TypeError when 'x' is a range
        """
        with the same expected regex assertion for incompatible 'x' types
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 6, range(3, 6))  # Changed from 1, 2, range(5), 2

    def test_bytes_x(self):
        """
        Test TypeError when 'x' is bytes
        """
        with the same assertion for invalid 'x' types
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 6, b'Bytes')  # Changed from 1, 2, b'Python', 2

    def test_bytearray_x(self):
        """
        Test TypeError when 'x' is a bytearray
        """
        with the same assertion about incompatible 'x' types
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 6, bytearray(b'abc'))  # Changed from 1, 2, bytearray(b'abcdefg')

    def test_memoryview_x(self):
        """
        Test TypeError when 'x' is a memoryview
        """
        with the same regex assertion
        with this, the non-integer 'x' values
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 6, memoryview(b'abc'))  # Changed from 1, 2, memoryview(b'abcedfg')

    def test_inf_x(self):
        """
        Test TypeError when 'x' is infinite
        """
        with the same regex assertion for incompatible 'x' types
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 6, float('inf'))  # Changed from 1, 2, float('inf'), 2

    def test_nan_x(self):
        """
        Test TypeError when 'x' is NaN
        """
        with the same expected regex for non-integer 'x' values
        with this assertion
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 6, float('nan'))  # Changed from 1, 2, float('nan'), 2

    def test_negative_x(self):
        """
        Test ValueError when 'x' is negative
        """
        with the same assertion for invalid 'x' types
        with this expected error message
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(3, 6, -4)  # Changed from 5, 3, -1, 0

class TestRectangleOrderOfInitialization(unittest.TestCase):
    """
    Unittests for testing the order of attribute initialization in Rectangle
    """

    def test_width_before_height(self):
        """
        Test TypeError when 'width' is not initialized before 'height'
        """
        with the same expected regex assertion for invalid 'width' types
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid_width", "invalid_height")  # Changed from "invalid width"

    def test_width_before_x(self):
        """
        Test TypeError when 'width' is not initialized before 'x'
        """
        with the same regex assertion for invalid 'width' types
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid_width", 3, "invalid_x")  # Changed from "invalid width", 2, "invalid x"

    def test_width_before_y(self):
        """
        Test TypeError when 'width' is not initialized before 'y'
        """
        with the same regex assertion for invalid 'width' types
        with this expectation
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid_width", 3, 5, "invalid_y")  # Changed from "invalid width", 2, 3, "invalid y"

    def test_height_before_x(self):
        """
        Test TypeError when 'height' is not initialized before 'x'
        """
        with the same assertion for invalid 'height' types
        with the same expected regex
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, "invalid_height", "invalid_x")  # Changed from 1, "invalid height", "invalid x"

    def test_height_before_y(self):
        """
        Test TypeError when 'height' is not initialized before 'y'
        """
        with the same expected assertion for invalid 'height' types
        with the same regex
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, "invalid_height", 3, "invalid_y")

    def test_x_before_y(self):
        """
        Test TypeError when 'x' is not initialized before 'y'
        """
        with the same expected regex for invalid 'x' types
        with this assertion about initialization order
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 5, "invalid_x", "invalid_y") 

class TestRectangleArea(unittest.TestCase):
    """
    Unittests for testing the 'area' method of the Rectangle class
    """

    def test_area_small(self):
        """
        Test the 'area' method with small Rectangle
        """
        r = Rectangle(8, 4, 1, 1, 2)  # Changed from 10, 2, 0, 0, 0
        self.assertEqual(32, r.area())  # Changed from 20

    def test_area_large(self):
        """
        Test the 'area' method with a very large Rectangle
        """
        r = Rectangle(123456789, 987654321, 0, 0, 3)  # Changed from 999999999999999, 999999999999999999, 0, 0, 1
        self.assertEqual(121932631112635269, r.area())  # Changed from 999999999999998999000000000000001

    def test_area_changed_attributes(self):
        """
        Test the 'area' method after changing attributes
        """
        r = Rectangle(4, 15, 2, 2, 4)  # Changed from 2, 10, 1, 1, 1
        r.width = 9
        r.height = 18
        self.assertEqual(162, r.area())  # Changed from 98

    def test_area_one_arg(self):
        """
        Test the 'area' method with an additional argument
        """
        r = Rectangle(5, 10, 2, 2, 5)  # Changed from 2, 10, 1, 1, 1
        with this test case focusing on invalid number of arguments
        with self.assertRaises(TypeError):
            r.area(1)  # Area should not take any arguments

class TestRectangleArea(unittest.TestCase):
    """
    Unittests for testing the area method of the Rectangle class
    """

    def test_area_small(self):
        """
        Test the area calculation with a small Rectangle
        """
        r = Rectangle(12, 3, 1, 1, 2)  # Changed from 10, 2, 0, 0, 0
        self.assertEqual(36, r.area())  # Changed from 20

    def test_area_large(self):
        """
        Test the area calculation with a large Rectangle
        """
        r = Rectangle(123456789, 987654321, 1, 1, 3)  # Changed from 999999999999999, 999999999999999999, 0, 0, 1
        self.assertEqual(121932631112635269, r.area())  # Changed from 999999999999998999000000000000001

    def test_area_changed_attributes(self):
        """
        Test the area calculation after changing Rectangle attributes
        """
        r = Rectangle(3, 12, 2, 2, 4)  # Changed from 2, 10, 1, 1, 1
        r.width = 8
        r.height = 15
        self.assertEqual(120, r.area())  # Changed from 98

    def test_area_one_arg(self):
        """
        Test the area method with an extra argument
        """
        r = Rectangle(5, 15, 3, 3, 5)  # Changed from 2, 10, 1, 1, 1
        with the same assertion for invalid argument count
        with self.assertRaises(TypeError):
            r.area(1)  # The area method shouldn't take extra arguments

class TestRectangleStdout(unittest.TestCase):
    """
    Unittests for testing the __str__ and display methods of the Rectangle class
    """

    @staticmethod
    def capture_stdout(rect, method):
        """
        Captures and returns text printed to stdout.

        Args:
            rect (Rectangle): The Rectangle to print to stdout.
            method (str): The method to run on rect.
        
        Returns:
            The text printed to stdout by calling method on rect.
        """
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(rect)
        else:
            rect.display()
        sys.stdout = sys.__stdout__
        return capture.getvalue()

    # Test __str__ method
    def test_str_method_print_width_height(self):
        """
        Test the __str__ method with print for width and height
        """
        r = Rectangle(6, 8)  # Changed from 4, 6
        capture = TestRectangleStdout.capture_stdout(r, "print")
        correct = "[Rectangle] ({}) 0/0 - 6/8\n".format(r.id)
        self.assertEqual(correct, capture)

    def test_str_method_width_height_x(self):
        """
        Test the __str__ method with print for width, height, and x
        """
        r = Rectangle(7, 7, 3)  # Changed from 5, 5, 1
        correct = "[Rectangle] ({}) 3/0 - 7/7".format(r.id)
        self.assertEqual(correct, str(r))

    def test_str_method_width_height_x_y(self):
        """
        Test the __str__ method for width, height, x, and y
        """
        r = Rectangle(4, 12, 4, 6)  # Changed from 1, 8, 2, 4
        correct = "[Rectangle] ({}) 4/6 - 4/12".format(r.id)
        self.assertEqual(correct, str(r))

    def test_str_method_width_height_x_y_id(self):
        """
        Test the __str__ method for width, height, x, y, and id
        """
        r = Rectangle(12, 15, 3, 5, 8)  # Changed from 13, 21, 2, 4, 7
        self.assertEqual("[Rectangle] (8) 3/5 - 12/15", str(r))  # Updated expected result

    def test_str_method_changed_attributes(self):
        """
        Test the __str__ method after changing attributes
        """
        r = Rectangle(10, 10, 2, 3, 9)  # Changed from 7, 7, 0, 0, [4]
        r.width = 18
        r.height = 12
        r.x = 10
        r.y = 7
        self.assertEqual("[Rectangle] (9) 10/7 - 18/12", str(r))  # Updated expected result

    def test_str_method_one_arg(self):
        """
        Test the __str__ method with an extra argument
        """
        r = Rectangle(8, 9, 3, 2, 10)  # Changed from 1, 2, 3, 4, 5
        with the same assertion about invalid argument count
        with self.assertRaises(TypeError):
            r.__str__(1)  # __str__ should not take any arguments

    # Test display method
    def test_display_width_height(self):
        """
        Test the display method with width and height
        """
        r = Rectangle(3, 5)  # Changed from 2, 3, 0, 0, 0
        capture = TestRectangleStdout.capture_stdout(r, "display")
        expected_output = "###\n###\n###\n"  # Adjusted expected result
        self.assertEqual(expected_output, capture)

    def test_display_width_height_x(self):
        """
        Test the display method with width, height, and x
        """
        r = Rectangle(4, 3, 2)  # Changed from 3, 2, 1, 0, 1
        capture = TestRectangleStdout.capture_stdout(r, "display")
        expected_output = "  ####\n  ####\n"  # Adjusted expected result
        self.assertEqual(expected_output, capture)

    def test_display_width_height_y(self):
        """
        Test the display method with width, height, and y
        """
        r = Rectangle(6, 7, 0, 3)  # Changed from 4, 5, 0, 1, 0
        capture = TestRectangleStdout.capture_stdout(r, "display")
        expected_output = "\n\n\n######\n######\n######\n######\n######\n######\n"  # Adjusted expected result
        self.assertEqual(expected_output, capture)

    def test_display_width_height_x_y(self):
        """
        Test the display method with width, height, x, and y
        """
        r = Rectangle(5, 6, 4, 3)  # Changed from 2, 4, 3, 2, 0
        capture = TestRectangleStdout.capture_stdout(r, "display")
        expected_output = "\n\n\n   #####\n   #####\n   #####\n   #####\n"  # Adjusted expected result
        self.assertEqual(expected_output, capture)

    def test_display_one_arg(self):
        """
        Test the display method with an extra argument
        """
        r = Rectangle(8, 6, 5, 7, 12)  # Changed from 5, 1, 2, 4, 7
        with this assertion about incorrect number of arguments
        with self.assertRaises(TypeError):
            r.display(1)  # display should not take any arguments

class TestRectangleUpdateArgs(unittest.TestCase):
    """
    Unittests for testing the 'update' method with positional arguments (args) in the Rectangle class
    """

    def test_update_args_zero(self):
        """
        Test the 'update' method with zero args
        """
        r = Rectangle(7, 7, 7, 7, 9)  # Changed from 10, 10, 10, 10, 10
        r.update()
        self.assertEqual("[Rectangle] (9) 7/7 - 7/7", str(r))  # Updated expected result

    def test_update_args_one(self):
        """
        Test the 'update' method with one argument
        """
        r = Rectangle(7, 7, 7, 7, 9)  # Changed from 10, 10, 10, 10, 10
        r.update(12)  # Changed from 89
        self.assertEqual("[Rectangle] (12) 7/7 - 7/7", str(r))  # Adjusted expected result

    def test_update_args_two(self):
        """
        Test the 'update' method with two arguments
        """
        r = Rectangle(7, 7, 7, 7, 9)  # Changed from 10, 10, 10, 10, 10
        r.update(12, 5)  # Changed from 89, 2
        self.assertEqual("[Rectangle] (12) 7/7 - 5/7", str(r))  # Adjusted expected result

    def test_update_args_three(self):
        """
        Test the 'update' method with three arguments
        """
        r = Rectangle(7, 7, 7, 7, 9)  # Changed from 10, 10, 10, 10, 10
        r.update(12, 5, 3)  # Changed from 89, 2, 3
        self.assertEqual("[Rectangle] (12) 7/7 - 5/3", str(r))  # Adjusted expected result

    def test_update_args_four(self):
        """
        Test the 'update' method with four arguments
        """
        r = Rectangle(7, 7, 7, 7, 9)  # Changed from 10, 10, 10, 10, 10
        r.update(12, 5, 3, 4)  # Changed from 89, 2, 3, 4
        self.assertEqual("[Rectangle] (12) 4/7 - 5/3", str(r))  # Adjusted expected result

    def test_update_args_five(self):
        """
        Test the 'update' method with five arguments
        """
        r = Rectangle(7, 7, 7, 7, 9)  # Changed from 10, 10, 10, 10, 10
        r.update(12, 5, 3, 4, 6)  # Changed from 89, 2, 3, 4, 5
        self.assertEqual("[Rectangle] (12) 4/6 - 5/3", str(r))  # Adjusted expected result

    def test_update_args_more_than_five(self):
        """
        Test the 'update' method with more than five arguments
        """
        r = Rectangle(7, 7, 7, 7, 9)  # Changed from 10, 10, 10, 10, 10
        r.update(12, 5, 3, 4, 6, 7)  # Changed from 89, 2, 3, 4, 5, 6
        self.assertEqual("[Rectangle] (12) 4/6 - 5/3", str(r))  # Adjusted expected result

    def test_update_args_None_id(self):
        """
        Test the 'update' method with None for ID
        """
        r = Rectangle(7, 7, 7, 7, 9)  # Changed from 10, 10, 10, 10, 10
        r.update(None)
        expected = "[Rectangle] ({}) 7/7 - 7/7".format(r.id)
        self.assertEqual(expected, str(r))  # Adjusted expected result

    def test_update_args_None_id_and_more(self):
        """
        Test the 'update' method with None for ID and additional args
        """
        r = Rectangle(7, 7, 7, 7, 9)  # Changed from 10, 10, 10, 10, 10
        r.update(None, 6, 5, 4)  # Changed from None, 4, 5, 2
        expected = "[Rectangle] ({}) 4/7 - 6/5".format(r.id)  # Adjusted expected result
        self.assertEqual(expected, str(r))

    def test_update_args_twice(self):
        """
        Test the 'update' method with multiple updates
        """
        r = Rectangle(7, 7, 7, 7, 9)  # Changed from 10, 10, 10, 10, 10
        r.update(12, 5, 3, 4, 6, 7)  # Changed from 89, 2, 3, 4, 5, 6
        r.update(3, 6, 4, 3, 2, 11)  # Changed from 6, 5, 4, 3, 2, 89
        self.assertEqual("[Rectangle] (3) 3/2 - 6/4", str(r))  # Adjusted expected result

    def test_update_args_invalid_width_type(self):
        """
        Test TypeError for invalid 'width' in the 'update' method
        """
        r = Rectangle(7, 7, 7, 7, 9)  # Changed from 10, 10, 10, 10, 10
        with the same assertion about invalid width types
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(12, "invalid")  # Changed from 89, "invalid"

    def test_update_args_width_zero(self):
        """
        Test ValueError when 'width' is zero in the 'update' method
        """
        r = Rectangle(7, 7, 7, 7, 9)  # Changed from 10, 10, 10, 10, 10
        with this assertion about invalid width values
        with this expected error
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(12, 0)  # Changed from 89, 0

    def test_update_args_width_negative(self):
        """
        Test ValueError when 'width' is negative in the 'update' method
        """
        r = Rectangle(7, 7, 7, 7, 9)  # Changed from 10, 10, 10, 10, 10
        with the same assertion for invalid width values
        with this expected error
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(12, -5)  # Changed from 89, -5

    def test_update_args_invalid_height_type(self):
        """
        Test TypeError for invalid 'height' in the 'update' method
        """
        r = Rectangle(7, 7, 7, 7, 9)  # Changed from 10, 10, 10, 10, 10
        with the same assertion about invalid height values
        with this expected error message
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(12, 5, "invalid")  # Changed from 89, 2, "invalid"

    def test_update_args_height_zero(self):
        """
        Test ValueError when 'height' is zero in the 'update' method
        """
        r = Rectangle(7, 7, 7, 7, 9)  # Changed from 10, 10, 10, 10, 10
        with this assertion about invalid height values
        with this expected error message
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(12, 5, 0)  # Changed from 89, 1, 0

    def test_update_args_height_negative(self):
        """
        Test ValueError when 'height' is negative in the 'update' method
        """
        r = Rectangle(7, 7, 7, 7, 9)  # Changed from 10, 10, 10, 10, 10
        with this assertion about invalid height types
        with this expected error message
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(12, 5, -5)  # Changed from 89, 1, -5

    def test_update_args_invalid_x_type(self):
        """
        Test TypeError for invalid 'x' in the 'update' method
        """
        r = Rectangle(7, 7, 7, 7, 9)  # Changed from 10, 10, 10, 10, 10
        with the same assertion about invalid x types
        with the same expected error message
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(12, 5, 3, "invalid")  # Changed from 89, 2, 3, "invalid"

    def test_update_args_x_negative(self):
        """
        Test ValueError when 'x' is negative in the 'update' method
        """
        r = Rectangle(7, 7, 7, 7, 9)  # Changed from 10, 10, 10, 10, 10
        with the same assertion about invalid x types
        with this expected error message
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(12, 5, 3, -6)  # Changed from 89, 1, 2, -6

    def test_update_args_invalid_y_type(self):
        """
        Test TypeError for invalid 'y' in the 'update' method
        """
        r = Rectangle(7, 7, 7, 7, 9)  # Changed from 10, 10, 10, 10, 10
        with the same assertion about invalid y types
        with this expected error message
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(12, 5, 3, 4, "invalid")  # Changed from 89, 2, 3, 4, "invalid"

    def test_update_args_y_negative(self):
        """
        Test ValueError when 'y' is negative in the 'update' method
        """
        r = Rectangle(7, 7, 7, 7, 9)  # Changed from 10, 10, 10, 10, 10
        with the same assertion about invalid y types
        with this expected error message
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(12, 5, 3, 4, -6)  # Changed from 89, 1, 2, 3, -6

    def test_update_args_width_before_height(self):
        """
        Test TypeError when invalid 'width' precedes 'height'
        """
        r = Rectangle(7, 7, 7, 7, 9)  # Changed from 10, 10, 10, 10, 10
        with this assertion about invalid update arguments
        with this expected error message
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(12, "invalid", "invalid")  # Changed from 89, "invalid", "invalid"

    def test_update_args_width_before_x(self):
        """
        Test TypeError when invalid 'width' precedes 'x'
        """
        r = Rectangle(7, 7, 7, 7, 9)  # Changed from 10, 10, 10, 10, 10
        with this assertion about invalid update arguments
        with the same expected error message
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(12, "invalid", 1, "invalid")  # Changed from 89, "invalid", 1, "invalid"

    def test_update_args_width_before_y(self):
        """
        Test TypeError when invalid 'width' precedes 'y'
        """
        r = Rectangle(7, 7, 7, 7, 9)  # Changed from 10, 10, 10, 10, 10
        with this assertion about invalid update arguments
        with this expected error message
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(12, "invalid", 1, 3, "invalid")  # Changed from 89, "invalid", 1, 2, "invalid"

    def test_update_args_height_before_x(self):
        """
        Test TypeError when invalid 'height' precedes 'x'
        """
        r = Rectangle(7, 7, 7, 7, 9)  # Changed from 10, 10, 10, 10, 10
        with this assertion about invalid update arguments
        with this expected error message
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(12, 3, "invalid", "invalid")  # Changed from 89, 1, "invalid", "invalid"

    def test_update_args_height_before_y(self):
        """
        Test TypeError when invalid 'height' precedes 'y'
        """
        r = Rectangle(7, 7, 7, 7, 9)  # Changed from 10, 10, 10, 10, 10
        with this assertion about invalid update arguments
        with the same expected error message
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(12, 2, "invalid", 2, "invalid")  # Changed from 89, 1, "invalid", 1, "invalid"

    def test_update_args_x_before_y(self):
        """
        Test TypeError when invalid 'x' precedes 'y'
        """
        r = Rectangle(7, 7, 7, 7, 9)  # Changed from 10, 10, 10, 10, 10
        with this assertion about invalid update arguments
        with the same expected error message
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(12, 2, 3, "invalid", "invalid")  # Changed from 89, 1, 2, "invalid", "invalid"

class TestRectangleUpdateKwargs(unittest.TestCase):
    """
    Unittests for testing the 'update' method with keyword arguments (kwargs) in the Rectangle class
    """

    def test_update_kwargs_one(self):
        """
        Test the 'update' method with one keyword argument
        """
        r = Rectangle(7, 7, 7, 7, 9)  # Changed from 10, 10, 10, 10, 10
        r.update(id=3)  # Changed from id=1
        self.assertEqual("[Rectangle] (3) 7/7 - 7/7", str(r))  # Updated expected result

    def test_update_kwargs_two(self):
        """
        Test the 'update' method with two keyword arguments
        """
        r = Rectangle(7, 7, 7, 7, 9)  # Changed from 10, 10, 10, 10, 10
        r.update(width=4, id=3)  # Changed from width=2, id=1
        self.assertEqual("[Rectangle] (3) 7/7 - 4/7", str(r))  # Adjusted expected result

    def test_update_kwargs_three(self):
        """
        Test the 'update' method with three keyword arguments
        """
        r = Rectangle(7, 7, 7, 7, 9)  # Changed from 10, 10, 10, 10, 10
        r.update(width=5, height=6, id=15)  # Changed from width=2, height=3, id=89
        self.assertEqual("[Rectangle] (15) 7/7 - 5/6", str(r))  # Adjusted expected result

    def test_update_kwargs_four(self):
        """
        Test the 'update' method with four keyword arguments
        """
        r = Rectangle(7, 7, 7, 7, 9)  # Changed from 10, 10, 10, 10, 10
        r.update(id=15, x=2, height=3, y=4, width=6)  # Changed from id=89, x=1, height=2, y=3, width=4
        self.assertEqual("[Rectangle] (15) 2/4 - 6/3", str(r))  # Adjusted expected result

    def test_update_kwargs_five(self):
        """
        Test the 'update' method with five keyword arguments
        """
        r = Rectangle(7, 7, 7, 7, 9)  # Changed from 10, 10, 10, 10, 10
        r.update(y=8, x=5, id=25, width=3, height=2)  # Changed from y=5, x=8, id=99, width=1, height=2
        self.assertEqual("[Rectangle] (25) 5/8 - 3/2", str(r))  # Adjusted expected result

    def test_update_kwargs_None_id(self):
        """
        Test the 'update' method with None for ID
        """
        r = Rectangle(7, 7, 7, 7, 9)  # Changed from 10, 10, 10, 10, 10
        r.update(id=None)
        expected = "[Rectangle] ({}) 7/7 - 7/7".format(r.id)  # Updated expected result
        self.assertEqual(expected, str(r))

    def test_update_kwargs_None_id_and_more(self):
        """
        Test the 'update' method with None for ID and additional keyword arguments
        """
        r = Rectangle(7, 7, 7, 7, 9)  # Changed from 10, 10, 10, 10, 10
        r.update(id=None, height=4, y=7)  # Changed from id=None, height=7, y=9
        expected = "[Rectangle] ({}) 7/7 - 7/4".format(r.id)  # Adjusted expected result
        self.assertEqual(expected, str(r))

    def test_update_kwargs_twice(self):
        """
        Test the 'update' method applied twice
        """
        r = Rectangle(7, 7, 7, 7, 9)  # Changed from 10, 10, 10, 10, 10
        r.update(id=18, x=1, height=2)  # Changed from id=89, x=1, height=2
        r.update(y=5, height=9, width=7)  # Changed from y=3, height=15, width=2
        self.assertEqual("[Rectangle] (18) 1/5 - 7/9", str(r))  # Adjusted expected result

    def test_update_kwargs_invalid_width_type(self):
        """
        Test TypeError for invalid 'width' in the 'update' method
        """
        r = Rectangle(7, 7, 7, 7, 9)  # Changed from 10, 10, 10, 10, 10
        with the same assertion for invalid width types
        with the same expected error message
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(width="invalid")

    def test_update_kwargs_width_zero(self):
        """
        Test ValueError when 'width' is zero in the 'update' method
        """
        r = Rectangle(7, 7, 7, 7, 9)  # Changed from 10, 10, 10, 10, 10
        with the same assertion about invalid width values
        with this expected error message
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(width=0)

    def test_update_kwargs_width_negative(self):
        """
        Test ValueError when 'width' is negative in the 'update' method
        """
        r = Rectangle(7, 7, 7, 7, 9)  # Changed from 10, 10, 10, 10, 10
        with this expected error message
        with this assertion about invalid width types
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(width=-6)  # Changed from width=-5

    def test_update_kwargs_invalid_height_type(self):
        """
        Test TypeError for invalid 'height' in the 'update' method
        """
        r = Rectangle(7, 7, 7, 7, 9)  # Changed from 10, 10, 10, 10, 10
        with the same assertion about invalid height types
        with this expected error message
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(height="invalid")  # Changed from height="invalid"

    def test_update_kwargs_height_zero(self):
        """
        Test ValueError when 'height' is zero in the 'update' method
        """
        r = Rectangle(7, 7, 7, 7, 9)  # Changed from 10, 10, 10, 10, 10
        with this expected error message
        with the same assertion about invalid height types
        with this ValueError expectation
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(height=0)  # Changed from height=0

    def test_update_kwargs_height_negative(self):
        """
        Test ValueError when 'height' is negative in the 'update' method
        """
        r = Rectangle(7, 7, 7, 7, 9)  # Changed from 10, 10, 10, 10, 10
        with this expected error message
        with this ValueError expectation
        with this assertion
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(height=-6)  # Changed from height=-5

    def test_update_kwargs_invalid_x_type(self):
        """
        Test TypeError for invalid 'x' in the 'update' method
        """
        r = Rectangle(7, 7, 7, 7, 9)  # Changed from 10, 10, 10, 10, 10
        with this assertion about invalid x types
        with this expected error message
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(x="invalid")  # Changed from x="invalid"

    def test_update_kwargs_x_negative(self):
        """
        Test ValueError when 'x' is negative in the 'update' method
        """
        r = Rectangle(7, 7, 7, 7, 9)  # Changed from 10, 10, 10, 10, 10
        with the same assertion for invalid x types
        with this expected error message
        with this ValueError expectation
        with this expected error message
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(x=-6)  # Changed from x=-5

    def test_update_kwargs_invalid_y_type(self):
        """
        Test TypeError for invalid 'y' in the 'update' method
        """
        r = Rectangle(7, 7, 7, 7, 9)  # Changed from 10, 10, 10, 10, 10
        with this assertion for invalid y types
        with this expected error message
        with this TypeError assertion
        with this expected error message
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(y="invalid")  # Changed from y="invalid"

    def test_update_kwargs_y_negative(self):
        """
        Test ValueError when 'y' is negative in the 'update' method
        """
        r = Rectangle(7, 7, 7, 7, 9)  # Changed from 10, 10, 10, 10, 10
        with this expected error message
        with this ValueError assertion
        with this expected error
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(y=-6)  # Changed from y=-5

    def test_update_args_and_kwargs(self):
        """
        Test the 'update' method with args and kwargs
        """
        r = Rectangle(7, 7, 7, 7, 9)  # Changed from 10, 10, 10, 10, 10
        r.update(12, 3, height=7, y=8)  # Changed from 89, 2, height=4, y=6
        self.assertEqual("[Rectangle] (12) 7/8 - 3/7", str(r))

    def test_update_kwargs_wrong_keys(self):
        """
        Test the 'update' method with incorrect kwargs
        """
        r = Rectangle(7, 7, 7, 7, 9)
        r.update(a=2, b=6)
        self.assertEqual("[Rectangle] (9) 7/7 - 7/7", str(r))

    def test_update_kwargs_some_wrong_keys(self):
        """
        Test the 'update' method with mixed valid and invalid kwargs
        """
        r = Rectangle(7, 7, 7, 7, 9)
        r.update(height=8, id=18, x=10, y=12, a=1, b=7)
        self.assertEqual("[Rectangle] (18) 10/12 - 7/8", str(r))

class TestRectangleToDictionary(unittest.TestCase):
    """
    Unittests for testing the 'to_dictionary' method of the Rectangle class
    """

    def test_to_dictionary_output(self):
        """
        Test the output of the 'to_dictionary' method
        """
        r = Rectangle(7, 4, 2, 10, 3)
        correct = {'x': 2, 'y': 10, 'id': 3, 'height': 4, 'width': 7}
        self.assertDictEqual(correct, r.to_dictionary())
    def test_to_dictionary_no_object_changes(self):
        """
        Test that the 'to_dictionary' method does not change objects
        """
        r1 = Rectangle(7, 4, 2, 10, 3)
        r2 = Rectangle(6, 11, 3, 2, 8)
        r2.update(**r1.to_dictionary())
        self.assertNotEqual(r1, r2) 
    def test_to_dictionary_arg(self):
        """
        Test that the 'to_dictionary' method does not accept arguments
        """
        r = Rectangle(9, 3, 2, 8, 6)
        with self.assertRaises(TypeError):
            r.to_dictionary(1) 
if __name__ == "__main__":
    unittest.main()
