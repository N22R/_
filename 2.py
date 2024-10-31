class Book:
    def __init__(self, pages=None, author=None, price=None, evening_hours=None):
        self.__pages = pages
        self.__author = author
        self.price = price
        self.__evening_hours = evening_hours

    def get_pages(self):
        return self.__pages
    
    def get_author(self):
        return self.__author

    def get_evening_hours(self):
        return self.__evening_hours

    def set_evening_hours(self, hours):
        self.__evening_hours = hours

    def __repr__(self):
        return (f'Кількість сторінок: {self.__pages} '
                f'\nАвтор: {self.__author} '
                f'\nЦіна: {self.price} грн\n'
                f'\nГодини читання вечором: {self.__evening_hours}\n')

    def __del__(self):
        print(f"{self.__str__()}")

def find_most_read_book(books):
    max_hours = -1
    most_read_book = None
    for book in books:
        if book.get_evening_hours() > max_hours:
            max_hours = book.get_evening_hours()
            most_read_book = book
    return most_read_book

def main():
    book1 = Book(300, 'Тарас Шевченко', 120, 10)
    book2 = Book(250, 'Ліна Костенко', 200, 15)
    book3 = Book(500, 'Леся Українка', 150, 12)

    books = [book1, book2, book3]

    for book in books:
        print(repr(book))

    most_read_book = find_most_read_book(books)
    print(f"Найбільше прочитана книжка: {repr(most_read_book)}")

main()
