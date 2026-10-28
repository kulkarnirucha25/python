from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Student Form")
root.geometry("300x250")

Label(root, text="Student Registration").pack()

Label(root, text="Name").pack()
name = Entry(root)
name.pack()

Label(root, text="Roll Number").pack()
roll = Entry(root)
roll.pack()

Label(root, text="Branch").pack()
branch = Entry(root)
branch.pack()


def submit():
    messagebox.showinfo(
        "Student Details",
        "Name: "
        + name.get()
        + "\nRoll No: "
        + roll.get()
        + "\nBranch: "
        + branch.get(),
    )


Button(root, text="Submit", command=submit).pack(pady=10)

root.mainloop()
