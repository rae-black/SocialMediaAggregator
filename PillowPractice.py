import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry('600x400+50+50')
root.resizable(0, 0)
root.title("Social Media Aggregator")
label = Label(root)
label.pack()

img = PhotoImage(Image.open(
    'C:/Users/raybo/OneDrive/Documents/School/Comp 363/images/278820373_329184585948144_6669179164942239423_n.jpg'))
label.image = img
label.pack()

root.mainloop()
