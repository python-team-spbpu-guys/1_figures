# Класс Прямоугольник
class Rectangle:
    def __init__(self, width: float, height: float):
        self._width = width
        self._height = height

    @property
    def width(self) -> float:
        return self._width

    @width.setter
    def width(self, width: float):
        self._width = width

    @property
    def height(self) -> float:
        return self._height

    @height.setter
    def height(self, height: float):
        self._height = height

    def area(self) -> float:
        return self.width * self.height