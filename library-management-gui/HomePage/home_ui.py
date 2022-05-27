import os
from tkinter import *
from PIL import ImageTk, Image
from HomePage.bookinfo_page import FoundBook
from library.library import Library

# Instance of library class
library = Library()
    

class HomePage(Tk):
    def __init__(self, user): 
        super().__init__()

        self.user = user     # Name of user from sign in page
        
        # Frame 3
        self.title('Home Page')
        self.geometry('1800x1500')
        self.config(bg='#07272C')

        self.frame()    # Frame Picture

        # Search Bar
        self.search_button()
        # Discover most borrowed book section
        self.discover()
        # Borrowed books section
        self.borrowed()
        # Newest books section
        self.last_added()
        
        self.mainloop()

    def frame(self):
        img = ImageTk.PhotoImage(file='/Users/rosannagamal/Documents/GitHub/library-management-gui/HomePage/home.png')
        Label(self, image=img, bg='white').place(x=0, y=0)

    def search_bar(self):
        # Entry
        entry = Entry(self, bg='#061A1D', bd=0, width=55, highlightthickness=0, fg='white')
        val = entry     # Value of the entry
        entry.insert(0, 'Search')
        entry.place(x=558, y=17)
        entry.bind("<FocusIn>", lambda e: entry.delete(0, 'end'))
        return val
        
    def search_button(self):
        # Magnifying glass icon
        pic = Image.open('/Users/rosannagamal/assignment_two/HomePage/search_button.png')
        photo = ImageTk.PhotoImage(pic)
        # Button Label
        button = Label(image=photo, cursor='hand', bg='#061A1D')
        button.image = photo
        button.place(x=1135, y=15)
        button.bind('<Button-1>', lambda event: self.search_book())

    def search_book(self):
        val = self.search_bar()    # Value extracted from search bar
        book = library.find_book(library.books, val.get().lower())
        # Window displaying data about book
        FoundBook(book, self.user)

    def discover(self):
        # Displays cover page abot most borrowed book
        lst = list(library.books)   # Converting set object to list
        book = lst[library.most_borrowed()]     # Index of book

        file = os.path.join('/Users/rosannagamal/assignment_two/book_covers', book.file)
        img = ImageTk.PhotoImage(file=file)
        frame = Label(self, image=img, bg='#061A1D')
        frame.image = img
        frame.place(x=192, y=148)

    def borrowed(self):
        # Displaying data about borrowed books
        for dct in library.active_loans[self.user]:
            value = list(dct.values())
            l1 = Label(self, text='Title', bg='#0B3238', fg='white', font=('Arial', 20, 'bold'))
            l1.place(x=304, y=654)

            l2 = Label(self, text=value[0], bg='#D9D9D9', fg='black', font=('Arial', 20, 'bold'))
            l2.place(x=203, y=711)

            l3 = Label(self, text='Return Date', bg='#0B3238', fg='white', font=('Arial', 20, 'bold'))
            l3.place(x=265, y=768)

            l4 = Label(self, text=value[2], bg='#D9D9D9', fg='black', font=('Arial', 20, 'bold'))
            l4.place(x=203, y=825)

            l5 = Label(self, text='Return', bg='#073A42', fg='white', cursor='hand', font=('Arial', 20, 'bold'))
            l5.place(x=284, y=879)

            l5.bind('<Button-1>', lambda event: self.return_func([l1, l2, l3, l4, l5], value[0]))

    def return_func(self, lst, title):
        # Return book function from library class
        if library.return_book(self.user, title):
            for i in lst:
                i.destroy()

    def last_added(self):
        # Displaying cover of the newest books
        lst = list(library.books)
        book1 = lst[-1]
        book2 = lst[-2]

        file1 = os.path.join('/Users/rosannagamal/assignment_two/book_covers', book1.file)
        img1 = ImageTk.PhotoImage(file=file1)
        frame = Label(self, image=img1, bg='#061A1D')
        frame.image = img1
        frame.place(x=1280, y=185)

        file2 = os.path.join('/Users/rosannagamal/assignment_two/book_covers', book2.file)
        img2 = ImageTk.PhotoImage(file=file2)
        frame = Label(self, image=img2, bg='#061A1D')
        frame.image = img2
        frame.place(x=1280, y=578)
