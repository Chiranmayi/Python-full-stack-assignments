class Library:

    def __init__(self):
        self.books = {}

    def add_book(self, book_id, book_name):
        self.books[book_id] = {
            "name": book_name,
            "available": True
        }
        print("Book added successfully.")

    def issue_book(self, book_id):
        if book_id not in self.books:
            print("Book not found.")

        elif self.books[book_id]["available"]:
            self.books[book_id]["available"] = False
            print("Book issued successfully.")

        else:
            print("Book is already issued.")

    def return_book(self, book_id):
        if book_id not in self.books:
            print("Book not found.")

        elif not self.books[book_id]["available"]:
            self.books[book_id]["available"] = True
            print("Book returned successfully.")

        else:
            print("Book is already available.")

    def display_books(self):
        print("\nAvailable Books:")

        for book_id, book in self.books.items():
            if book["available"]:
                print(book_id, "-", book["name"])


library = Library()

while True:

    print("\n--- Library Menu ---")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Display Available Books")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book_id = input("Enter Book ID: ")
        book_name = input("Enter Book Name: ")
        library.add_book(book_id, book_name)

    elif choice == "2":
        book_id = input("Enter Book ID: ")
        library.issue_book(book_id)

    elif choice == "3":
        book_id = input("Enter Book ID: ")
        library.return_book(book_id)

    elif choice == "4":
        library.display_books()

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")