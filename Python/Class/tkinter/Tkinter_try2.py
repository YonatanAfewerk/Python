from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext as st
from tkinter import messagebox
from PIL import ImageTk, Image
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

class root(Tk):
    def __init__(self):
        super(root, self).__init__()
       # the tkinter design  
        self.title('Calculator v.0.0')
        self.minsize(500,400)
        
        self.create_browsing()
        

      # create a label
    
    def create_button(self):
        self.button = ttk.Button(self, text='Touch Me', command=self.message).grid(column=0, row=0)


    def create_frame(self): 
        pass  

root = root()
root.mainloop()