# Overview

A project which show you a library managment system (LMS) in both procedural and OOP style.
The main style is procedural, and have been rewritten into OOP style in the later date.

# Folder Structure
```
oop_assignment_1/
│
├── procedural_version          # The folder containing Procedural version of the LMS
    ├── library_procedural.py   # The LMS system (written in procedural style)
    ├── test_procedural.py      # Test program for Procedural LMS version
├── oop_solution                # The folder containing OOP version of the LMS
    ├── library_oop.py          # The LMS system (written in OOP style)
    ├── test_oop.py             # Test program for OOP LMS version
├── README.md                   # This file
```

# Design Overview

## Book
This is an empty class that only the book metadata, there's no function here because everything is handled via Member / Library

Holds `book_id, title, author, total_copies` data

## Member
A class which hold member data, have the `borrow_book` and `return_book` function, which when called, return True and False depending on if that operation is successful.

Holds `member_id, name, email` data

## Library
The library managment system class itself. Handle various tasks such as member registeration, book registeration.

Holds `books, members, borrowed_books` data

Have the following functions
- add_member
    - Register a new member
- add_book
    - Register a new book
- find_member
    - Find a member using their id
- find_book
    - Find a book using their id
- borrow_book
    - Borrow a book using member id and book id
- return_book
    - Return a book using member id and book id
- display_available_books
    - Show all available books that can be borrowed
- display_member_books
    - Show all the books that have been borrowed

# Testing

Have basic test-case and edge cases intergrated to the code-base.

# How to test

Procedural
```bash
python procedural_version/test_procedural.py
```

OOP
```bash
python oop_solution/test_oop.py
```