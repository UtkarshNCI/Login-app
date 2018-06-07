import tkinter 
import os

root=tkinter.Tk()
root.title("Login App")
root.geometry("400x400")
root.configure(background="snow")

label1=tkinter.Label(text="Enter details and select platform",fg="black",font=("TkMenuFont",10),bg="misty rose")
label1.grid(column=0,row=0,rowspan=2)

rad1 = tkinter.Radiobutton(root,text='Facebook', value=1)
rad2 = tkinter.Radiobutton(root,text='Twitter', value=2)

 

rad1.grid(column=0, row=2)
rad2.grid(column=1, row=2)

 
label_usr=tkinter.Label(text="Username",fg="Black",font=("TkMenuFont",10),bg="misty rose")
label_usr.grid(column=0,row=3,sticky=tkinter.W)

entry_usr=tkinter.Entry()
entry_usr.grid(column=1,row=3)

label_pwd=tkinter.Label(text="Password",fg="Black",font=("TkMenuFont",10),bg="misty rose")
label_pwd.grid(column=0,row=4,sticky=tkinter.W)

entry_pwd=tkinter.Entry(show="*")
entry_pwd.grid(column=1,row=4)





root.mainloop()