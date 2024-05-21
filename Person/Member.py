from Person.Person import Person

class Member(Person):
    def __init__(self, name):
        """
        Initializes a new instance of the Member class.

        This constructor method sets up a new member with the provided name.
        It also initializes an empty list to keep track of books borrowed by the member.
        
        Args:
            name (str): The name of the member.
        """
        super().__init__(name)
        self.borrowed_books = []

    def borrow_book(self, book, due_date):
        """
        It  allows the member to borrow a book from the library if it is available.
        It takes two params: book object and due_date message.
        This method checks if the book is available. If it is, the book's availability is set to False,
        the book is added to the member's list of borrowed books, and a message is printed.
        If the book is not available, an appropriate message is printed.
        
        Args:
            book (Book): The book to be borrowed.
        """
        if book.is_available:
            book.is_available = False
            book._return_msg = due_date
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed {book.title}.")
        else:
            print(f"Sorry, {book.title} is not available.")

    def return_book(self, book):
        """
        Allows the member to return a borrowed book to the library.

        This method checks if the book is in the member's list of borrowed books. 
        If it is, the book's availability is set to True, the book is removed from the list, 
        and a message is printed. If the book is not in the list, an appropriate message is printed.
        
        Args:
            book (Book): The book to be returned.
        """
        if book in self.borrowed_books:
            book.is_available = True
            book._return_msg = "No message!"
            self.borrowed_books.remove(book)
            print(f"{self.name} returned {book.title}.")
        else:
            print(f"{self.name} does not have {book.title}.")

    def get_role(self):
        """
        Returns the role of the person.

        This method returns a string indicating that the person's role is "Member".
        
        Returns:
            str: The role of the person, which is "Member".
        """
        return "Member"
    


