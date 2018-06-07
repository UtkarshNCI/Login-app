import tkinter 
import os
from getpass import getpass
from time import sleep
from selenium import webdriver

text1=str   
text2=str

def clicked(*args):
    fail=False
    text1=entry_usr.get()
    text2=entry_pwd.get()
    if choice== 1:
        facebook()
    elif choice==2:    
        twitter()
    else:
        print("Select app from given option and click Login button")
        fail=True

    if fail==True:
        return clicked()
    else:
        return None


def facebook():
    print("Facebook")

def twitter():
    print("Twitter")    




     

















root=tkinter.Tk()
root.title("Login App")
root.geometry("400x400")
root.configure(background="snow")

label1=tkinter.Label(text="Enter details and select platform",fg="black",font=("TkMenuFont",10),bg="misty rose")
label1.grid(column=0,row=0,rowspan=2)

choice=tkinter.IntVar

rad1 = tkinter.Radiobutton(root,text='Facebook', value=1,variable=choice)
rad2 = tkinter.Radiobutton(root,text='Twitter', value=2,variable=choice)

 

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

button_log=tkinter.Button(text="Login",command=clicked)
button_log.grid(column=1,row=5)

root.bind("button_log","<Button-1>",clicked)





root.mainloop()