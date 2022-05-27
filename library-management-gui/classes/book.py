class Book:
    
    copies_borrowed: int = 0

    def __init__(self, title: str = "", author: str = "", isbn: str = "", total_copies: int = 0, online_physical: int = 0, file=None):
        
        self.title = title
        self.author = author
        self.isbn = isbn
        self.total_copies = total_copies
        self.online_physical = online_physical
        self.file = file
        self.available_copies: int = int(self.total_copies) - int(self.copies_borrowed)

    def __dict__(self) -> dict:
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "total copies": self.total_copies,
            "online physical": self.online_physical,
            "borrowed copies": self.copies_borrowed,
            "file": self.file
        }

    def __str__(self) -> str:
        return f"{self.title}\t{self.author}\t{self.isbn}\t{'Online Copy' if self.online_physical == 1 else 'Physical Copy'}\t{self.available_copies}"

    def __hash__(self) -> int:
        return hash(self.isbn)

    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o, type(self)):
            return NotImplemented
        return self.isbn == __o.isbn

    def instance(self, book_dict) -> str:

        # values = [title, author, isbn, total copies, online physical, copies borrowed, file]
        values = list(book_dict.values())

        # creating a new instance of the Book class from values extracted from dict
        book = Book(title=values[0], author=values[1], isbn=values[2],  total_copies=values[3], file=values[6])

        # setting the copies_borrowed and borrowers_info from data in dict
        book.copies_borrowed = values[5]

        return book