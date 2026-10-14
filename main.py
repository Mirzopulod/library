# Хранит: название, автор, год издания, статус (взята/не взята).
# Умеет: возвращать строковое представление.
class Book:
    def __init__(self, name, author, year):
        self.__name = name
        self.__author = author
        self.__year = year
        self.__status = False

    def change_status(self):
        self.__status = not self.__status

    def get_name(self):
        return self.__name
    def get_author(self):
        return self.__author
    def get_year(self):
        return self.__year
    def get_status(self):
        return self.__status

    def get_status_text(self):
        return  'занята' if self.__status  else 'свободна'

    def get_all(self):
        return f"Название: {self.__name}, Автор: {self.__author}, Год издания: {self.__year}, Статус: {self.get_status_text()}"


# Наследуется от Book.
# Дополнительно хранит: размер файла.
class EBook(Book):
    def __init__(self, name, author, year, size):
        super().__init__(name, author, year)
        self.__size = size

    def get_all(self):
        base = super().get_all()
        return f"{base}, Размер: {self.__size} стр"


# Хранит: имя, список взятых книг.
# Умеет: брать книгу, возвращать книгу.
class Reader:
    def __init__(self, name, books):
        self.__name = name
        self.__books = []
        
        if isinstance(books, list):
            self.__books = books
        else:
            self.__books.append(books)

    def add_books(self, books):
        if isinstance(books, list):
            self.__books = books
        else:
            self.__books.append(books)

    def del_books(self, books):
        for i in range(len(books)):
            j = 0
            while j < len(self.__books):
                if books[i] == self.__books[j]:
                    self.__books.pop(j)
                    break
                j += 1


class Library:
    def __init__(self):
        pass


def main():
    Mr = EBook("Взлетай", "Гоголь", 2026, 567)
    Mr.change_status()
    print(Mr.get_all())

if __name__ == '__main__':
    main()