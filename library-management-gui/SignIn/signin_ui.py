from tkinter import *
from PIL import ImageTk

# UI classes
from HomePage.home_ui import HomePage
from SignUp.signup_ui import SignUpWindow

# Library class
from library.library import Library
library = Library()


class SignInWindow(Tk):
    def __init__(self):
        super().__init__()

        # Frame 1
        self.title('Sign In')
        self.geometry('477x330')
        self.config(bg='#061A1D')

        # Frame picture
        self.frame = self.frame_picture()

        # Credentials
        self.username = self.username_entry()
        self.password = self.password_entry()

        # Link to SignUp Window
        self.signUp_link()

        # SignIn Button -> Home page
        self.button()

        self.mainloop()

    def frame_picture(self):
        # Frame Picture
        img = ImageTk.PhotoImage(file='/Users/rosannagamal/Documents/GitHub/library-management-gui/SignIn/frame.png')
        Label(self, image=img, bg='#061A1D').place(x=0, y=0)

    def username_entry(self):
        # Entry Box
        entry = Entry(self.frame, bg='#061A1D', bd=0, width=18, highlightthickness=0, fg='white')
        val = entry     # Value of Entry Box
        entry.place(x=157, y=148)
        entry.insert(0, 'Username')
        entry.bind("<FocusIn>", lambda e: entry.delete(0, 'end'))
        return val

    def password_entry(self):
        # Entry Box
        entry = Entry(self.frame, bg='#061A1D', bd=0, width=18, highlightthickness=0, fg='white')
        val = entry     # Value of Entry Box
        entry.place(x=157, y=202)
        entry.insert(0, 'Password')
        entry.bind("<FocusIn>", lambda e: entry.delete(0, 'end'))
        return val

    def authenticate(self):
        if library.authenticate(library.registered, self.username.get(), self.password.get()) :
            user = self.username.get()
            # Removing Sign In Window
            self.destroy()
            # Home Page Class
            HomePage(user)
        else:
            Label(self, text='The password you entered is incorrect. Try again', font=('Inter', 10, 'bold'),
                  bg='#061A1D', fg='#D93838').place(x=10, y=20)

    def button(self) :
        # Creating Label
        button_label = Label(self, text='Sign In', font=('Inter', 14, 'bold'), fg='white', bg='#0E3B42', cursor='hand')
        button_label.place(x=212, y=274)
        button_label.bind('<Button-1>', lambda event : self.authenticate())

    def signUp_link(self):
        # Label 'Not registered?'
        Label(self.frame, text='Not registered?', font=('Inter', 10), bg='#061A1D', fg='white').place(x=150, y=240)

        # 'Create an account' labe
        label_two = Label(self.frame, text='Create an account', font=('Inter', 10, 'bold'), fg='white', bg='#061A1D',
                          cursor='hand')
        label_two.place(x=230, y=240)

        # Binding button to label
        label_two.bind('<Button-1>', lambda event : SignUpWindow())


def main():
    signIn = SignInWindow()
    signIn.mainloop()
