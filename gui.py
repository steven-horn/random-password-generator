from tkinter import *
from functions import *


class Gui:
    def __init__(self, window):
        """Initial setup for the GUI. The screen will consist of a welcome label, a password length entry, a generate
        button, and an error message for inputting an incorrect password length."""

        self.window = window
        self.window.geometry('300x300')
        self.window.resizable(False, False)
        self.window.title('Random Password Generator')

        self.welcome_label = Label(text='Welcome to Password Generator!')
        self.welcome_label.pack()

        self.frame_length = Frame(self.window, highlightbackground='black', highlightthickness=1)
        self.length_label = Label(self.frame_length, text='Password Length:')
        self.length_entry = Entry(self.frame_length)
        self.length_label.pack(side='left')
        self.length_entry.pack(side='right')
        self.frame_length.pack()

        self.generate_button = Button(text='Generate', command=self.generate)
        self.generate_button.pack()

        self.password_label = Label(text='')
        self.password_label.pack()

        self.error_frame = Frame(self.window)
        self.error_label = Label(self.error_frame, text='Please enter a number between 8 and 32',
                                 fg='red', relief='groove')
        self.error_label.pack()
        self.error_frame.pack_forget()

    def generate(self):
        x = length(self.length_entry.get())
        if x is False:
            self.error_frame.pack()
            self.length_entry.delete(0, END)
        else:
            self.password_label.config(text=password_generator(x))
            self.password_label.pack()
            self.length_entry.delete(0, END)
            self.error_frame.pack_forget()
