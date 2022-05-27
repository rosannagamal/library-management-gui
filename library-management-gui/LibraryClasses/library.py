import datetime

from classes.book import Book
from classes.user import *
from LibraryClasses.json_functions import *


def extract_data(file):
        dct = list(unload_json(file).values())
        try:
            return set(dct[0]), set(dct[1]), dct[2], set(dct[3])
        except IndexError:
            return set(), set(), dict(), set()

class Library:

    registered: set
    restricted: set
    active_loans: dict
    books: set

    registered, restricted, active_loans, books = extract_data("LibraryClasses/library.json")

    borrowing_policy: dict = {"loan period": 7, "grace period": 7, "extension number": 3}

    def __dict__(self) -> dict:
        return {
            "registered": [user.__dict__() for user in self.registered],
            "restricted": [book.__dict__() for book in self.restricted],
            "books": [book.__dict__() for book in self.books]
        }

    @staticmethod
    def find_user(registered_users: set, username: str) -> User:
        """
        This method iterates through the list of users and finds the one
        that matches the username used by the user to log in.

        Args:
            registered_users (set): _description_
            username (str): _description_

        Returns:
            User: object of class user
        """
        for user in registered_users:
            if user.username == username:
                return user

    @staticmethod
    def find_book(books: set, title: str) -> Book:
        """
        This method iterates through the list of books and finds the one
        that matches the title given by the user.

        Args:
            books (set): _description_
            title (str): _description_

        Returns:
            Book: object of book class
        """
        for book in books:
            if title.lower() in book.title.lower():
                return book

    @staticmethod
    def date() -> str:
        """
        method returns today's date

        Returns:
            _type_: _description_
        """
        return datetime.datetime.now().strftime("%d-%m-%Y")

    @staticmethod
    def date_difference(old_date: str, todays_date: str) -> int:
        """
        this method calculates the amount of days that have passed from a certain date

        Args:
            old_date (str)
            today's_date (str)

        Returns:
            int: numbers of days passed
        """
        return (todays_date - old_date).days

    @staticmethod
    def update_date(days: str) -> str:
        """
        The method takes today's date and add to it the number of days given by the user

        Args:
            days (str)

        Returns:
            date
        """
        date = datetime.datetime.now() + datetime.timedelta(days=int(int(days)))
        return date.strftime("%d-%m-%Y")

    def add_user(self, user_type: int, **kwargs) -> User:
        """
        Method that creates a new instance of the user class and appends
        it to the list of registered users.

        Args:
            user_type (int):

        Returns:
            _type_: _description_
        """
        users_lst = [Regular, Student, Librarian, Admin]

        new_user = users_lst[user_type - 1](**kwargs)

        self.registered.add(new_user)
        return new_user

    def remove_user(self, registered_users: set, username: str) -> None:
        """
        Method removes the user instance from the users set

        Args:
            registered_users (set)
            username (str)
        """
        user = self.find_user(registered_users, username)
        registered_users.remove(user)

    def add_book(self, **kwargs) -> None:
        """
        Method adds books to set of books
        """
        new_book = Book(**kwargs)
        self.books.add(new_book)
        Library.books.add(new_book)

    def remove_book(self, books: set, title: str) -> None:
        """
        Method removes book from set of books
        Args:
            books (set)
            title (str)
        """
        book = self.find_book(books, title)
        books.remove(book)

    def borrow_book(self, books: set, user: User, title: str) -> None:
        try:
            # iterating through book list and finding book instance with the same title
            book = self.find_book(books, title)

            # adding 1 to the number of copies borrowed
            book.copies_borrowed += 1

            # adding title of the book and the date of borrowing to the dictionary self.active_loans
            self.active_loans[user.name].append(
                {
                    "title": title,
                    "date_borrowed": str(self.date()),
                    "return_date": str(self.update_date(7)),
                }
            )
            print(f"You have successfully borrowed{title}")

        except AttributeError:
            print("Book not found.")

    def return_book(self, name, title: str) -> bool:
        try:
            # iterating through book list and finding book instance with the same title
            book = self.find_book(self.books, title)

            # subtracting 1 from the number of copies borrowed
            book.copies_borrowed -= 1

            # self.active_loans = 'name of user': {'title': date of borrowing}

            for dct in self.active_loans[name]:
                value = list(dct.values())

                if title in value[0]:
                    self.active_loans[name].remove(dct)
                    return True

        except AttributeError:
            print("This book was never added to your library.")
            return False

    def set_borrowing_policy(self, user_input: list) -> None:
        # user_input = ['new loan period', 'new grace period', 'new number of extensions ']

        self.borrowing_policy = {
            "loan period": user_input[0],
            "grace period": user_input[1],
            "extension number": user_input[2],
        }

    def restrict_user(self, user: User) -> bool:

        # adding the loan and the grace period
        max_days = int(self.borrowing_policy["loan period"]) + int(
            self.borrowing_policy["grace period"]
        )

        # iterating through the active loans dict to make sure the user doesn't have any unsetteled debts
        for key, value in self.active_loans[user.name].items():
            # calculating how many days the user has been keeping a certain book
            days_borrowed = self.date_difference(value, self.date())

            # checking if the days exceed te loan period and the grace period
            if days_borrowed > max_days:
                self.restricted.add(user)

                # printing warning message to user
                print(
                    f"Dear user, you have borrowed the book {key} for {days_borrowed} \
                    days.\nMake sure you return it before you borrow another one."
                )
                return True
            # returning false if the user doesn't have any unsettled debts
        return False

    def most_borrowed(self) -> int:

        # appending the number of borrowed books for each book
        # instance in a list and then returning the index of the most borrowed book

        lst = [book.copies_borrowed for book in self.books]
        return lst.index(max(lst))

    def least_borrowed(self) -> int:

        # appending the number of borrowed books for each book
        # instance in a list and then returning the index of the least borrowed books

        lst = [book.copies_borrowed for book in self.books]
        return lst.index(min(lst))

    def authenticate(self, registered_users: set, username, password):
        try:
            user = self.find_user(registered_users, username)
            if user.password == password:
                return True
            else:
                print("The password you've enterd is incorrect. Please try again.")

        except AttributeError:
            print("The username you have entered is incorrect.")

    def extend_loan_period(self, user: User, title: str, days: int):
        try:
            for dct in self.active_loans[user.name]:
                value = list(dct.values())

                if title in value[0]:
                    dct["return_date"] = self.update_date(int(days) + 7)

        except AttributeError:
            print(
                "The title you're looking for has already been returned or has never been added."
            )

    @staticmethod
    def store_data(file: str, dct: dict):
        load_json(file, dct)

