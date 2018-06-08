import tkinter 
import os
from getpass import getpass
from time import sleep
from selenium import webdriver


text1=str   
text2=str
fail=False
def clicked(*args):
    choice_var=choice.get()
    print(choice_var)
    text1=entry_usr.get()
    text2=entry_pwd.get()
    if choice_var== 1:
        facebook(text1,text2)
    elif choice_var==2:    
        twitter(text1,text2)
    else:
        print("Select app from given option and click Login button")
        check_input()


def check_input():
    if fail==True:
        return clicked()
    else:
        return None


def facebook(usr,pwd):
    cwd=os.getcwd()
    ok=os.path.join(cwd,'chromedriver.exe')
    driver=webdriver.Chrome(ok)
    driver.get("https://www.facebook.com/")
    print("Opened Facebook")
    sleep(1)

    username=driver.find_element_by_id('email')
    username.send_keys(usr)
    print("Username entered")
    sleep(1)

    password=driver.find_element_by_id('pass')
    password.send_keys(pwd) 
    print("Password entered")
    sleep(1)

    login_click=driver.find_element_by_id("loginbutton")
    login_click.click()


    print("All Done")
    driver.quit()
    print("Finished")
    

def twitter(usr,pwd):
    cwd=os.getcwd()
    ok=os.path.join(cwd,'chromedriver.exe')
    driver=webdriver.Chrome(ok)
    driver.get("https://twitter.com/login?lang=en")
    print("Opened Twitter")
    sleep(1)

    username=driver.find_element_by_class_name("js-username-field")
    username.send_keys(usr)
    print("Username entered")
    sleep(1)

    password=driver.find_element_by_class_name("js-password-field")
    password.send_keys(pwd) 
    print("Password entered")
    sleep(1)

    login_click=driver.find_element_by_class_name("EdgeButtom--medium")
    login_click.click()


    print("All Done")
    driver.quit()
    print("Finished")
    




     

















root=tkinter.Tk()
root.title("Login App")
root.geometry("400x400")
root.configure(background="snow")

label1=tkinter.Label(text="Enter details and select platform",fg="black",font=("TkMenuFont",10),bg="misty rose")
label1.grid(column=0,row=0,rowspan=2)

choice=tkinter.IntVar()


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