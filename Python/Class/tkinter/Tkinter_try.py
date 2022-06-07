from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkinter import messagebox


def get_reaction():
    first = entry_.get()
    first2 = entry_1.get()
    first3 = entry_2.get()
    
    Label(root, text=first).place(x=100,y=450)
    print(first, first2, first3)
    
def message(): 
    messagebox.showinfo('Tab name', 'Message') 

root = Tk()
root.title('Try')
root.geometry('1000x500')
root.resizable('False','False')
root.configure(bg='black')

label = Label(root, text='This is me trying to use place() layout manager', font=('Liberation Sans', 10))
label.place(x=350,y=200)

entry_ = ttk.Entry(root, font=('arial', 10), width=10)
entry_.place(x=500,y=400)
entry_1 = ttk.Entry(root, font=('arial', 10), width=10)
entry_1.place(x=580,y=400)
entry_2 = ttk.Entry(root, font=('arial', 10), width=10)
entry_2.place(x=660,y=400)


button = ttk.Button(root, text='Click', command=message).pack()




button = ttk.Button(root, text='Button', command=get_reaction).place(x=100,y=100)


combo = Combobox(root, width=15)
label_ = Label(root, text='Label').place(x=100,y=200)
combo['values']=(1,2,3,4,5,'Chose Number')
combo.current(5)
combo.place(x=150,y=200)

root.mainloop()