from Library.Library import Library
from Library.Book import Book
from Person.Librarian import Librarian
from Person.Member import Member

if __name__ == "__main__":
    library = Library.instance()

    # Creating books
    book1 = Book("1984", "George Orwell", "1234567890")
    book2 = Book("To Kill a Mockingbird", "Harper Lee", "1234567891")

    # Creating persons
    member = Member("Alice")
    librarian = Librarian("Bob")

    # Librarian adds books to the library
    librarian.add_book(library, book1)
    librarian.add_book(library, book2)

    # Displaying books in the library
    library.display_books()

    # Member borrows a book
    member.borrow_book(book1, "I'll return the book after 2 days")

    book1.get_status()
    book1.get_return_msg()
    print(book1.is_available)
    print("______________")
    book2.get_return_msg()
    book2.get_status()
    book2.get_title()
    book2.get_author()

    # # Displaying books in the library after borrowing
    # library.display_books()

    # # Member returns a book
    # member.return_book(book1)

    # # Displaying books in the library after returning
    # library.display_books()