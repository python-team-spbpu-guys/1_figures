from Rectangle import Rectangle
from Square import Square

if __name__ == "__main__":
    # Создаём объект Rectangle и Square
    rect = Rectangle(5, 10)
    square = Square(4)

    # Площадь прямоугольника и квадрата
    print("Rectangle area:", rect.area())  # Ожидается: 5 * 10 = 50
    print("Square area:", square.area())  # Ожидается: 4 * 4 = 16

    # Изменим ширину у квадрата
    square.width = 7

    print("Updated Square area:", square.area())  # Ожидается: 7 * 7 = 49
    print("Square width:", square.width)  # Ожидается: 7
    print("Square height:", square.height)  # Ожидается: 7
