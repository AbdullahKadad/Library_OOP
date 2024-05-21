from Person.Person import Person

class Librarian(Person):
    """
        Initializes a new instance of the Librarian class.

        This constructor method sets up a new librarian with the provided name. 
        It calls the constructor of the base class `Person` to initialize the name attribute.

        Args:
            name (str): The name of the librarian.
    """
    def __init__(self, name):
        super().__init__(name)

    def add_book(self, library, book):
        """
        Adds a book to the library.

        This method appends the given book to the library's list of books 
        and prints a message indicating that the librarian has added the book.

        Args:
            library (Library): The library to which the book will be added.
            book (Book): The book to be added to the library.
        """
        library.books.append(book)
        print(f"{self.name} added {book.title} to the library.")

    def remove_book(self, library, book):
        """
        Removes a book from the library.

        This method removes the given book from the library's list of books 
        if it exists in the list. It prints a message indicating that the librarian 
        has removed the book or if the book was not found in the library.

        Args:
            library (Library): The library from which the book will be removed.
            book (Book): The book to be removed from the library.
        """
        if book in library.books:
            library.books.remove(book)
            print(f"{self.name} removed {book.title} from the library.")
        else:
            print(f"{book.title} is not in the library.")

    def get_role(self):
        """
        Returns the role of the person.

        This method returns a string indicating that the person's role is "Librarian".

        Returns:
            str: The role of the person, which is "Librarian".
        """
        return "Librarian"