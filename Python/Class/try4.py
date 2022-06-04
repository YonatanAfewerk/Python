import tkinter
from tkinter import ttk
from tkinter.ttk import *
import MySQLdb as mdb
from tkinter import messagebox



def get_value():
    if entry.get() == "" and entry_.get() == "":
        messagebox.showinfo("Error", "Empty Input!")
    else:
        u_text = entry.get()
        p_text = entry_.get()
        check_entry(u_text, p_text)
    
    

def check_entry(user_, pass_):
    user = 'python'
    password = 'python'
    
    if user == user_ and password == pass_:
        Label(root, text= 'Connecting to database...', font= ('Century 15 bold', 7)).pack()
        connect_to_database(user, password)
    else:
       messagebox.showinfo("Error", "Error! Connecting to Database.....")
        

def connect_to_database(user, password):
    
    try:
        db = mdb.connect('localhost', user, password)
        root.label.configure(text='Connected Successfully!')
    except mdb.Error as e:
        root.label.configure(text='Not Connected!')
       
    # create the instance of tkinter frame 
root = tkinter.Tk()
root.title('Haramaya School of Engineering')

    # set the geometry for the frame 
root.geometry('1000x500')
root.resizable('False','False')


    # create the Label object
label_ = Label(root, text='Username').place(x=400, y=100)
    #Create an Entry Widget
entry= ttk.Entry(root,font=('Century 12', 10),width=30)
entry.place(x=500, y=100)


label_ = Label(root, text='Password').place(x=400, y=130)
 #Create an Entry Widget
entry_= ttk.Entry(root,font=('Century 12', 10),width=30)
entry_.place(x=500, y=130)


    #Create a button to display the text of entry widget
button= ttk.Button(root, text="Enter", command= get_value)
button.place(x=500, y=160)

combo = Combobox(root, width=20)
label_ = Label(root, text='Departments')
label_.place(x=400, y=200)

combo["values"] = ('Civil Engineering','Mechanical Engineering','Computer Science','Information Technology','Computer Engineering','Information Science','Software Engineering')
combo.current(6)
combo.place(x=500, y=200)

rad1 = Radiobutton(root, text='Student', value=1).place(x=400, y=250)
rad2 = Radiobutton(root, text='Staff', value=2).place(x=500 , y=250)
rad3 = Radiobutton(root, text='Admin', value=3).place(x=600 , y=250)


root.mainloop()
