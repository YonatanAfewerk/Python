from tkinter import *
from tkinter import ttk


 # create the instance 

root = Tk()
root.geometry('1000x500')
root.title('NotePad Copy')


menuBar = Menu(root)
root.config(menu = menuBar)

file_menu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='New')
file_menu.add_command(label='New Window')
file_menu.add_command(label='Open...')
file_menu.add_command(label='Save')
file_menu.add_command(label='Save as...')
file_menu.add_separator()
file_menu.add_command(label='Page Setup...')
file_menu.add_command(label='Print...')
file_menu.add_separator()
file_menu.add_command(label='Exit', command=root.destroy)

edit_menu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label='Edit', menu=edit_menu)
edit_menu.add_command(label='Undo', command=root.destroy)
edit_menu.add_separator()
edit_menu.add_command(label='Cut')
edit_menu.add_command(label='Copy')
edit_menu.add_command(label='Paste')
edit_menu.add_command(label='Delete')



format_menu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label='Format', menu=format_menu)
format_menu.add_command(label='Word wrap')
format_menu.add_command(label='Font...')


view_menu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label='View', menu=view_menu)
view_menu.add_command(label='Zoom')
view_menu.add_command(label='Status Bar')

help_menu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label='Help', menu=help_menu)
help_menu.add_command(label='View Help')
help_menu.add_command(label='Send Feedback')
help_menu.add_separator()
help_menu.add_command(label='About NotePad')




root.mainloop()