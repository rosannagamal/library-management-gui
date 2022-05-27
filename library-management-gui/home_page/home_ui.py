import os
from tkinter import *
from PIL import ImageTk, Image
from home_page.bookinfo_page import FoundBook
from LibraryClasses.library import Library

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
        self.state('zoomed')

        self.frame()    # Frame Picture

        # Search Bar
        self.search_val = self.search_bar()    # Value extracted from search bar
        # Search Button
        self.search_button()
        # Discover most borrowed book section
        self.discover()
        # Borrowed books section
        self.borrowed()
        # Newest books section
        self.last_added()
        
        self.mainloop()

    def frame(self):
        img = ImageTk.PhotoImage(file='home_page/home.png')
        label = Label(self, image=img, bg='white')
        label.image = img
        label.place(x=0, y=0)

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
        pic = Image.open('home_page/search_button.png')
        photo = ImageTk.PhotoImage(pic)
        # Button Label
        button = Label(image=photo, cursor='hand', bg='#061A1D')
        button.image = photo
        button.place(x=1135, y=15)
        button.bind('<Button-1>', lambda event: self.search_book())

    def search_book(self):
        book = library.find_book(library.books, self.search_val.get().lower())
        # Window displaying data about book
        FoundBook(book, self.user)

    def discover(self):
        # Displays cover page abot most borrowed book
        lst = list(library.books)   # Converting set object to list
        book = lst[library.most_borrowed()]     # Index of book

        file = os.path.join('book_covers', book.file)
        img = ImageTk.PhotoImage(file=file)
        frame = Label(self, image=img, bg='#061A1D')
        frame.image = img
        frame.place(x=159, y=227)
        
        title_label = Label(self, text='Title', fg='white', bg='#0B3238', bd=0, font=('Roboto Slab', 13, 'bold'))
        title_label.place(x=430, y=275)
        
        title =  Label(self, text=book.title, fg='black', bg='#D9D9D9', bd=0, font=('Roboto Slab', 13, 'bold'))
        title.place(x=536, y=274)
        
        author_label = Label(self, text='Author', fg='white', bg='#0B3238', bd=0, font=('Roboto Slab', 13, 'bold'))
        author_label.place(x=424, y=332)
        
        author = Label(self, text=book.author, fg='black', bg='#D9D9D9', bd=0, font=('Roboto Slab', 13, 'bold'))
        author.place(x=534, y=332)
        
        
        borrowed_label = Label(self, text='Times Borrowed', fg='white', bg='#0B3238', bd=0, font=('Roboto Slab', 13, 'bold'))
        borrowed_label.place(x=398, y=396)
        
        borrowed =  Label(self, text=book.copies_borrowed, fg='black', bg='#D9D9D9', bd=0, font=('Roboto Slab', 14, 'bold'))
        borrowed.place(x=622, y=396)


    def borrowed(self):
        # Displaying data about borrowed books
        user = library.find_user(library.registered, self.user)


        for dct in library.active_loans[user.name]:
            value = list(dct.values())
           
            title_label = Label(self, text='Title', bg='#0B3238', fg='white', font=('Roboto Slab', 20, 'bold'))
            title_label.place(x=269, y=691)
            
            title = Label(self, text=value[0], bg='#D9D9D9', fg='black', font=('Roboto Slab', 20))
            title.place(x=401, y=691)

            borrowed_label = Label(self, text='Borrowed On', bg='#0B3238', fg='white', font=('Roboto Slab', 20, 'bold'))
            borrowed_label.place(x=230, y=774)
            
            borrowed = Label(self, text=value[1], bg='#D9D9D9', fg='black', font=('Roboto Slab', 20))
            borrowed.place(x=401, y=774)
            
            return_date_label = Label(self, text='Return Date', bg='#0B3238', fg='white', font=('Roboto Slab', 20, 'bold'))
            return_date_label.place(x=235, y=866)

            return_date = Label(self, text=value[2], bg='#D9D9D9', fg='black', font=('Roboto Slab', 20))
            return_date.place(x=401, y=866)

            button = Label(self, text='Return', bg='#073A42', fg='white', cursor='hand', font=('Roboto Slab', 20, 'bold'))
            button.place(x=435, y=941)
            button.bind('<Button-1>', lambda event: self.return_func(value[0]))

    def return_func(self, title):
        # Return book function from library class
        if library.return_book(self.user, title):
            Label(self, text='Book Returned.', bg='#061A1D', fg='white', font=('Roboto Slab', 15, 'bold')).place(x=591, y=945)
            

    def borrow_book(self, title):
        # Borrow book function from library class
        user = library.find_user(library.registered, self.user)
        library.borrow_book(library.books, user, title)
    
    def last_added(self):
        # Displaying cover of the newest books
        lst = list(library.books)
        book1 = lst[-1]
        book2 = lst[-2]

        Label(self, text=book1.title, bg='#D9D9D9', fg='black', font=('Roboto Slab', 20, 'bold')).place(x=1202, y=209)
        
        file1 = os.path.join('book_covers', book1.file)
        img1 = ImageTk.PhotoImage(file=file1)
        frame = Label(self, image=img1, bg='#061A1D')
        frame.image = img1
        frame.place(x=1261, y=265)
        
        button1 = Label(self, text='Borrow', bg='#073A42', fg='white', cursor='hand', font=('Roboto Slab', 20, 'bold'))
        button1.place(x=1313, y=543)
        button1.bind('<Button-1>', lambda event: self.borrow_book(book1.title))

        Label(self, text=book2.title, bg='#D9D9D9', fg='black', font=('Roboto Slab', 20, 'bold')).place(x=1202, y=650)
        file2 = os.path.join('book_covers', book2.file)
        img2 = ImageTk.PhotoImage(file=file2)
        frame = Label(self, image=img2, bg='#061A1D')
        frame.image = img2
        frame.place(x=1261, y=712)
        
        button2 = Label(self, text='Borrow', bg='#073A42', fg='white', cursor='hand', font=('Roboto Slab', 20, 'bold'))
        button2.place(x=1313, y=987)
        button2.bind('<Button-1>', lambda event: self.borrow_book(book2.title))
        
