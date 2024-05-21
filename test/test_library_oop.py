import pytest
from Library.Library import Library
from Library.Book import Book
from Person.Librarian import Librarian
from Person.Member import Member

@pytest.fixture
def sample_book():
    return Book("Test Book", "Test Author", "1234567890")

@pytest.fixture
def sample_member():
    return Member("Test Member")

@pytest.fixture
def sample_librarian():
    return Librarian("Test Librarian")

@pytest.fixture
def sample_library():
    return Library()

def test_borrow_book(sample_book, sample_member):
    sample_member.borrow_book(sample_book, "borrow msg")
    assert not sample_book.is_available
    assert sample_book in sample_member.borrowed_books

def test_return_book(sample_book, sample_member):
    sample_member.borrow_book(sample_book, "borrow msg.")
    sample_member.return_book(sample_book)
    assert sample_book.is_available
    assert sample_book not in sample_member.borrowed_books

def test_add_book(sample_book, sample_library, sample_librarian):
    sample_librarian.add_book(sample_library, sample_book)
    assert sample_book in sample_library.books

def test_remove_book(sample_book, sample_library, sample_librarian):
    sample_librarian.add_book(sample_library, sample_book)
    sample_librarian.remove_book(sample_library, sample_book)
    assert sample_book not in sample_library.books
