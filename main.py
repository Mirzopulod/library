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
# Умеет: возвращать строковое представление.
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

    def add_book(self, book):
        self.__books.append(book)

    def remove_book(self, book):
        if book in self.__books:
            self.__books.remove(book)

    def get_name(self):
        return self.__name
    def get_books(self):
        return self.__books


# Хранит: список всех книг, список всех читателей.
# Умеет: добавлять книгу, добавлять читателя, показывать все книги, показывать всех читателей.
# Умеет: Работать со списками книг и читателей
class Library:
    def __init__(self):
        self.__books = []
        self.__readers = []


    def add_books(self, *books):
        self.__books.extend(books)


    def add_readers(self, *readers):
            self.__readers.extend(readers)


    def take_book(self, reader, book):
        # проверка: книга свободна?
        if book.get_status():
            print("Книга занята")
            return
        reader.add_book(book.get_name())
        book.change_status()

    def return_book(self, reader, book):
        stbook = book.get_name()
        rtbook = reader.get_books()
        if stbook in rtbook:
            reader.remove_book(stbook)
            book.change_status()                
            print("Книга успешно возвращена!")
            return
        print("Книга не найдена в базе читателя!")
        return
        
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
    reader2 = Reader("Bob")

    # Добавляем в библиотеку
    lib.add_books(book1, book2, book3)
    lib.add_readers(reader1, reader2)

    print("=== Начальное состояние ===")
    lib.show_books()
    lib.show_readers()

    print("\n=== Tom берёт 'Война и мир' ===")
    lib.take_book(reader1, book1)
    lib.show_books()
    lib.show_readers()

    print("\n=== Tom пытается взять ту же книгу снова ===")
    lib.take_book(reader1, book1)   # должна быть ошибка
    lib.show_books()
    lib.show_readers()

    print("\n=== Tom возвращает 'Война и мир' ===")
    lib.return_book(reader1, book1)
    lib.show_books()
    lib.show_readers()

    print("\n=== Bob пытается вернуть 'Война и мир', которую не брал ===")
    lib.return_book(reader2, book1)   # должна быть ошибка
    lib.show_books()
    lib.show_readers()

    print("\n=== Tom берёт 'Python для всех' ===")
    lib.take_book(reader1, book3)
    lib.show_books()
    lib.show_readers()
   
    # Показываем
    print("=== Книги ===")
    lib.show_books()

    print("\n=== Читатели ===")
    lib.show_readers()

if __name__ == '__main__':
    main()