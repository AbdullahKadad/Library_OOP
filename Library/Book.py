class Book:
    def __init__(self, title, author, isbn):
        """
        Initializes a new instance of the Book class.

        This constructor method sets up a new book with the provided title, author, and ISBN. 
        It also sets the availability status of the book to True by default.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            isbn (str): The International Standard Book Number (ISBN) of the book.
        """
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True
        self._return_msg = "No message!"

    def get_return_msg(self):
        print(self._return_msg)
        return self._return_msg
    
    def get_status(self):
        print(f"Availability: {self.is_available}")
        return self.is_available
    
    def get_title(self):
        print(f"Title: {self.title}")
        return "Done"

    def get_author(self):
        print(f"Author: {self.author}")
        return "Done"

    def __str__(self):
        """
        Returns a string representation of the Book instance.

        This method provides a human-readable summary of the book's details, including its title, author, ISBN, 
        and availability status.

        Returns:
            str: A string in the format "title by author, ISBN: isbn, Available: Yes/No".
        """
        return f"{self.title} by {self.author}, ISBN: {self.isbn}, Available: {'Yes' if self.is_available else 'No'}"