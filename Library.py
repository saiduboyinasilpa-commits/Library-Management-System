# Library Management System

books = []

def add_book():
    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")

    book = {
        "id": book_id,
        "title": title,
        "author": author,
        "status": "Available"
    }

    books.append(book)
    print("Book added successfully!\n")


def display_books():
    if not books:
        print("No books available.\n")
        return

    print("\n----- Library Books -----")

    for book in books:
        print("Book ID:", book["id"])
        print("Title:", book["title"])
        print("Author:", book["author"])
        print("Status:", book["status"])
        print("------------------------")


def search_book():
    book_id = input("Enter Book ID to search: ")

    for book in books:
        if book["id"] == book_id:
            print("\nBook Found!")
            print("Title:", book["title"])
            print("Author:", book["author"])
            print("Status:", book["status"])
            return

    print("Book not found.\n")


def issue_book():
    book_id = input("Enter Book ID to issue: ")

    for book in books:
        if book["id"] == book_id:
            if book["status"] == "Available":
                book["status"] = "Issued"
                print("Book issued successfully!\n")
            else:
                print("Book is already issued.\n")
            return

    print("Book not found.\n")


def return_book():
    book_id = input("Enter Book ID to return: ")

    for book in books:
        if book["id"] == book_id:
            if book["status"] == "Issued":
                book["status"] = "Available"
                print("Book returned successfully!\n")
            else:
                print("Book was not issued.\n")
            return

    print("Book not found.\n")


def delete_book():
    book_id = input("Enter Book ID to delete: ")

    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            print("Book deleted successfully!\n")
            return

    print("Book not found.\n")


# Main Menu
while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Delete Book")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        display_books()

    elif choice == "3":
        search_book()

    elif choice == "4":
        issue_book()

    elif choice == "5":
        return_book()

    elif choice == "6":
        delete_book()

    elif choice == "7":
        print("Thank you for using Library Management System!")
        break

    else:
        print("Invalid choice. Please try again.")