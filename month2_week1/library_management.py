import datetime
import os


class Book:
    def __init__(self, title, author, isbn, amount):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.amount = amount
        self.availability_status = True if amount > 0 else False

    # def __lt__(self,other):
    #     return self.isbn<other.isbn

    def display_details(self):
        print(f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Amount: {self.amount}, Availability: {'Available' if self.availability_status else 'Not Available'}")


class User:
    userCount=0
    def __init__(self,name):
        User.userCount += 1
        self.user_id = User.userCount
        self.name = name
        self.books_borrowed = []

    def display_details(self):
        books_borrowed='\n'.join(['\t'+book.title for book in self.books_borrowed] if len(self.books_borrowed)>0 else 'no boorowed books')
        print(f"User ID: {self.user_id}, Name: {self.name}\nBooks Borrowed:\n {books_borrowed}\n")

class Transaction:
    def __init__(self, user, book, action):
        self.user = user
        self.book = book
        self.action = action
        self.timestamp = datetime.datetime.now().strftime("%Y-%m-%d  %H:%M")


class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.books_on_borrowing ={}
        self.transactions = []

    def add_book(self, book):
        self.sortBook()
        sBook=self.searchBook(book.isbn,0,len(self.books)-1)
        if sBook:
            sBook.amount+=book.amount
        else:
            self.books.append(book)
        
        print(f"=> {book.amount} amount of {book.title} books added. \n=> Now {sBook.amount if sBook else book.amount} amount of {sBook.title if sBook else book.title} books are available in the library")

    def register_user(self, user):
        self.users.append(user)
        print(f"{user.name} is successfully registered ID: {user.user_id}")

    def borrow_book(self, user, book_title):
        book = next((b for b in self.books if b.title == book_title and b.availability_status and b.amount > 0), None)
        
        if book:
            borrBook=Book(book.title,book.author,book.isbn,1)
            book.availability_status = True if book.amount > 0 else False
            book.amount -= 1
            user.books_borrowed.append(borrBook)
            self.books_on_borrowing[user]=user.books_borrowed
            transaction = Transaction(user, borrBook, "Borrowed")
            self.transactions.append(transaction)
            print(f"{user.name} has successfully borrowed '{book.title}'.")
        else:
            print(f"Sorry, '{book_title}' is not available for borrowing.")

    def return_book(self, user, book_title):
        book = next((b for b in self.books_on_borrowing[user] if b.title == book_title), None)

        if book:
            retBook=next((b for b in self.books if b.title == book.title), None)
            if retBook:
                retBook.availability_status =True
                retBook.amount += 1
            else:
                self.books.append(book)
            
            self.books_on_borrowing[user].remove(book)
            user.books_borrowed.remove(book)
            transaction = Transaction(user, book, "Returned")
            self.transactions.append(transaction)
            print(f"{user.name} has successfully returned '{book.title}'.")
        else:
            print(f"Error: '{book_title}' is not borrowed by {user.name}.")

    def generateTransactionReport(self):
        for transaction in self.transactions:
            print(f"{transaction.user.name} {transaction.action} '{transaction.book.title}' on {transaction.timestamp}")
    
    def displayBorrowedBooks(self):
        for user, books in enumerate(self.books_on_borrowing):
            borrowedBooks="\n".join([b.title for b in books ]if len(books) > 0 else "No books Borrowed")
            print(f"Name: {user.name} Borrowed Books:\n{borrowedBooks}")

    def sortBook(self):
        self.books.sort(key=lambda Book: Book.isbn)

    def searchBook(self,isbn,low,high):

        while low <= high:
            mid=(low+high)//2

            if self.books[mid].isbn==isbn:
                return self.books[mid]
            elif self.books[mid].isbn<isbn:
                low=mid+1
            else:
                high=mid-1
        
        return None
        

def userLogin(user,library):

    while True:
        os.system("clear")

        print("================ USER PAGE =================")
        print("1. Borrow Book")
        print("2. Return Book")
        print("3. display borrowing details")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice ==1:
            book_title = input("Enter book title to borrow: ")
            library.borrow_book(user, book_title)
        elif choice ==2:
            book_title = input("Enter book title to return: ")
            library.return_book(user, book_title)
        elif choice ==3:
            user.display_details()
        elif choice ==4:
            break
        else:
            print("Wrong choice!")

        input("please enter to continue...")

def adminLogin(library):

    while True:
        os.system("clear")

        print("================ ADMIN PAGE =================")

        print("1. Add Book")
        print("2. Register User")
        print("3. display Single Book information")
        print("4. display All books information")
        print("5. Display All Users information")
        print("6. Display Single User information")
        print("7. Generate Transaction Report")
        print("8. display borrowed books")
        print("9. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            isbn = input("Enter ISBN: ")
            amount = int(input("Enter amount: "))
            book = Book(title, author, isbn, amount)
            library.add_book(book)

        elif choice == 2:
            name = input("Enter user name: ")
            user = User(name)
            library.register_user(user)

        elif choice == 3:
            book_title=input("Please enter Book Title")
            book=next((b for b in library.books if b.title == book_title), None)
            if book:
                book.display_details()
        
        elif choice == 4:
            for book in library.books:
                book.display_details()
        
        elif choice ==5:
            for user in library.users:
                user.display_details()
        elif choice ==6:
            user_id=input("Please enter user id")
            user = next((u for u in library.users if u.user_id == user_id), None)
            if user:
                user.display_details()
        elif choice == 7:
            library.generateTransactionReport()
        elif choice ==8:
            library.displayBorrowedBooks()
        elif choice ==9:
            break
        else:
            print("Wrong choice!")

        input("please enter to continue...")

if __name__ == "__main__":
    library = Library()

    while True:
        os.system("clear")
        print("\n====================LIBRARY MANAGEMENT SYSTEM HOME PAGE================================")
        print("1. User Login")
        print("2. dmin Login")
        print("3. Exit")

        choice = int(input("Enter your choice: "))

        if choice ==1:
            user_id=int(input("Enter your user id: "))
            user = next((u for u in library.users if u.user_id == user_id),None)
            if user:
                userLogin(user,library)
            else:
                print(f"NO user found with {user_id} id number in library")
        elif choice ==2:
            adminLogin(library)
        elif choice ==3:
            break
        else:
            print("Wrong choice!")

        input("please enter to continue...")