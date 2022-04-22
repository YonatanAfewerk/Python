import tkinter 
from tkinter import*

root = Tk()
root.title("Simple Calculator")
root.geometry("410x450+100+200")

root.resizable(False, False)
root.configure(bg="#121212")  #background color black



label_result = Label(root,width=16,height=2,text="",bg="#121212",font=("arial",30))
label_result.pack()


Button(root,text="CE", width=5, height=1, font=("arial",20),bd=1, fg="#fff",bg="#1c1c1c").place(x=11,y=110)
Button(root,text="C", width=5, height=1, font=("arial",20),bd=1, fg="#fff",bg="#1c1c1c").place(x=110,y=110)
Button(root,text="<", width=5, height=1, font=("arial",20),bd=1, fg="#fff",bg="#1c1c1c").place(x=210,y=110)
Button(root,text="/", width=5, height=1, font=("arial",20),bd=1, fg="#fff",bg="#1c1c1c").place(x=310,y=110)


Button(root,text="7", width=5, height=1, font=("arial",20),bd=1, fg="#fff",bg="#050505").place(x=11,y=178)
Button(root,text="8", width=5, height=1, font=("arial",20),bd=1, fg="#fff",bg="#050505").place(x=110,y=178)
Button(root,text="9", width=5, height=1, font=("arial",20),bd=1, fg="#fff",bg="#050505").place(x=210,y=178)
Button(root,text="x", width=5, height=1, font=("arial",20),bd=1, fg="#fff",bg="#1c1c1c").place(x=310,y=178)

Button(root,text="4", width=5, height=1, font=("arial",20),bd=1, fg="#fff",bg="#050505").place(x=11,y=248)
Button(root,text="5", width=5, height=1, font=("arial",20),bd=1, fg="#fff",bg="#050505").place(x=110,y=248)
Button(root,text="6", width=5, height=1, font=("arial",20),bd=1, fg="#fff",bg="#050505").place(x=210,y=248)
Button(root,text="-", width=5, height=1, font=("arial",20),bd=1, fg="#fff",bg="#1c1c1c").place(x=310,y=248)

Button(root,text="1", width=5, height=1, font=("arial",20),bd=1, fg="#fff",bg="#050505").place(x=11,y=318)
Button(root,text="2", width=5, height=1, font=("arial",20),bd=1, fg="#fff",bg="#050505").place(x=110,y=318)
Button(root,text="3", width=5, height=1, font=("arial",20),bd=1, fg="#fff",bg="#050505").place(x=210,y=318)
Button(root,text="+", width=5, height=1, font=("arial",20),bd=1, fg="#fff",bg="#1c1c1c").place(x=310,y=318)

Button(root,text="+/-", width=5, height=1, font=("arial",20),bd=1, fg="#fff",bg="#050505").place(x=11,y=388)
Button(root,text="0", width=5, height=1, font=("arial",20),bd=1, fg="#fff",bg="#050505").place(x=110,y=388)
Button(root,text=".", width=5, height=1, font=("arial",20),bd=1, fg="#fff",bg="#050505").place(x=210,y=388)
Button(root,text="=", width=5, height=1, font=("arial",20),bd=1, fg="#fff",bg="#4a728a").place(x=310,y=388)






root.mainloop()