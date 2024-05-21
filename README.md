# Library Management System with Singleton Design Pattern

Authors:

- Abdullah Qdad

- [some one](https://google.com)

## OOP Principles

- Encapsulation
- Inheritance
- Polymorphism
- Abstraction
- Singleton Design Pattern

### Implementation

```python
from abc import ABC, abstractmethod

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True

    def __str__(self):
        return f"{self.title} by {self.author}, ISBN: {self.isbn}, Available: {'Yes' if self.is_available else 'No'}"

class Person(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_role(self):
        pass

class Member(Person):
    def __init__(self, name):
        super().__init__(name)
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.is_available:
            book.is_available = False
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed {book.title}.")
        else:
            print(f"Sorry, {book.title} is not available.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_available = True
            self.borrowed_books.remove(book)
            print(f"{self.name} returned {book.title}.")
        else:
            print(f"{self.name} does not have {book.title}.")

    def get_role(self):
        return "Member"

class Librarian(Person):
    def __init__(self, name):
        super().__init__(name)

    def add_book(self, library, book):
        library.books.append(book)
        print(f"{self.name} added {book.title} to the library.")

    def remove_book(self, library, book):
        if book in library.books:
            library.books.remove(book)
            print(f"{self.name} removed {book.title} from the library.")
        else:
            print(f"{book.title} is not in the library.")

    def get_role(self):
        return "Librarian"

class Library:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Library, cls).__new__(cls)
            cls._instance.books = []
        return cls._instance

    def display_books(self):
        for book in self.books:
            print(book)

# Example Usage
library = Library()

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
member.borrow_book(book1)

# Displaying books in the library after borrowing
library.display_books()

# Member returns a book
member.return_book(book1)

# Displaying books in the library after returning
library.display_books()
```

### Explanation

1. Singleton Design Pattern: The Library class implements the Singleton pattern. The __new__ method ensures only one instance of the Library class is created. When Library() is called, it checks if an instance already exists; if not, it creates a new one. Otherwise, it returns the existing instance.

2. Encapsulation: The attributes and methods related to Book, Person, Member, Librarian, and Library are encapsulated within their respective classes.

3. Inheritance: The Member and Librarian classes inherit from the abstract base class Person.

4. Polymorphism: The get_role method is overridden in both Member and Librarian classes, demonstrating polymorphism.

5. Abstraction: The Person class contains an abstract method get_role that must be implemented by any subclass.
