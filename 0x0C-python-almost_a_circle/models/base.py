#!/usr/bin/python3
"""Class Base module that contains the base of all other classes
in the project"""

import turtle
import json
import csv

class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Convert a list of dictionaries to a JSON string
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write a list of objects to a JSON file
        """
        filename = cls.__name__ + ".json"
        if list_objs is None:
            with open(filename, 'w') as f:
                f.write("[]")
        else:
            list_dictionaries = [obj.to_dictionary() for obj in list_objs]
            json_string = cls.to_json_string(list_dictionaries)
            with open(filename, 'w') as f:
                f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
        Convert a JSON string to a list of dictionaries
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Create an object from a dictionary
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Load a list of objects from a JSON file
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as f:
                json_string = f.read()
            list_dictionaries = Base.from_json_string(json_string)
            return [cls.create(**d) for d in list_dictionaries]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            if cls.__name__ == "Rectangle":
                writer.writerow(["id", "width", "height", "x", "y"])
                for obj in list_objs:
                    writer.writerow([obj.id, obj.width, obj.height, obj.x, obj.y])
            elif cls.__name__ == "Square":
                writer.writerow(["id", "size", "x", "y"])
                for obj in list_objs:
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])
        return filename

@classmethod
def load_from_file_csv(cls):
    """
    Loads a list of objects from a CSV file
    """
    filename = cls.__name__ + ".csv"
    try:
        with open(filename, "r", newline="") as csvfile:
            if cls.__name__ == "Rectangle":
                fieldnames = ["id", "width", "height", "x", "y"]
            else:
                fieldnames = ["id", "size", "x", "y"]
            list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
            list_dicts = [dict([k, int(v)] for k, v in d.items())
                          for d in list_dicts]
            return [cls.create(**d) for d in list_dicts]
    except IOError:
        return []

@staticmethod
def draw(list_rectangles, list_squares):
    """Draws all the Rectangles and Squares using Turtle graphics"""
    turtle.speed(0)
    for obj in list_rectangles + list_squares:
        turtle.penup()
        turtle.goto(obj.x, obj.y)
        turtle.pendown()
        for i in range(2):
            turtle.forward(obj.width if hasattr(obj, "width") else obj.size)
            turtle.left(90)
            turtle.forward(obj.height if hasattr(obj, "height") else obj.size)
            turtle.left(90)
turtle.exitonclick()