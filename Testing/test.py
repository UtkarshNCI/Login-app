import tkinter
choice=tkinter.IntVar()
root=tkinter.Tk()
root.title("Login App")
root.geometry("400x400")
root.configure(background="snow")

label1=tkinter.Label(text="Enter details and select platform",fg="black",font=("TkMenuFont",10),bg="misty rose")
label1.grid(column=0,row=0,rowspan=2)

choice.set(1)

rad1 = tkinter.Radiobutton(root,text='Facebook', value=1,variable=choice)
rad2 = tkinter.Radiobutton(root,text='Twitter', value=2,variable=choice)

root.mainloop()