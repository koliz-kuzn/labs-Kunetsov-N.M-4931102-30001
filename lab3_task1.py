class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}" # метод может быть часстичго унаследован

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})" # метод может быть переружен

    @property
    def name_autor(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"



class PaperBook(Book):
    def __init__(self, _name: str, _author: str, pages: int):
        super().__init__(_name,_author)
        self.pages = pages

        if not isinstance(pages, int):
            raise TypeError("количество страниц должно быть целым числом")
        if pages <= 0:
            raise ValueError("количество страниц должно быть положительным числом")

        super().__str__(),f"Страниц {self.pages}"

    @property
    def name1_autor(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages = {self.pages})"


class AudioBook(Book):
    def __init__(self, _name: str, _author: str, duration: float):
        super().__init__(_name,_author)
        self.duration = duration

        if not isinstance(duration, float):
            raise TypeError("аудио должно быть вещественным числом")
        if duration <= 0:
            raise ValueError("аудио должно быть положительным числом")

        super().__str__(),f"Время {self.duration}"

    @property
    def name2_autor(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration = {self.duration})"

book = Book('Букварь','Пушкин')
book1 = PaperBook('Математика','автор',8)
book2 = AudioBook('золотая рыбка','Пушкин',9.6)
print(book.name_autor)
print(book1.name1_autor)
print(book2.name2_autor)

