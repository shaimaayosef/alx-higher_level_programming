#!/usr/bin/python3
import json

class Base:
    """
    Base class for managing id attribute in future classes.
    """

    # private class attribute
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Class constructor.

        Args:
            id (int, optional): The id for the instance. Defaults to None.
        """
        if id is not None:
            # Assign the public instance attribute id with the provided argument value
            self.id = id
        else:
            # Increment __nb_objects and assign the new value to the public instance attribute id
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Convert a list of dictionaries to a JSON string.

        Args:
            list_dictionaries (list): List of dictionaries.

        Returns:
            str: JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): List of instances that inherit from Base.

        Returns:
            None
        """
        filename = cls.__name__ + ".json"
        with open(filename, mode='w') as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dict = [obj.to_dictionary() for obj in list_objs]
                json_string = cls.to_json_string(list_dict)
                file.write(json_string)
      
    @staticmethod
    def from_json_string(json_string):
        """
        Convert a JSON-formatted string to a list of dictionaries.

        Args:
            json_string (str): JSON-formatted string.

        Returns:
            list: List of dictionaries represented by json_string.
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Create an instance with all attributes set based on the provided dictionary.

        Args:
            **dictionary: Dictionary containing attributes and their values.

        Returns:
            instance: Instance of the class with attributes set.
        """
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        else:
            dummy_instance = cls()

        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """
        Load instances from a JSON file and return a list of instances.

        Returns:
            list: List of instances loaded from the JSON file.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode='r') as file:
                json_string = file.read()
                list_dict = cls.from_json_string(json_string)
                return [cls.create(**d) for d in list_dict]
        except FileNotFoundError:
            return []
