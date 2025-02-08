BOOKS_DATABASE = [
    {"id": 1, "name": "test_name_1", "pages": 200},
    {"id": 2, "name": "test_name_2", "pages": 400},
]

class Book:
    def __init__(self, id_, name, pages):
        self.id_ = id_
        self.name = name
        self.pages = pages

    def __repr__(self) -> str:
        return f"Book(id_={self.id_}, name='{self.name}', pages={self.pages})"

class Library:
    def __init__(self, books=None):
        self.books = books if books else []  # Храним список книг

    def get_next_book_id(self):
        return max((book.id_ for book in self.books), default=0) + 1  # Следующий ID

    def get_index_by_book_id(self, book_id):
        for i, book in enumerate(self.books):
            if book.id_ == book_id:
                return i
        raise ValueError("Книги с запрашиваемым id не существует")

if __name__ == '__main__':
    empty_library = Library()
    print(empty_library.get_next_book_id())  # 1

    list_books = [Book(id_=book["id"], name=book["name"], pages=book["pages"]) for book in BOOKS_DATABASE]
    library_with_books = Library(books=list_books)

    print(library_with_books.get_next_book_id())  # 3
    print(library_with_books.get_index_by_book_id(1))  # 0
