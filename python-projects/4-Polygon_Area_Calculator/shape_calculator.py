class Rectangle:
    def __init__(self, width: int, height: int):
        self._width = width
        self._height = height

    def __str__(self):
        return f"Rectangle(width={self._width}, height={self._height})"
    
    @property
    def width(self):
        return self._width

    @width.setter
    def set_width(self, value_width):
        self._width = value_width

    @property
    def height(self):
        return self._height

    @height.setter
    def set_height(self, value_height):
        self._height = value_height

    def get_area(self):
        area = self._width * self._height
        return area
    
    def get_perimeter(self):
        perimeter = (2 * self._width) + (2 * self._height)
        return perimeter

    def get_diagonal(self):
        diagonal = ((self._width ** 2) + (self._height ** 2) ** 0.5)
        return diagonal

    def get_picture(self):
        if (self._width > 50 or self._height > 50):
            return "Too big for picture"
        else:
            picture = (("*" * self._width) + "\n") * self._height
            return picture

    def get_amount_inside(self, shape):
        return int(self.get_area() / shape.get_area())
        

rec = Rectangle(2, 5)
rect = Rectangle(5,10)
print(rect)
print(rect.get_area())
print(rect.get_perimeter())
print(rect.get_diagonal())
print(rect.get_picture())
print(rect.get_amount_inside(rec))