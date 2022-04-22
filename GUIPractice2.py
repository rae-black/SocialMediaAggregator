import tkinter as tk
from tkinter import ttk

# root window
root = tk.Tk()
root.title('GUIPractice2')

window_width = 600
window_height = 400

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)

root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

demo_button_label = ttk.Label(root, text='Congrats, you pressed the demo button')

# demo button
demo_button = ttk.Button(
    root,
    text="Demo button",
    command=lambda: demo_button_label.pack()
)
demo_button.pack()

# exit button
exit_button = ttk.Button(
    root,
    text="Close this shit",
    command=lambda: root.quit()
)
exit_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

root.mainloop()
