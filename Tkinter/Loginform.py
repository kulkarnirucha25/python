from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Login Form")
root.geometry("300x200")

Label(root, text="Username").pack()
user = Entry(root)
user.pack()

Label(root, text="Password").pack()
pwd = Entry(root, show="*")
pwd.pack()


def login():
    if user.get() == "admin" and pwd.get() == "1234":
        messagebox.showinfo("Login", "Login Successful")
    else:
        messagebox.showerror("Login", "Invalid Details")


Button(root, text="Login", command=login).pack(pady=10)

root.mainloop()
