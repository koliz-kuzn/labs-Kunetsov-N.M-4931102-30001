import doctest


class People:
    """
    Класс описывает модель человека.
    """
    def __init__(self, height: float = 0.0, weight: float = 0.0):
        """
        Создание объекта класса "People".
        :param height: рост человека (float)
        :param weight: вес человека (float)

        Примеры:
        >>> person = People(1.75, 70.5)
        """
        self.add_data(height, weight)

    def add_data(self, height: float = 0.0, weight: float = 0.0) -> None:
        """Добавление данных о человеке."""
        if height <= 0:
            raise ValueError("Рост должен быть положительным числом")
        if weight <= 0:
            raise ValueError("Вес должен быть положительным числом")
        self.height = height
        self.weight = weight

    def print_data(self) -> None:
        """Вывод данных о человеке."""
        print(self.height, self.weight)


class Milk:
    """
    Класс описывает модель молока.
    """
    def __init__(self, volume: float = 0.0, drunk: float = 0.0, bottle: float = 0.0):
        """
        Создание объекта класса "Milk".
        :param volume: объем молока (float)
        :param drunk: объем выпитого молока (float)
        :param bottle: объем бутылки (float)

        Примеры:
        >>> milk1 = Milk(1.0, 0.5, 1.5)
        """
        self.add_data(volume, drunk, bottle)

    def add_data(self, volume: float = 0.0, drunk: float = 0.0, bottle: float = 0.0) -> None:
        """Добавление данных о молоке."""
        if bottle <= 0:
            raise ValueError("Объем бутылки должен быть положительным числом")
        if volume < 0 or volume > bottle:
            raise ValueError("Объем молока должен быть от 0 до объема бутылки")
        if drunk < 0:
            raise ValueError("Объем выпитого молока должен быть положительным числом")
        self.volume = volume
        self.drunk = drunk
        self.bottle = bottle

    def print_data(self) -> None:
        """Вывод данных о молоке."""
        print(self.volume, self.drunk, self.bottle)


class Ambar:
    """
    Класс описывает модель амбара.
    """
    def __init__(self, fruits: int = 0, vegetables: int = 0):
        """
        Создание объекта класса "Ambar".
        :param fruits: количество фруктов (int)
        :param vegetables: количество овощей (int)

        Примеры:
        >>> storage = Ambar(100, 50)
        """
        self.add_data(fruits, vegetables)

    def add_data(self, fruits: int = 0, vegetables: int = 0) -> None:
        """Добавление данных об амбаре."""
        if fruits < 0:
            raise ValueError("Количество фруктов не может быть отрицательным")
        if vegetables < 0:
            raise ValueError("Количество овощей не может быть отрицательным")
        self.fruits = fruits
        self.vegetables = vegetables

    def print_data(self) -> None:
        """Вывод данных об амбаре."""
        print(self.fruits, self.vegetables)


if __name__ == "__main__":
    # Проверка работоспособности через doctest
    doctest.testmod()
