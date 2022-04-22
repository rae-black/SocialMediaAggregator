import tkinter as tk
from tkinter import ttk

root = tk.Tk()

# set window title
root.title('Tkinter Window Demo')

window_width = 600
window_height = 400

# # center window on the screen
# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

#

# specify if window is resizable (width, height)
root.resizable(0, 0)

# specify minimum and maximum size (width, height
root.minsize(400, 200)
root.maxsize(800, 600)

# place a label on the root window
tk.Label(root, text="Classic Label").pack()

# place a themed label on root window
ttk.Label(root, text='Themed Label').pack()

# set transparency (0.0-1.0)
# root.attributes('-alpha', 0.5)

# # window stacking order
# place root window on top of all other windows
root.attributes('-topmost', 1)

# # change default icon to new one
root.iconbitmap('C:/Users/raybo/OneDrive/Pictures/pythontutorial-1-150x150.ico')

# add button
def callback():
    # do something
    # if one expression, forego function definition in favor of lambda expression

ttk.Button(root, text="Demo Button", command=callback)

# set disabled flag on button
button.state(['disabled'])

# remove disabled flag on button
button.state(['!disabled'])

# keep the window displaying
root.mainloop()