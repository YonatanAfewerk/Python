# import all the required modules
import socket
import threading
from tkinter import *
from tkinter import font, ttk

from PIL import Image, ImageTk

PORT = 5050
SERVER = "192.168.1.103"
ADDRESS = (SERVER, PORT)
FORMAT = "utf-8"
	
# Create a new client socket
# and connect to the server
# client = socket.socket(socket.AF_INET,
# 					socket.SOCK_STREAM)
# client.connect(ADDRESS)


# GUI class for the chat
class GUI:
	# constructor method so that we can use self to easily 
 	# access all the instances defined with the class
	def __init__(self):

		# chat window which is currently hidden
		self.Window = Tk()
		self.Window.withdraw()

		# login window
		self.login = Toplevel()
		# set the title
		self.login.title("C-ተወያይ-hat")
		self.login.resizable('False','False')
		self.login.geometry('300x450')
		self.login.configure(bg='White')
  
		self.photo_ = PhotoImage(file = "message.png")
		self.Window.iconphoto(False, self.photo_)
		self.login.iconphoto(False, self.photo_)
		
		self.photo = PhotoImage(file = "Main Logo.png")
		self.logo = ttk.Label(self.login, 
                           image=self.photo,
                           background='white').place(x=65,y=25)

		# create a Label
		self.pls = ttk.Label(self.login, 
                           text='Enter Your Name',
                           background='white').place(x=105,y=250)
  
		self.fun = ttk.Label(self.login, 
                           text='መልእክተኛ ኃ.የተ.የግ.ማ © 2014',
                           font=('aril',7),
                           background='white').place(x=160,y=430)
  
		self.fun_ = ttk.Label(self.login, 
                           text='MessengerPlc@gmail.com',
                           font=('aril',7),
                           background='white').place(x=10,y=430)
  
		# create a entry box for
		# typing the message
		self.entryName = ttk.Entry(self.login, 
                           width = 25,
                           font = ('arial', 10))

		self.entryName.place(x=65,y=280)

		# set the focus of the cursor
		self.entryName.focus()

		# create a Continue Button
		# along with action
		self.go = ttk.Button(self.login, text='Continue', command=lambda: self.goAhead(self.entryName.get()))

		self.go.place(x=115, y=310)
  
		self.Window.mainloop()

	def goAhead(self, name):
		self.login.destroy()
		self.layout(name)

		# the thread to receive messages
		rcv = threading.Thread(target=self.receive)
		rcv.start()

	# The main layout of the chat
	def layout(self, name):

		self.name = name
		# to show chat window
		self.Window.deiconify()
		self.Window.title("C-ተወያይ-hat")  
		self.Window.geometry("315x550")  
		self.Window.resizable('False','False')  
		self.Window.configure(bg='white')
  
		self.labelHead = ttk.Label( self.Window,
                                    background="#17202A",
							        foreground="#EAECEE", 
                                    text=self.name).pack(side=TOP, anchor=NE)

		self.line = Label(self.Window,
						width=450,
						bg="#17202A").place(relwidth=1, rely=0.032, relheight=0.002)
        


		self.textCons = Text(self.Window,
							width=20,	
							bg="white",
							font=("aril", 8),
							padx=5,
							pady=5)

		self.textCons.place(x=0,y=20,relwidth=1, relheight=0.87)  

		self.labelBottom = Label(self.Window,
								bg="#17202A",
								height=80)

		self.labelBottom.place(relwidth=1, rely=0.9, relheight=0.002)

		self.entryMsg = ttk.Entry(self.Window, font=('arial',10), width=35)

		# place the given widget
		# into the gui window
		self.entryMsg.place(x=2, y=500)

		self.entryMsg.focus()

		# create a Send Button
		self.buttonMsg = ttk.Button(self.Window,
								text="Send",
								command=lambda: self.sendButton(self.entryMsg.get()))

		self.buttonMsg.place(x=238,y=498)

		self.textCons.config(cursor="arrow")

		# create a scroll bar
		scrollbar = Scrollbar(self.textCons)

		# place the scroll bar
		# into the gui window
		scrollbar.place(relheight=1,
						relx=0.974)

		scrollbar.config(command=self.textCons.yview)

		self.textCons.config(state=DISABLED)

	# function to basically start the thread for sending messages
	def sendButton(self, msg):
		self.textCons.config(state=DISABLED)
		self.msg = msg
		self.entryMsg.delete(0, END)
		snd = threading.Thread(target=self.sendMessage)
		snd.start()

	# function to receive messages
	def receive(self):
		while True:
			try:
				message = client.recv(1024).decode(FORMAT)

				# if the messages from the server is NAME send the client's name
				if message == 'NAME':
					client.send(self.name.encode(FORMAT))
				else:
					# insert messages to text box (cause we already set the state to DISABLED we need to set it to NORMAL before we insert data)
					self.textCons.config(state=NORMAL)
					self.textCons.insert(END,
										message+"\n")

					self.textCons.config(state=DISABLED)
					self.textCons.see(END)
			except:
				# an error will be printed on the command line or console if there's an error
				print("An error occurred!")
				client.close()
				break

	# function to send messages
	def sendMessage(self):
		self.textCons.config(state=DISABLED)
		while True:
			message = (f"{self.name}: {self.msg}")
			client.send(message.encode(FORMAT))
			break


# create a GUI class object
g = GUI()
