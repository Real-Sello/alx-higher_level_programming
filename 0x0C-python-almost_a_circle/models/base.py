#!/usr/bin/python3
"""
Module containing the Base class
"""

import json
import csv
import turtle


class Base:
    """
    'Base' class
    This class is the 'base' of all other classes in this project
    The goal is to manage 'id' attribute in all future classes
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        init method of class 'Base'
        Arguments:
            id: default value set to None
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        static method that returns
            JSON representation of 'list_dictionaries'
        Arguments:
            list_dictionaries: a list of dictionaries

        Returns: [], if list_dictionaries is None or empty
                else, JSON string representation of 'list_dictionaries'
        """
        if (len(list_dictionaries) == 0) or (list_dictionaries is None):
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
        static method that returns
            a list of the JSON string representation json_string
        Arguments:
            json_string
        """
        if json_string is None or (len(json_string) == 0):
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        class method that writes the
            JSON string representation of 'list_objs to a file
        Arguments:
            list_objs: list of instances who inherits of Base class
        """
        lst_val = []
        with open(cls.__name__ + ".json", "w", encoding="utf-8") as file:
            if list_objs is not None:
                for i in list_objs:
                    lst_val.append(i.to_dictionary())
            file.write(cls.to_json_string(lst_val))

    @classmethod
    def create(cls, **dictionary):
        """
        class method that returns:
            an instamce of all attributes already set
        Arguments:
            dictionary: a list of key-worded arguments
                      : can be thought of as a double puinter to a dictionary
        """
        if cls.__name__ == "Rectangle":
            inst = cls(3, 5)
        elif cls.__name__ == "Square":
            inst = cls(4)

        inst.update(**dictionary)
        return inst

    @classmethod
    def load_from_file(cls):
        """
        class method that returns:
            a istt of instances
        """
        lst = []
        try:
            with open(cls.__name__ + ".json", "r", encoding="utf-8") as file:
                x = cls.from_json_string(file.read())

            for i in x:
                lst.append(cls.create(**i))
            return lst
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        class method that serializes in CSV
        Arguments:
            list_objs: list of inherited instances of class Base
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        class method that deserializes in CSV
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
        """
        Draw rectangles and squares
        'turtle' module imported
        Arguments:
            list_rectangles: list of rectangles
            list_squares: list of squares
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()