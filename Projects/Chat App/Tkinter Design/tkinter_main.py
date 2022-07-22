<<<<<<< HEAD
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *


def sendButton():
    pass


root = Tk()
root.title('C-ተወያይ-hat!')
root.geometry('315x500')
root.resizable('False','False')


name = "Client's Name goes Here..."

    # to show chat root
root.title("C-ተወያይ-hat!")  
root.geometry("315x550")  
root.resizable('False','False')  
root.configure(bg='white')
  
  
labelHead = ttk.Label( root,background="#17202A",foreground="#EAECEE",text=name)
labelHead.pack(side=TOP, anchor=NE)

line = Label(root, width=450, background="#17202A")
line.place(relwidth=1, rely=0.032, relheight=0.002)
        


textCons = Text(root,width=20,bg="white",font=("aril", 10),padx=5,pady=5)
textCons.place(x=0,y=20,relwidth=1, relheight=0.87)  


labelBottom = Label(root, background="#17202A")
labelBottom.place(relwidth=1, rely=0.9, relheight=0.002)



entryMsg = ttk.Entry(root, font=('arial',10), width=35)
entryMsg.place(x=2, y=500)
entryMsg.focus()

    # create a Send Button
buttonMsg = ttk.Button(root,text="Send",command=lambda: sendButton(entryMsg.get()))
buttonMsg.place(x=238,y=498)


    # create a scroll bar
# textCons.config(cursor="arrow")
scrollbar = Scrollbar(textCons)

# place the scroll bar into the gui root

scrollbar.place(relheight=1,relx=0.974)
scrollbar.config(command=textCons.yview)
# textCons.config(state=DISABLED)


=======
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *


def sendButton():
    pass


root = Tk()
root.title('C-ተወያይ-hat!')
root.geometry('315x500')
root.resizable('False','False')


name = "Client's Name goes Here..."

    # to show chat root
root.title("C-ተወያይ-hat!")  
root.geometry("315x550")  
root.configure(bg='white')
  
  
labelHead = ttk.Label( root,background="#17202A",foreground="#EAECEE",text=name)
labelHead.pack(side=TOP, anchor=NE)

line = Label(root, width=450, background="#17202A")
line.place(relwidth=1, rely=0.032, relheight=0.002)
        


textCons = Text(root,width=20,bg="white",font=("aril", 10),padx=5,pady=5)
textCons.place(x=0,y=20,relwidth=1, relheight=0.87)  


labelBottom = Label(root, background="#17202A")
labelBottom.place(relwidth=1, rely=0.9, relheight=0.002)



entryMsg = ttk.Entry(root, font=('arial',10), width=35)
entryMsg.place(x=2, y=500)
entryMsg.focus()

    # create a Send Button
buttonMsg = ttk.Button(root,text="Send",command=lambda: sendButton(entryMsg.get()))
buttonMsg.place(x=238,y=498)


    # create a scroll bar
# textCons.config(cursor="arrow")
scrollbar = Scrollbar(textCons)

# place the scroll bar into the gui root

scrollbar.place(relheight=1,relx=0.974)
scrollbar.config(command=textCons.yview)
# textCons.config(state=DISABLED)


>>>>>>> 8c662f6f97e0d64e5265aea18fd90c4cf7969d3d
root.mainloop()