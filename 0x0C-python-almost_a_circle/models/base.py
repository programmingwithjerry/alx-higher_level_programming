#!/usr/bin/python3
"""This module contains a class which will be the
   “base” of all other classes in this project.
"""


import csv
import json
import os
import turtle


class Base:
    """Serve as base for all classes in this project"""
    __nb_objects = 0

    """class constructor: def __init__(self, id=None)"""
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        if not isinstance(list_dictionaries, list) or not
                         all(isinstance(i, dict) for i in list_dictionaries):
            raise TypeError("list_dictionaries must be a list of dictionaries")
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        file_name = cls.__name__ + ".json"
        with open(file_name, "w") as json_file:
            if list_objs is None:
                json_file.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                json_file.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation - json_string"""
        json_string_list = []

        if json_string is not None and json_string != '':
            if not isinstance(json_string, str):
                raise TypeError("json_string must be a string")
            json_string_list = json.loads(json_string)

        return json_string_list

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)  # Create a dummy Rectangle instance
        elif cls.__name__ == "Square":
            dummy = cls(1)  # Create a dummy Square instance
        else:
            raise ValueError("Unsupported class type")

        dummy.update(**dictionary)
        return dummy

    def load_from_file(cls):
        """Returns a list of instances"""

        file_name = cls.__name__ + ".json"
        instances_list = []
        dictionaries_list = []

        if os.path.exists(file_name):
            with open(file_name, 'r') as file:
                json_string = file.read()
                dictionaries_list = cls.from_json_string(json_string)
                for dictionary in dictionaries_list:
                    instances_list.append(cls.create(**dictionary))
        return instances_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes list_objs and writes to file"""

        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csv_file:
            if list_objs is None or list_objs == []:
                csv_file.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    field_names = ["id", "width", "height", "x", "y"]
                else:
                    field_names = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csv_file, field_names=field_names)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes CSV format from a file"""

        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csv_file:
                if cls.__name__ == "Rectangle":
                    field_names = ["id", "width", "height", "x", "y"]
                else:
                    field_names = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csv_file, field_names=field_names)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#ee3cae")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#e1abcd")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for _ in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#c95da1")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for _ in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()

