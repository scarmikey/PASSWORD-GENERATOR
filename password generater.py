import random
import string
from tkinter import *

# Initialize the Tkinter window
root = Tk()
root.geometry("400x280")
root.title("Password Generator")

# Initial variables
title = StringVar()
choice = IntVar()
lengthlabel = StringVar()
passlength = IntVar()
symbols = "!§$%&/()=?{[]}*+'#~,;.:-_'<>"
poor = string.ascii_uppercase + string.ascii_lowercase
average = string.ascii_uppercase + string.ascii_lowercase + string.digits
advanced = poor + average + symbols
password = ""


# Functions
def selection():
    choice.get()


def passgen():
    global password
    password = ""
    if choice.get() == 1:
        password = ''.join(random.sample(poor, passlength.get()))
    elif choice.get() == 2:
        password = ''.join(random.sample(average, passlength.get()))
    elif choice.get() == 3:
        password = ''.join(random.sample(advanced, passlength.get()))
    label.config(text="Generated Password: " + password)


def copytoclipboard():
    global password
    print(password)
    root.clipboard_clear()
    root.clipboard_append(password)
    root.update()


# User interface
label = Label(root, textvariable=title)
label.pack()
title.set("Select password complexity:")

R1 = Radiobutton(root, text="Uppercase and Lowercase", variable=choice, value=1, command=selection)
R1.pack(anchor=CENTER)

R2 = Radiobutton(root, text="Uppercase, Lowercase, Digits", variable=choice, value=2, command=selection)
R2.pack(anchor=CENTER)

R3 = Radiobutton(root, text="Uppercase, Lowercase, Digits, Symbols", variable=choice, value=3, command=selection)
R3.pack(anchor=CENTER)

lengthlabel.set("Password length (8 to 24):")
lengthtitle = Label(root, textvariable=lengthlabel)
lengthtitle.pack()

spinboxlength = Spinbox(root, from_=8, textvariable=passlength, width=13)
spinboxlength.pack()

passgenButton = Button(root, text="Generate Password", command=passgen)
passgenButton.pack()

copyButton = Button(root, text="Copy Password to Clipboard", command=copytoclipboard)
copyButton.pack(side=BOTTOM)

root.mainloop()
