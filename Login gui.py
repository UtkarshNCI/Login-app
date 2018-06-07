import tkinter 
import os

root=tkinter.Tk()
root.title("Login App")
root.geometry("400x400")

label1=tkinter.Label(text="Enter details and select platform",fg="black",font=("Open Sans",10))
label1.grid(column=0,row=0)

label_usr=tkinter.Label(text="Username:",fg="Black",font=("Open Sans",10))
label_usr.grid(column=0,row=1,sticky=tkinter.W)

entry_usr=tkinter.Entry()
entry_usr.grid(column=1,row=1,sticky=tkinter.W)

label_pwd=tkinter.Label(text="Password:",fg="Black",font=("Open Sans",10))
label_pwd.grid(column=0,row=2,sticky=tkinter.W)

entry_pwd=tkinter.Entry(show="*")
entry_pwd.grid(column=1,row=2)





root.mainloop()