import argparse
import logging

"""
Урок 11, задача 3 + Урок 13, задача 1.
Разработайте программу для работы с прямоугольниками. Необходимо создать класс Rectangle, который будет представлять
прямоугольник с заданными шириной и высотой.

Добавьте в задачу Rectangle, которую писали ранее, исключение NegativeValueError, которое выбрасывается при
некорректных значениях ширины и высоты, как при создании объекта, так и при установке их через сеттеры.
"""


class NegativeValueError(Exception):
    def __init__(self, message):
        super().__init__(message)


class Rectangle:
    """
    Класс, представляющий прямоугольник.
    Атрибуты:   - width (int): ширина прямоугольника
                - height (int): высота прямоугольника
    Методы: - perimeter(): вычисляет периметр прямоугольника
            - area(): вычисляет площадь прямоугольника
            - __add__(other): определяет операцию сложения двух прямоугольников
            - __sub__(other): определяет операцию вычитания одного прямоугольника из другого
            - __lt__(other): определяет операцию "меньше" для двух прямоугольников
            - __eq__(other): определяет операцию "равно" для двух прямоугольников
            - __le__(other): определяет операцию "меньше или равно" для двух прямоугольников
            - __str__(): возвращает строковое представление прямоугольника
            - __repr__(): возвращает строковое представление прямоугольника, которое может быть использовано для создания нового объекта
    """

    def __init__(self, width, height=None):
        try:
            if width <= 0:
                raise NegativeValueError(f'Ширина должна быть положительной, а не {width}')
            self._width = width
            if height is None:
                self._height = width
            else:
                if height <= 0:
                    raise NegativeValueError(f'Высота должна быть положительной, а не {height}')
                self._height = height
        except NegativeValueError as e:
            logger.info(f'Переданные данные прямоугольника: Ширина({width}), Высота({height}). '
                        f'Вызвано исключение: {e}')

    @property
    def width(self):
        """
        Значение ширины для прямоугольника
        Возвращает: - int: ширина прямоугольника
        """
        try:
            return self._width
        except AttributeError as e:
            logger.info(f'При возврате ширины вызвано исключение: {e}')

    @width.setter
    def width(self, value):
        """
        Устанавливает значение ширины для прямоугольника
        Аргументы: - value(int): новая ширина прямоугольника
        """
        try:
            if value > 0:
                self._width = value
            else:
                raise NegativeValueError(f'Ширина должна быть положительной, а не {value}')
        except NegativeValueError as e:
            logger.info(f'Переданные данные прямоугольника: Ширина({value}). '
                        f'Вызвано исключение: {e}')
            print('Вызвана ошибка: см. Log/lof_for_main_15_1.log')

    @property
    def height(self):
        """
        Значение высоты для прямоугольника
        Возвращает: - int: высота прямоугольника
        """
        try:
            return self._height
        except AttributeError as e:
            logger.info(f'При возврате высоты вызвано исключение: {e}')

    @height.setter
    def height(self, value):
        """
        Устанавливает значение высоты для прямоугольника
        Аргументы - value(int): новая высота прямоугольника
        """
        try:
            if value > 0:
                self._height = value
            else:
                raise NegativeValueError(f'Высота должна быть положительной, а не {value}')
        except NegativeValueError as e:
            logger.info(f'Переданные данные прямоугольника: Высота({value}). '
                        f'Вызвано исключение: {e}')

    def perimeter(self):
        """
        Вычисляет периметр прямоугольника.
        Возвращает: - int: периметр прямоугольника
        """
        try:
            return 2 * (self.width + self.height)
        except TypeError as e:
            logger.info(f'Невозможно вычислить периметр прямоугольника. Вызвано исключение: {e}')

    def area(self):
        """
        Вычисляет площадь прямоугольника.
        Возвращает: - int: площадь прямоугольника
        """
        try:
            return self.width * self.height
        except TypeError as e:
            logger.info(f'Невозможно вычислить площадь прямоугольника. Вызвано исключение: {e}')

    def __add__(self, other):
        """
        Определяет операцию сложения двух прямоугольников.
        Аргументы: - other (Rectangle): второй прямоугольник
        Возвращает: - Rectangle: новый прямоугольник, полученный путем сложения двух исходных прямоугольников
        """
        try:
            width = self.width + other.width
            perimeter = self.perimeter() + other.perimeter()
            height = perimeter / 2 - width
            return Rectangle(width, height)
        except TypeError as e:
            logger.info(f'Невозможно определить операцию сложения двух прямоугольников. Вызвано исключение: {e}. '
                        f'Был создан другой прямоугольник с Шириной и высотой: 1, 1!')
            print('\nБыл создан другой прямоугольник, так входные данные указаны неверно! Ширина и высота равны 1!')
            return Rectangle(1, 1)

    def __sub__(self, other):
        """
        Определяет операцию вычитания одного прямоугольника из другого.
        Аргументы: - other (Rectangle): вычитаемый прямоугольник
        Возвращает: - Rectangle: новый прямоугольник, полученный путем вычитания вычитаемого прямоугольника из исходного
        """
        try:
            if self.perimeter() < other.perimeter():
                self, other = other, self
            width = abs(self.width - other.width)
            perimeter = self.perimeter() - other.perimeter()
            height = perimeter / 2 - width
            return Rectangle(width, height)
        except TypeError as e:
            logger.info(f'Невозможно определить операцию вычитания двух прямоугольников. Вызвано исключение: {e}. '
                        f'Был создан другой прямоугольник с Шириной и высотой: 1, 1!')
            print('\nБыл создан другой прямоугольник, так входные данные указаны неверно! Ширина и высота равны 1!')
            return Rectangle(1, 1)

    def __lt__(self, other):
        """
        Определяет операцию "меньше" для двух прямоугольников.
        Аргументы: - other (Rectangle): второй прямоугольник
        Возвращает: - bool: True, если площадь первого прямоугольника меньше площади второго, иначе False
        """
        try:
            return self.area() < other.area()
        except TypeError as e:
            logger.info(f'Невозможно определить операцию "меньше" для двух прямоугольников. Вызвано исключение: {e}')
            return None

    def __eq__(self, other):
        """
        Определяет операцию "равно" для двух прямоугольников.
        Аргументы: - other (Rectangle): второй прямоугольник
        Возвращает: - bool: True, если площади равны, иначе False
        """
        try:
            return self.area() == other.area()
        except TypeError as e:
            logger.info(f'Невозможно определить операцию "равно" для двух прямоугольников. Вызвано исключение: {e}')
            return None

    def __le__(self, other):
        """
        Определяет операцию "меньше или равно" для двух прямоугольников.
        Аргументы: - other (Rectangle): второй прямоугольник
        Возвращает: - bool: True, если площадь первого прямоугольника меньше или равна площади второго, иначе False
        """
        try:
            return self.area() <= other.area()
        except TypeError as e:
            logger.info(f'Невозможно определить операцию "меньше или равно" для двух прямоугольников. '
                        f'Вызвано исключение: {e}')
            return None

    def __str__(self):
        """
        Возвращает строковое представление прямоугольника.
        Возвращает: - str: строковое представление прямоугольника
        """
        return f"Прямоугольник со сторонами {self.width} и {self.height}"

    def __repr__(self):
        """
        Возвращает строковое представление прямоугольника, которое может быть использовано для создания нового объекта.
        Возвращает: - str: строковое представление прямоугольника
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        print('Программа завершилась! Для более подробного отчета см. Log/log_for_main15_1.log')


if __name__ == "__main__":
    logging.basicConfig(filename='Log/log_for_main15_1.log',
                        filemode='w',
                        format='{levelname} - {asctime} функция "{funcName}()" строка {lineno} :\n{msg}\n',
                        encoding='utf-8',
                        style='{',
                        level=logging.INFO)
    logger = logging.getLogger(__name__)

    # Вариант запуска через консоль
    parser = argparse.ArgumentParser(description='Принимаем размеры прямоугольника')
    parser.add_argument('-rect1W', type=int, default=1)
    parser.add_argument('-rect1H', type=int, default=None)
    parser.add_argument('-perimeter', type=bool, default=False)
    parser.add_argument('-area', type=bool, default=False)
    try:
        args = parser.parse_args()
        rect1 = Rectangle(int(args.rect1W))
        if args.rect1H is not None:
            rect1.height = int(args.rect1H)
        if bool(args.perimeter):
            print(f'Периметр: {rect1.perimeter()}')
        if bool(args.area):
            print(f'Площадь: {rect1.area()}')
    except Exception as e:
        logger.info(f'При транспонировании матрицы было вызвано исключение: {e}')
        print("Вероятно, не все аргументы были указаны! ")
    # Запуски командной строкой:
    # python main15_1.py -rect1W=5 -rect1H=-7
    # python main15_1.py -rect1W=5 -rect1H=10 -perimeter=True -area=True
    # python main15_1.py -rect1W=5 -rect1H=10 -perimeter=True

    # Второй вариант запуска через IDLE
    # rect1 = Rectangle(5, 10)
    # rect2 = Rectangle(-3, 7)
    # rect2.height = 5
    # print(f"Периметр rect1: {rect1.perimeter()}")
    # print(f"Площадь rect2: {rect2.area()}")
    # print(f"rect1 < rect2: {rect1 < rect2}")
    # print(f"rect1 == rect2: {rect1 == rect2}")
    # print(f"rect1 <= rect2: {rect1 <= rect2}")
    # rect3 = rect1 + rect2
    # print(f"Периметр rect3: {rect3.perimeter()}")
    # rect4 = rect1 - rect2
    # print(f"Ширина rect4: {rect4.width}")
