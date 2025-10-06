# library_management.py
# Implementation of Book and Library classes

class Book:
    """Represents a book with title, author, and availability status."""

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        """Mark the book as checked out if available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False  # Already checked out

    def return_book(self):
        """Mark the book as returned (available again)."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False  # Already returned

    def is_available(self):
        """Check if the book is currently available."""
        return not self._is_checked_out


class Library:
    """Represents a library that manages a collection of books."""

    def __init__(self):
        self._books = []  # Private list to store Book instances

    def add_book(self, book):
        """Add a new book to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by its title."""
        for book in self._books:
            if book.title.lower() == title.lower():
                if book.check_out():
                    print(f"'{book.title}' has been checked out.")
                else:
                    print(f"'{book.title}' is already checked out.")
                return
        print(f"No book found with title '{title}'.")

    def return_book(self, title):
        """Return a book by its title."""
        for book in self._books:
            if book.title.lower() == title.lower():
                if book.return_book():
                    print(f"'{book.title}' has been returned.")
                else:
                    print(f"'{book.title}' was not checked out.")
                return
        print(f"No book found with title '{title}'.")

    def list_available_books(self):
        """List all available (not checked out) books."""
        available_books = [book for book in self._books if book.is_available()]
        if not available_books:
            print("No books available.")
        else:
            for book in available_books:
                print(f"{book.title} by {book.author}")
