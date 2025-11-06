# Library Management System - OOP Style


class Book:
    """
    Class for handling library's Book
    """

    def __init__(self, book_id, title, author, total_copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.total_copies = total_copies
        self.available_copies = total_copies


class Member:
    """
    Class for handling library's member
    """

    def __init__(self, member_id, name, email):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.borrowed_books = []

    def borrow_book(self, book):
        """Process a book borrowing transaction"""
        if book.available_copies <= 0:
            print("Error: No copies available!")
            return False

        if len(self.borrowed_books) >= 3:
            print("Error: Member has reached borrowing limit!")
            return False

        book.available_copies -= 1
        self.borrowed_books.append(book.book_id)
        return True

    def return_book(self, book):
        """Process a book return transaction"""
        if book.book_id not in self.borrowed_books:
            print("Error: This member hasn't borrowed this book!")
            return False

        # Process the return
        book.available_copies += 1
        self.borrowed_books.remove(book.book_id)

        return True


