class Library:
    _instance = None

    def __new__(cls):
        """
        Ensures that only one instance of the Library class is created (Singleton pattern).

        This method checks if an instance of the Library class already exists. If it doesn't,
        it creates a new instance and initializes the library's state by calling `_initialize`.
        If an instance already exists, it returns the existing instance.

        Returns:
            Library: The single instance of the Library class.
        """
        
        if cls._instance is None:
            cls._instance = super(Library, cls).__new__(cls)
            cls._instance._initialize()
        return cls._instance

    @staticmethod
    def instance():
        """
        Provides a global point of access to the single instance of the Library class.

        If the instance does not already exist, it is created.

        Returns:
            Library: The single instance of the Library class.
        """
        if Library._instance is None:
            Library()
        return Library._instance

    def _initialize(self):
        """
        Initializes the library's state.

        This method sets up the initial state of the library by creating an empty list of books.
        """
        self.books = []

    def display_books(self):
        """
        Displays all the books in the library.

        This method iterates over the list of books in the library and prints a string
        representation of each book using the `__str__` method of the Book class.
        """
        for book in self.books:
            print(book)
