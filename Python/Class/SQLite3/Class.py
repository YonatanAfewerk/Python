from tkinter import *
from tkinter import ttk
import sqlite3
from tabulate import tabulate
import sys 


def tkinter():
    root = Tk()
    root.title(" Register ")
    root.geometry('400x350')

    # Title 
    title = ttk.Label(root, text="Registration", font=('arial BOLD', 16)).place(x=50, y=50)

    # Form
    f_name = ttk.Label(root, text="Full Name").place(x=50, y=100)
    in_name = ttk.Entry(root, width=25,font=('arial', 8))
    in_name.place(x=120,y=100)


    Email = ttk.Label(root, text="Email").place(x=50, y=135)
    in_email = ttk.Entry(root, width=25, font=('arial', 8))
    in_email.place(x=120,y=135)


    Age = ttk.Label(root, text="Age").place(x=50, y=170)
    in_age = ttk.Entry(root, width=10, font=('arial', 8))
    in_age.place(x=120,y=165)

    #Button
    btn = ttk.Button(root, text="Register", command=lambda: database(in_name.get(), in_email.get(), in_age.get()))
    btn.place(x=150,y=200)

    root.mainloop()


def database(name, email, age):
    conn = sqlite3.connect("Register.db")
    c = conn.cursor()

    user = [(name, email, age)]

    c.executemany('''
        INSERT INTO registered(Full_name, Email, Age)
        VALUES(?,?,?)''',user)    

    conn.commit()





tkinter()