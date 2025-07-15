from zoneinfo import available_timezones
from Book import Book
from typing import List


class BookStore():
    def __init__(self):
        self.currentBooks: List[Book] = []

    def addBook(self, book):
        self.currentBooks.append(book)
        print("Successfully added")

    def Borrow(self, book_name):
        for book in self.currentBooks:
            if book.name == book_name and book.isAvailable:
                book.is_Available = False
                print("You borrowed the Book")
                return
        raise ValueError("Book not found or not available")

    def Returning(self, book_name):
        for book in self.currentBooks:
            if book.name == book_name and not book.isAvailable:
                book.is_Available = True
                print("You returned the book")
                return
        raise ValueError("Book not found or was not borrowed")

    def printInfo(self):
        for book in self.currentBooks:
            if book.isAvailable:
                status = "available"
            else:
                status = "Borrowed"
            print("name:", book.getname, "author name:", book.getAuthor, "status:", status)
