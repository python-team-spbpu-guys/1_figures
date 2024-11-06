from Rectangle import Rectangle

# Класс Квадрат, сохраняющий наследование и принцип LSP
class Square(Rectangle):
    def __init__(self, side: float):
        super().__init__(side, side)

    @property
    def width(self) -> float:
        return self._width

    @width.setter
    def width(self, side: float):
        # Для квадрата, ширина и высота должны быть одинаковыми
        self._width = self._height = side

    @property
    def height(self) -> float:
        return self._height

    @height.setter
    def height(self, side: float):
        # Для квадрата, ширина и высота должны быть одинаковыми
        self._width = self._height = side
