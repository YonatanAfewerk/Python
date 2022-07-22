import tkinter
from tkinter import ttk
from tkinter.ttk import *
import MySQLdb as mdb
from tkinter import messagebox
import tkinter.font as font
import csv

def get_info():
    messagebox.showinfo('Made By','By Mini G')

def get_signin_stu(): 
    
    def get_sign_in():
        
        def sign_up():
            students = []
            
            f_name = f_entry.get() 
            s_name = s_entry.get()
            dob_ = dob_entry.get()
            dep = combo.get()
            prog_ = combo_2.get()
            user_ = user_entry.get()
            pass_ = pass_entry.get()
            
            students.append({
                'FirstName':f_name,
                'LastName':s_name,
                'DateofBirth':dob_,
                'department':dep,
                'program':prog_,
                'username':user_,
                'password':pass_ 
                })
            
            with open("SingedInStudents.csv", 'a') as file:
                writer = csv.DictWriter(file, fieldnames=['FirstName', 'LastName', 'DateofBirth','department','program', 'username','password']) 
                for row in students: 
                    writer.writerow({
                        "FirstName": row["FirstName"].title(),
                        "LastName": row["LastName"].title(),
                        "DateofBirth": row["DateofBirth"],
                        "department": row["department"],
                        "program": row["program"] ,
                        "username": row["username"],
                        "password": row["password"]
                        })
                
            
            print(students)
            
            
            # messagebox.showinfo("Error", "Program Still in Development.....")


        root = tkinter.Tk()
        root.title('Haramaya School of Engineering')
        root.configure(bg='light yellow')

                # set the geometry for the frame 
        root.geometry('600x600')
        root.resizable('False','False')
        
        menuBar= tkinter.Menu(root)
        root.config(menu = menuBar)

        help_menu = tkinter.Menu(menuBar, tearoff=0)
        menuBar.add_cascade(label='Back', menu = help_menu)
        help_menu.add_command(label='Back', command=root.destroy)




            # form title
        title = Label(root, text="Student Sign In" , font=('Liberation Sans',12)).place(x=50, y=50)

            # signin format
        f_name = Label(root, text='First Name').place(x=50, y=100)
        f_entry = ttk.Entry(root, font=('Liberation Sans',8),width=15)
        f_entry.place(x=130, y=100)

        s_name = Label(root, text='Last Name').place(x=250, y=100)
        s_entry = ttk.Entry(root, font=('Liberation Sans',8),width=15)
        s_entry.place(x=330, y=100)
            
        dob = Label(root, text='Date of Birth').place(x=50, y=130)
        dob_entry = ttk.Entry(root, font=('Liberation Sans',8),width=15)
        dob_entry.place(x=130, y=130)  
            
            # department
        combo = Combobox(root, width=20 , font=('Liberation Sans',8))
        c_label = Label(root, text='Departments').place(x=50,y=160)
        combo['values'] = ('Accounting','Management','Computer Science','Information Science','Software Engineering')
        combo.current(4)
        combo.place(x=130,y=160)    

            # program's
        combo_2 = Combobox(root, width=10 , font=('Liberation Sans',8))
        c_label_2 = Label(root, text='Program').place(x=50,y=190)
        combo_2['values'] = ('Extension','Regular')
        combo_2.current(1)
        combo_2.place(x=130,y=190)    

            # set username and password
        user_label = Label(root, text='Username',font=('Liberation Sans', 10)).place(x=50, y=220)
        user_entry= ttk.Entry(root,font=('Liberation Sans', 8),width=23)
        user_entry.place(x=130, y=220)

        pass_label = Label(root, text='Password' ,font=('Liberation Sans', 10)).place(x=50, y=250)
        pass_entry= ttk.Entry(root,font=('Liberation Sans', 8),width=23)
        pass_entry.place(x=130, y=250)


            # SingUp button

        sign_up = ttk.Button(root, text="Sign Up",command = sign_up ).place(x=350, y=280)
            
        root.mainloop()
    
    def get_value():
    
        if entry.get() == "" and entry_.get() == "":
            messagebox.showinfo("Error", "Empty Input!")
        else:
            u_text = entry.get()
            p_text = entry_.get()
            check_entry(u_text, p_text)
        
        

    def check_entry(user_, pass_):
        
        with open('SingedInStudents.csv') as file:
            reader = csv.DictReader(file)
            for row in reader:   
                user = row["username"]
                password = row["password"]
                if user == user_ and password == pass_:
                    break
                
            if user == user_ and password == pass_:
                Label(root, text= 'Connecting to database...', font= ('Century 15 bold', 7)).pack()
                connect_to_database(user, password)
            else:
                answer = messagebox.askyesnocancel("Error not Signed-In!", "Error! Connecting to Database...(Sign Up?)")
                if answer == True:
                    get_sign_in()
                else:
                    root.destroy
            

    def connect_to_database(user, password):
        
        try:
            db = mdb.connect('localhost', user, password)
            messagebox.showinfo("Status", "Connected Successfully!")
        except mdb.Error as e:
            messagebox.showinfo("Status", "Not Connected!")
            
        
        # create the instance of tkinter frame 
    root = tkinter.Tk()
    root.title('Haramaya School of Engineering')
    root.configure(bg='light yellow')

        # set the geometry for the frame 
    root.geometry('1100x500')
    root.resizable('False','False')
    
    menuBar= tkinter.Menu(root)
    root.config(menu = menuBar)

    help_menu = tkinter.Menu(menuBar, tearoff=0)
    menuBar.add_cascade(label='Back', menu = help_menu)
    help_menu.add_command(label='Back', command=root.destroy)


    label_1 = Label(root, text='Student Sign In',background='light yellow', font=('Liberation Sans bold', 10) )
    label_1.place(x=450, y=50)


        # create the Label object
    label_ = Label(root, text='Username',background='light yellow' ,font=('Liberation Sans', 10)).place(x=400, y=100)
        #Create an Entry Widget
    entry= ttk.Entry(root,font=('Liberation Sans', 8),width=30)
    entry.place(x=500, y=100)


    label_ = Label(root, text='Password',background='light yellow' ,font=('Liberation Sans', 10)).place(x=400, y=130)
    #Create an Entry Widget
    entry_= ttk.Entry(root,font=('Liberation Sans', 8),width=30)
    entry_.place(x=500, y=130)


        #Create a button to display the text of entry widget
    button= ttk.Button(root, text="Enter", command= get_value)
    button.place(x=510, y=160)
    
    
    button_= ttk.Button(root, text="Sign Up", command= get_sign_in)
    button_.place(x=590, y=160)
    
    

    combo = Combobox(root, width=20)
    label_ = Label(root, text='Departments',background='light yellow')
    label_.place(x=400, y=200)

    combo["values"] = ('Civil Engineering','Mechanical Engineering','Computer Science','Information Technology','Computer Engineering','Information Science','Software Engineering')
    combo.current(6)
    combo.place(x=500, y=200)
    
    
    root.mainloop()


def get_staff():
    
    def get_sign_in_2():
        def sign_up():
            staff = []
            
            f_name = f_entry.get() 
            s_name = s_entry.get()
            spn_ = spn_entry.get()
            dep = combo.get()
            prog_ = combo_2.get()
            user_ = user_entry.get()
            pass_ = pass_entry.get()
            
            staff.append({
                'FirstName':f_name,
                'LastName':s_name,
                'StaffPassNumber':spn_,
                'department':dep,
                'program':prog_,
                'username':user_,
                'password':pass_ 
                })
            
            for row in staff: 
                with open("SingedInStaffs.csv", 'a') as file:
                    writer = csv.DictWriter(file, fieldnames=['FirstName', 'LastName', 'StaffPassNumber','department','program', 'username','password']) 
                    writer.writerow({
                        "FirstName": row["FirstName"].title(),
                        "LastName": row["LastName"].title(),
                        "StaffPassNumber": row["StaffPassNumber"],
                        "department": row["department"],
                        "program": row["program"] ,
                        "username": row["username"],
                        "password": row["password"]
                        })  
            
            print(staff)
            


        root = tkinter.Tk()
        root.title('Haramaya School of Engineering')
        root.configure(bg='light gray')

                # set the geometry for the frame 
        root.geometry('600x600')
        root.resizable('False','False')
        
        menuBar= tkinter.Menu(root)
        root.config(menu = menuBar)

        help_menu = tkinter.Menu(menuBar, tearoff=0)
        menuBar.add_cascade(label='Back', menu = help_menu)
        help_menu.add_command(label='Back', command=root.destroy)


            # form title
        title = Label(root, text="Staff Sign In" , font=('Liberation Sans',12)).place(x=50, y=50)

            # signin format
        f_name = Label(root, text='First Name').place(x=50, y=100)
        f_entry = ttk.Entry(root, font=('Liberation Sans',8),width=15)
        f_entry.place(x=130, y=100)

        s_name = Label(root, text='Last Name').place(x=250, y=100)
        s_entry = ttk.Entry(root, font=('Liberation Sans',8),width=15)
        s_entry.place(x=330, y=100)
            
        spn = Label(root, text='Staff Pass Number').place(x=50, y=130)
        spn_entry = ttk.Entry(root, font=('Liberation Sans',8),width=15)
        spn_entry.place(x=160, y=130)  
            
            # department
        combo = Combobox(root, width=20 , font=('Liberation Sans',8))
        c_label = Label(root, text='Departments').place(x=50,y=160)
        combo['values'] = ('Accounting','Management','Computer Science','Information Science','Software Engineering')
        combo.current(4)
        combo.place(x=130,y=160)    

            # program's
        combo_2 = Combobox(root, width=10 , font=('Liberation Sans',8))
        c_label_2 = Label(root, text='Program').place(x=50,y=190)
        combo_2['values'] = ('Extension','Regular')
        combo_2.current(1)
        combo_2.place(x=130,y=190)    

            # set username and password
        user_label = Label(root, text='Username',font=('Liberation Sans', 10)).place(x=50, y=220)
        user_entry= ttk.Entry(root,font=('Liberation Sans', 8),width=23)
        user_entry.place(x=130, y=220)

        user_label = Label(root, text='Password' ,font=('Liberation Sans', 10)).place(x=50, y=250)
        pass_entry= ttk.Entry(root,font=('Liberation Sans', 8),width=23)
        pass_entry.place(x=130, y=250)


            # SingUp button

        sign_up = ttk.Button(root, text="Sign Up",command = sign_up ).place(x=350, y=280)
            
        root.mainloop()
    
    def get_value():
        if entry.get() == "" and entry_.get() == "":
            messagebox.showinfo("Error", "Empty Input!")
        else:
            u_text = entry.get()
            p_text = entry_.get()
            check_entry(u_text, p_text)
        
        

    def check_entry(user_, pass_):
        
        with open('SingedInStaffs.csv') as file:
            reader = csv.DictReader(file)
            for row in reader:   
                user = row["username"]
                password = row["password"]
                if user == user_ and password == pass_:
                    print(user, password)
                    break
                
            if user == user_ and password == pass_:
                Label(root, text= 'Connecting to database...', font= ('Century 15 bold', 7)).pack()
                connect_to_database(user, password)
            else:
                answer = messagebox.askyesnocancel("Error not Signed-In!", "Error! Connecting to Database...(Sign Up?)")
                if answer == True:
                    get_sign_in_2()
                else:
                    root.destroy

    def connect_to_database(user, password):
        
        try:
            db = mdb.connect('localhost', user, password)
            root.label.configure(text='Connected Successfully!')
        except mdb.Error as e:
            root.label.configure(text='Not Connected! Database Connection Failed!')
        
        # create the instance of tkinter frame 
    root = tkinter.Tk()
    root.title('Haramaya School of Engineering')
    root.configure(bg='light gray')

        # set the geometry for the frame 
    root.geometry('1100x500')
    root.resizable('False','False')
    
    menuBar= tkinter.Menu(root)
    root.config(menu = menuBar)

    help_menu = tkinter.Menu(menuBar, tearoff=0)
    menuBar.add_cascade(label='Back', menu = help_menu)
    help_menu.add_command(label='Back', command=root.destroy)


    label_1 = Label(root, text='Staff Sign In',background='light gray', font=('Liberation Sans bold', 10) )
    label_1.place(x=450, y=50)


        # create the Label object
    label_ = Label(root, text='Username',background='light gray' ,font=('Liberation Sans', 10)).place(x=400, y=100)
        #Create an Entry Widget
    entry= ttk.Entry(root,font=('Liberation Sans', 8),width=30)
    entry.place(x=500, y=100)


    label_ = Label(root, text='Password',background='light gray' ,font=('Liberation Sans', 10)).place(x=400, y=130)
    #Create an Entry Widget
    entry_= ttk.Entry(root,font=('Liberation Sans', 8),width=30)
    entry_.place(x=500, y=130)


        #Create a button to display the text of entry widget
    button= ttk.Button(root, text="Enter", command= get_value)
    button.place(x=510, y=160)
    
    
    button_= ttk.Button(root, text="Sign Up", command= get_sign_in_2)
    button_.place(x=590, y=160)
    
    
    root.mainloop()


    # create the instance of tkinter frame 
root = tkinter.Tk()
root.title('Haramaya School of Engineering')
root.configure(bg='light green')

    # Menu for about and exit
menuBar= tkinter.Menu(root)
root.config(menu = menuBar)

help_menu = tkinter.Menu(menuBar, tearoff=0)
menuBar.add_cascade(label='Help', menu = help_menu)
help_menu.add_command(label='About', command=get_info)
help_menu.add_command(label='Exit', command=root.destroy)




    # set the geometry for the frame 
root.geometry('1100x500')
root.resizable('False','False')

label_1 = Label(root, text='Library Management System',background='light green', font=('Liberation Sans bold', 30) )
label_1.place(x=300, y=100)

label_2 = Label(root, text='A simple project based on Library Management System that uses Python tkinter module for',background='light green', font=('Liberation Sans', 10) )
label_2.place(x=300, y=170)

label_3 = Label(root, text='GUI and MySql Database on the backend.',background='light green', font=('Liberation Sans', 10) )
label_3.place(x=430, y=185)


    #Create a button to display the text of entry widget
button= ttk.Button(root, text="Student", command= get_signin_stu)
button.place(x=470, y=250)

    #Create a button to display the text of entry widget
button_= ttk.Button(root, text="Staff", command= get_staff)
button_.place(x=570, y=250)


root.mainloop()
