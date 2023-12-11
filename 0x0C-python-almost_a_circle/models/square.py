#!/usr/bin/python3

from models.rectangle import Rectangle

class Square(Rectangle):
    """
    Square class, inherits from Rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Class constructor.

        Args:
            size (int): Size of the square.
            x (int, optional): x-coordinate of the square. Defaults to 0.
            y (int, optional): y-coordinate of the square. Defaults to 0.
            id (int, optional): The id for the instance. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size."""
        return self.width  # Since size is both width and height

    @size.setter
    def size(self, value):
        """Setter for size."""
        self._validate_integer(value, "width")
        self._validate_positive(value, "width")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update attributes with provided arguments.

        Args:
            *args: Variable number of positional arguments in the order (id, size, x, y).
            **kwargs: Variable number of keyword arguments representing attribute-value pairs.
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]

        if kwargs and not args:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """Return a string representation of the Square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def to_dictionary(self):
        """
        Return a dictionary representation of the Square.

        Returns:
            dict: Dictionary containing id, size, x, and y.
        """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
