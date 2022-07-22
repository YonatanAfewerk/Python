from tkinter import *
from tkinter import ttk


 # create the instance 

root = Tk()
root.geometry('1000x500')
root.resizable('False','False')


tab_control = ttk.Notebook(root)
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text = 'Sign Up')

tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text = 'Log In')

tab_control.pack(expand=1, fill=BOTH)



FirstFrame = ttk.Labelframe(tab1, text='Sign Up')
FirstFrame.grid(column=0, row=0, padx=20, pady=40)

ttk.Label(FirstFrame, text='First Name').grid(column=0, row=0)
ttk.Entry(FirstFrame, font=('times', 10)).grid(column=1, row=0)
ttk.Label(FirstFrame, text='Last Name').grid(column=0, row=1)
ttk.Entry(FirstFrame, font=('times', 10)).grid(column=1, row=1)

ttk.Label(FirstFrame, text='UserName').grid(column=0, row=2)
ttk.Entry(FirstFrame, font=('times', 10)).grid(column=1, row=2)
ttk.Label(FirstFrame, text='Password').grid(column=0, row=3)
ttk.Entry(FirstFrame, font=('times', 10)).grid(column=1, row=3)

ttk.Button(FirstFrame, text='Sign Up').grid(column=1, row=4)


FirstFrame_ = ttk.Labelframe(tab2, text='Log In')
FirstFrame_.grid(column=0, row=0, padx=20, pady=40)

ttk.Label(FirstFrame_, text='User Name').grid(column=0, row=0)
ttk.Entry(FirstFrame_, font=('times', 10)).grid(column=1, row=0)
ttk.Label(FirstFrame_, text='Password').grid(column=0, row=1)
ttk.Entry(FirstFrame_, font=('times', 10)).grid(column=1, row=1)

ttk.Button(FirstFrame_, text='Log In').grid(column=1, row=2)




root.mainloop()