from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name):
        """
        Initializes a new instance of the Person class.

        This constructor method sets up a new person with the provided name.
        The Person class is an abstract base class, so it cannot be instantiated directly.

        Args:
            name (str): The name of the person.
        """
        self.name = name

    @abstractmethod
    def get_role(self):
        """
        Returns the role of the person.

        This is an abstract method that must be implemented by any subclass of Person. 
        It should return a string indicating the role of the person.

        Returns:
            str: The role of the person.
        """
        pass