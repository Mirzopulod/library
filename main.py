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
    def __init__(self, name, *books):
        
        self.__name = name
        self.__books = list(books)
        
    def __str__(self):
        if self.__books:
            books_str = ", ".join(self.__books) 
        else:
            books_str = "нет"
        return f"Имя: {self.__name}, Взятые книги: {books_str}"

    def add_books(self, books):
        if isinstance(books, list):
            self.__books.extend(books)
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


# Хранит: список всех книг, список всех читателей.
# Умеет: добавлять книгу, добавлять читателя, показывать все книги, показывать всех читателей.
class Library:
    def __init__(self):
        self.__books = []
        self.__readers = []


    def add_books(self, books):
        if isinstance(books, list):
            self.__books.extend(books)
        else:
            self.__books.append(books)

    def add_readers(self, readers):
        if isinstance(readers, list):
            self.__readers.extend(readers)
        else:
            self.__readers.append(readers)

    def show_books(self):
        print("Все книги:")
        for x in self.__books:
            print(x.get_all())

    def show_readers(self):
        print("Все читатели:")
        for x in self.__readers:
            print(x)




def main():
    lib = Library()

    # Создаём книги
    book1 = Book("Война и мир", "Толстой", 1869)
    book2 = Book("Преступление и наказание", "Достоевский", 1866)
    book3 = EBook("Python для всех", "Лутц", 2020, 15)

    # Создаём читателей
    reader1 = Reader("Tom")
    reader2 = Reader("Bob", "Война и мир", "Python для всех")

    # Добавляем в библиотеку
    lib.add_books(book1)
    lib.add_books(book2)
    lib.add_books(book3)

    lib.add_readers(reader1)
    lib.add_readers(reader2)

    # Показываем
    print("=== Книги ===")
    lib.show_books()

    print("\n=== Читатели ===")
    lib.show_readers()

if __name__ == '__main__':
    main()