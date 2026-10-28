from tkinter import *

root = Tk()
root.title("Simple Calculator")
root.geometry("300x300")

Label(root, text="First Number").pack()
e1 = Entry(root)
e1.pack()

Label(root, text="Second Number").pack()
e2 = Entry(root)
e2.pack()

result = Label(root, text="Result: ")
result.pack(pady=10)


def calculate(op):
    a = float(e1.get())
    b = float(e2.get())

    if op == "+":
        c = a + b
    elif op == "-":
        c = a - b
    elif op == "*":
        c = a * b
    elif op == "/":
        if b == 0:
            result.config(text="Cannot divide by zero")
            return
        c = a / b

    result.config(text="Result: " + str(c))


Button(root, text="Add", command=lambda: calculate("+")).pack()
Button(root, text="Subtract", command=lambda: calculate("-")).pack()
Button(root, text="Multiply", command=lambda: calculate("*")).pack()
Button(root, text="Divide", command=lambda: calculate("/")).pack()

root.mainloop()
