#!/usr/bin/python3

import json

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
        if not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
      list_dict = [i.to_dictionary() for i in list_objs] if list_objs else []

      list_json = cls.to_json_string(list_dict)

      with open(cls.__name__ + ".json", "w") as f:
          f.write(list_json)

    @staticmethod
    def from_json_string(json_string):
        if not json_string:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = None

        if dummy is not None:
            dummy.update(**dictionary)
        
        return dummy

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as f:
                json_str = f.read()
                list_dict = cls.from_json_string(json_str)
                return [cls.create(**i) for i in list_dict]

        except FileNotFoundError:
            return []

