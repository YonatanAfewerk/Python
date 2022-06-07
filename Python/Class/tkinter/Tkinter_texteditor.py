from tkinter import *
from tkinter import ttk


 # create the instance 

root = Tk()
root.geometry('1000x500')


menuBar = Menu(root)
root.config(menu = menuBar)

file_menu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='Exit', command=root.destroy)
file_menu.add_separator()

edit_menu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label='Edit', menu=edit_menu)
edit_menu.add_command(label='Exit', command=root.destroy)
edit_menu.add_separator()

format_menu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label='Format', menu=format_menu)
format_menu.add_command(label='Exit', command=root.destroy)
format_menu.add_separator()

view_menu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label='View', menu=view_menu)
view_menu.add_command(label='Exit', command=root.destroy)
view_menu.add_separator()

help_menu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label='Help', menu=help_menu)
help_menu.add_command(label='Exit', command=root.destroy)
help_menu.add_separator()



root.mainloop()