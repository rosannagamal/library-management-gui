from tkinter import *
from PIL import ImageTk

# Library Class
from LibraryClasses.library import Library
library = Library()


class SignUpWindow(Toplevel):
         
    def __init__(self):
        Toplevel.__init__(self)
        
        # Frame 1
        self.title('Sign Up')
        self.geometry('446x432')
        self.config(bg='#061A1D')

        # Frame
        self.frame()
        
        # radio buttons for user privilege
        self.options = self.buttons()

        # User Data
        self.name = self.name_entry()
        self.email = self.email_entry()
        self.username = self.username_entry()
        self.password = self.password_entry()
        self.ssn = self.socialSec_num()
        self.mun = self.municipality_entry()
        
        # SignUp Button
        self.SignUp_button()

    def frame(self):
        # Frame Picture
        img = ImageTk.PhotoImage(file='SignUp/frametwo.png')
        label = Label(self, image=img, bg='#061A1D')
        label.image = img
        label.place(x=0, y=0)

    def buttons(self):
        var = StringVar()
        
        # normal user button
        Radiobutton(self, text = 'Normal User', variable=var, value = 1, bg='#07272C', bd=0, fg='white').place(x=52, y=48)
        # student button
        Radiobutton(self, text = 'Student', variable=var, value = 2, bg='#07272C', bd=0, fg='white').place(x=159, y=48)
        # librarian button
        Radiobutton(self, text = 'Librarian', variable=var, value = 3, bg='#07272C', bd=0, fg='white').place(x=241, y=48)
        # admin button
        Radiobutton(self, text = 'Admin', variable = var, value = 4, bg='#07272C', bd=0, fg='white').place(x=330, y=48)
        
        return var
    
    def name_entry(self):
        # Name Entry
        entry = Entry(self, bg='#061A1D', bd=0, width=12, highlightthickness=0, fg='white')
        var = entry     # Entry Value
        entry.insert(0, 'Name')
        entry.bind("<FocusIn>", lambda e: entry.delete(0, 'end'))
        entry.place(x=54, y=100)
        return var
        
    def email_entry(self):
        # Email Entry
        entry = Entry(self, bg='#061A1D', bd=0, width=13, highlightthickness=0, fg='white')
        var = entry     # Entry Value
        entry.insert(0, 'Email')
        entry.bind("<FocusIn>", lambda e: entry.delete(0, 'end'))
        entry.place(x=243, y=100)
        return var
       
    def username_entry(self):
        # Username Entry
        entry = Entry(self, bg='#061A1D', bd=0, width=12, highlightthickness=0, fg='white')
        var = entry     # Entry Value
        entry.insert(0, 'Username')
        entry.bind("<FocusIn>", lambda e: entry.delete(0, 'end'))
        entry.place(x=54, y=166)
        return var
        
    def password_entry(self):
        # Password Entry
        entry = Entry(self, bg='#061A1D', bd=0, width=12, highlightthickness=0, fg='white')
        var = entry     # Entry Value
        entry.insert(0, 'Password')
        entry.bind("<FocusIn>", lambda e: entry.delete(0, 'end'))
        entry.place(x=243, y=166)
        return var
        
    def socialSec_num(self):
        # Social Security Number Entry
        entry = Entry(self, bg='#061A1D', bd=0, width=16, highlightthickness=0, fg='white')
        var = entry     # Entry Value
        entry.insert(0, 'Social Security Number')
        entry.bind("<FocusIn>", lambda e: entry.delete(0, 'end'))
        entry.place(x=112, y=240)
        # label
        Label(self, text='* For users registering for National Libraries Only', font=('Inter', 10), bg='#061A1D', fg='white').place(x=103, y=202)
        return var
    
    def municipality_entry(self):
        # Municipality Entry
        entry = Entry(self, bg='#061A1D', bd=0, width=16, highlightthickness=0, fg='white')
        var = entry     # Entry Value
        entry.insert(0, 'Municipality')
        entry.bind("<FocusIn>", lambda e: entry.delete(0, 'end'))
        entry.place(x=112, y=313)
        # label
        Label(self, text='* For users registering  for Municipal Libraries Only', font=('Inter', 10), bg='#061A1D', fg='white').place(x=103, y=277)
        return var
        
    def SignUp_button(self):
        # SignUp Button
        button_label = Label(self, text='Sign Up', font=('Inter', 14, 'bold'), fg='white', bg='#0E3B42', cursor='hand')
        button_label.place(x=192, y=367)
        button_label.bind('<Button-1>', lambda event: self.create_acc())
    
    def create_acc(self):
        # Creating New Account
        library.add_user(int(self.options.get()), name=self.name.get(),
                         email=self.email.get(), username=self.username.get(),
                         password=self.password.get(), municipality=self.mun.get(),
                         social_sec_num=self.ssn.get())
        self.destroy()
