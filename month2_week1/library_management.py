import datetime


class Book:
    def __init__(self, title, author, isbn, amount):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.amount = amount
        self.availability_status = True if amount > 0 else False

    def display_details(self):
        print(f"Title: {self.title}\nAuthor: {self.author}\nISBN: {self.isbn}\nAmount: {self.amount}\nAvailability: {'Available' if self.availability_status else 'Not Available'}\n")


class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.books_borrowed = []

    def display_details(self):
        print(f"User ID: {self.user_id}\nName: {self.name}\nBooks Borrowed: {', '.join([book.title for book in self.books_borrowed])}\n")


class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.transactions = []

    def add_book(self, book):
        self.books.append(book)

    def register_user(self, user):
        self.users.append(user)

    def borrow_book(self, user, book_title):
        book = next((b for b in self.books if b.title == book_title and b.availability_status and b.amount > 0), None)
        
        if book:
            book.availability_status = False
            book.amount -= 1
            user.books_borrowed.append(book)
            transaction = Transaction(user, book, "Borrowed")
            self.transactions.append(transaction)
            print(f"{user.name} has successfully borrowed '{book.title}'.")
        else:
            print(f"Sorry, '{book_title}' is not available for borrowing or has reached its maximum limit.")

    def return_book(self, user, book_title):
        book = next((b for b in user.books_borrowed if b.title == book_title), None)

        if book:
            book.availability_status = True
            book.amount += 1
            user.books_borrowed.remove(book)
            transaction = Transaction(user, book, "Returned")
            self.transactions.append(transaction)
            print(f"{user.name} has successfully returned '{book.title}'.")
        else:
            print(f"Error: '{book_title}' is not borrowed by {user.name}.")

    def generate_transaction_report(self):
        for transaction in self.transactions:
            print(f"{transaction.user.name} {transaction.action} '{transaction.book.title}' on {transaction.timestamp}")


class Transaction:
    def __init__(self, user, book, action):
        self.user = user
        self.book = book
        self.action = action
        self.timestamp = datetime.datetime.now()

if __name__ == "__main__":
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Register User")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Generate Transaction Report")
        print("6. display user information")
        print("7. display book information")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            isbn = input("Enter ISBN: ")
            amount = int(input("Enter amount: "))
            book = Book(title, author, isbn, amount)
            library.add_book(book)
            print(f"Book '{title}' added successfully.")

        elif choice == "2":
            user_id = input("Enter user ID: ")
            name = input("Enter user name: ")
            user = User(user_id, name)
            library.register_user(user)
            print(f"User '{name}' registered successfully.")

        elif choice == "3":
            user_id = input("Enter user ID: ")
            book_title = input("Enter book title to borrow: ")
            user = next((u for u in library.users if u.user_id == user_id), None)
            if user:
                library.borrow_book(user, book_title)
            else:
                print("Error: User not found.")

        elif choice == "4":
            user_id = input("Enter user ID: ")
            book_title = input("Enter book title to return: ")
            user = next((u for u in library.users if u.user_id == user_id), None)
            if user:
                library.return_book(user, book_title)
            else:
                print("Error: User not found.")

        elif choice == "5":
            library.generate_transaction_report()

        elif choice == "6":
            user_id=input("Please enter user id")
            user = next((u for u in library.users if u.user_id == user_id), None)
            if user:
                user.display_details()
        elif choice == "7":
            book_title=input("Please enter Book Title")
            book=next((b for b in library.books if b.title == book_title), None)
            if book:
                book.display_details()
            print("Exiting Library Management System.")
            break

        else:
            print("Invalid choice. Please enter a valid option.")
