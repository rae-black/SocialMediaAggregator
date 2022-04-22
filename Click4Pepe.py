import tkinter as tk
from tkinter import ttk
from tkinter import *


# root window
root = Tk()
root.geometry('600x400+50+50')
root.resizable(0, 0)
root.title('Image Button Demo')


# download button

button_icon = tk.PhotoImage(file='C:/Users/raybo/OneDrive/Pictures/download.png')
pepe = PhotoImage(file='C:/Users/raybo/OneDrive/Pictures/1629868777073.png')

Button(
    root,
    image=button_icon,
    command=lambda: Label(image=pepe).pack(
        ipadx=5,
        ipady=5,
        expand=True
    )
).pack(
    ipadx=5,
    ipady=5,
    expand=True
)

root.mainloop()
