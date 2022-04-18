from tkinter import *

root = Tk()
root.title("Private User Login")
root.geometry("400x400")
root.configure(background="LightSkyBlue1")

label_name = Label(root, text="Name:", bg="LightSkyBlue1")
label_name.place(relx=0.3, rely=0.1, anchor=CENTER)

label_password = Label(root, text="Password:", bg="LightSkyBlue1")
label_password.place(relx=0.3, rely=0.2, anchor=CENTER)

label_captcha = Label(root, text="Captcha:", bg="LightSkyBlue1")
label_captcha.place(relx=0.3, rely=0.3, anchor=CENTER)

input_name = Entry(root)
input_name.place(relx=0.55, rely=0.1, anchor=CENTER)

input_password = Entry(root)
input_password.place(relx=0.55, rely=0.2, anchor=CENTER)

input_captcha = Entry(root)
input_captcha.place(relx=0.55, rely=0.3, anchor=CENTER)

show_username = Label(root, bg="LightSkyBlue1")
show_username.place(relx=0.5, rely=0.7, anchor=CENTER)

show_password = Label(root, bg="LightSkyBlue1")
show_password.place(relx=0.5, rely=0.8, anchor=CENTER)

show_captcha = Label(root, bg="LightSkyBlue1")
show_captcha.place(relx=0.5, rely=0.9, anchor=CENTER)

class UserDB:
    def __init__(self):
        self.__username = "James123"
        self.__password = "J11"
        self.captcha = "Wa3"
    
    def ShowUser(self):
        show_username["text"] = "Username: " + self.__username
        show_password["text"] = "Password: " + self.__password
        show_captcha["text"] = "Captcha: " + self.captcha

obj = UserDB

def AddUser(self):
    global obj
    obj.username = input_name.get()
    obj.password = input_password.get()
    obj.captcha = input_captcha.get()
    print("Details have been updated")

button_update = Button(root, text="Update Details", bg="gold", command=obj.ShowUser)
button_update.place(relx=0.3, rely=0.5, anchor=CENTER)

button_show = Button(root, text="Show Details", bg="gold", command=AddUser)
button_show.place(relx=0.7, rely=0.5, anchor=CENTER)

root.mainloop()