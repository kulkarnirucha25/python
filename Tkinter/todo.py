from tkinter import *

root = Tk()
root.title("To-Do List")
root.geometry("300x300")

task = Entry(root)
task.pack(pady=10)

tasks = Listbox(root)
tasks.pack()


def add_task():
    if task.get():
        tasks.insert(END, task.get())
        task.delete(0, END)


def delete_task():
    selected = tasks.curselection()
    if selected:
        tasks.delete(selected[0])


Button(root, text="Add Task", command=add_task).pack(pady=5)
Button(root, text="Delete Task", command=delete_task).pack()

root.mainloop()
