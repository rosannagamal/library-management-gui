import os
from tkinter import *
from PIL import ImageTk, Image
from LibraryClasses import library

# Instance of library class
library = library.Library()


class FoundBook(Toplevel):
    def __init__(self, book, user):
        Toplevel.__init__(self)

        self.book = book
        self.user = user

        # Frame 4
        self.title('Search')
        self.geometry('900x500')
        self.config(bg='#07272C')

        self.frame()    # Frame Picture

        self.book_cover()   # Displays Book cover

        # Book Info Labels
        self.book_title()
        self.book_author()
        self.book_isbn()
        self.book_type()

        # Borrow Book Button
        self.button()

    def frame(self):
        # Frame Picture
        img = ImageTk.PhotoImage(file='home_page/book_page.png')
        label = Label(self, image=img, bg='#061A1D')
        label.image = img
        label.place(x=0, y=0)

    def book_cover(self):
        # Cover Picture
        file = os.path.join('book_covers', self.book.file)
        img = ImageTk.PhotoImage(file=file)
        label = Label(self, image=img, bg='#061A1D')
        label.image = img
        label.place(x=97, y=128)

    def book_title(self):
        # Title Label
        title_label = Label(self, text='Title', fg='white', bg='#08262A', font=('Arial', 15, 'bold'))
        title_label.place(x=392, y=99)
        # Book Title
        title = Label(self, text=self.book.title, fg='white', bg='#08262A', font=('Arial', 15))
        title.place(x=524, y=99)

    def book_author(self):
        # Author Label
        author_label = Label(self, text='Author', fg='white', bg='#08262A', font=('Arial', 15, 'bold'))
        author_label.place(x=392, y=160)
        # Book Author
        author = Label(self, text=self.book.author, fg='white', bg='#08262A', font=('Arial', 15 ))
        author.place(x=524, y=160)

    def book_isbn(self):
        # ISBN Label
        isbn_label = Label(self, text='ISBN', fg='white', bg='#08262A', font=('Arial', 15, 'bold'))
        isbn_label.place(x=392, y=222)
        # Book ISBN
        isbn = Label(self, text=self.book.isbn, fg='white', bg='#08262A', font=('Arial', 15))
        isbn.place(x=524, y=222)

    def book_type(self):
        # Book Type Label Label
        book_type_label = Label(self, text='Type',  fg='white', bg='#08262A', font=('Arial', 15, 'bold'))
        book_type_label.place(x=392, y=282)
        # Converting number to appropriate text
        book_type = 'Hard Copy' if self.book.online_physical == '1' else 'Soft Copy'
        # Book Type
        online_physical = Label(self, text=book_type,  fg='white', bg='#08262A', font=('Arial', 15))
        online_physical.place(x=637, y=282)

    def borrow_book(self):
        # Borrow book function from library class
        user = library.find_user(library.registered, self.user)
        library.borrow_book(library.books, user, self.book.title)
        Label(self, text='Book Borrowed.', bg='#061A1D', font=('Inter', 15, 'bold'), fg='white').place(x=519, y=350)

    def button(self):
        # Creating Label for Button
        button_label = Label(self, text='Borrow', font=('Inter', 15, 'bold'), fg='white', bg='#08262A', cursor='hand')
        button_label.place(x=409, y=350)
        user = library.find_user(library.registered, self.user)
        button_label.bind('<Button-1>',lambda event: self.borrow_book())
