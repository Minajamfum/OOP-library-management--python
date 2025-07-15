from Book import Book
from Magazine import Magazine
from BookStore import BookStore

bookStore = BookStore()

while (True):
    move = input("what do you want to do?(add Book , Borrow , Return , show Books, exit )")
    move = move.lower()

    if move == "add book":
        name = input("enter the name of book: ")
        author = input("enter the name of author: ")
        type = input("enter 'book' or 'magazine': ")

        if type.lower() == "magazine":
            book = Magazine(name, author)
        elif type.lower() == "book":
            book = Book(name, author)
        else:
            raise TypeError("not such type exist")

        bookStore.addBook(book)

    elif move == "borrow":
        name = input("enter the name of book: ")
        bookStore.Borrow(name)

    elif move == "return":
        name = input("enter the book name to return: ")
        bookStore.Returning(name)

    elif move == "show books":
        bookStore.printInfo()

    elif move == "exit":
        break

    else:
        print("Invalid command")
        raise ValueError("Invalid command")
