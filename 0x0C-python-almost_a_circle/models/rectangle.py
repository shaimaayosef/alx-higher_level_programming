#!/usr/bin/python3

from models.base import Base

class Rectangle(Base):
    """
    Rectangle class, inherits from Base.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Class constructor.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int, optional): x-coordinate of the rectangle. Defaults to 0.
            y (int, optional): y-coordinate of the rectangle. Defaults to 0.
            id (int, optional): The id for the instance. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width."""
        self._validate_integer(value, "width")
        self._validate_positive(value, "width")
        self.__width = value

    @property
    def height(self):
        """Getter for height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height."""
        self._validate_integer(value, "height")
        self._validate_positive(value, "height")
        self.__height = value

    @property
    def x(self):
        """Getter for x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x."""
        self._validate_integer(value, "x")
        self._validate_non_negative(value, "x")
        self.__x = value

    @property
    def y(self):
        """Getter for y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y."""
        self._validate_integer(value, "y")
        self._validate_non_negative(value, "y")
        self.__y = value

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.width * self.height

    def display(self):
        """Print the Rectangle instance using the character #."""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)
    
    def __str__(self):
        """Return a string representation of the Rectangle."""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def to_dictionary(self):
        """
        Return a dictionary representation of the Rectangle.

        Returns:
            dict: Dictionary containing id, width, height, x, and y.
        """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }

    def update(self, *args, **kwargs):
        """
        Update attributes with provided arguments.

        Args:
            *args: Variable number of positional arguments in the order (id, width, height, x, y).
            **kwargs: Variable number of keyword arguments representing attribute-value pairs.
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]

        for key, value in kwargs.items():
            setattr(self, key, value)

    def _validate_integer(self, value, attribute_name):
        """Validate that the value is an integer."""
        if not isinstance(value, int):
            raise TypeError(f"{attribute_name} must be an integer.")

    def _validate_positive(self, value, attribute_name):
        """Validate that the value is positive (> 0)."""
        if value <= 0:
            raise ValueError(f"{attribute_name} must be > 0.")

    def _validate_non_negative(self, value, attribute_name):
        """Validate that the value is non-negative (>= 0)."""
        if value < 0:
            raise ValueError(f"{attribute_name} must be >= 0.")
