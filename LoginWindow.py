import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# root window
root = tk.Tk()
root.geometry('300x150')
root.resizable(0, 0)
root.title('Sign In')

# store email address and password
email = tk.StringVar()
password = tk.StringVar()


def login_clicked():
    """callback when the login button clicked
    """
    msg = f'You entered email: {email.get()} and password: {password.get()}'
    showinfo(
        title='Information',
        message=msg
    )


# Sign in frame
signin = ttk.Frame(root).pack(padx=10, pady=10, fill='x', expand=True)

# email
ttk.Label(signin, text="Email Address: ").pack(fill='x', expand=True)

email_entry = ttk.Entry(signin, textvariable=email)
email_entry.pack(fill='x', expand=True)
email_entry.focus()

# password
ttk.Label(signin, text="Password:").pack(fill='x', expand=True)

ttk.Entry(signin, textvariable=password, show="*").pack(fill='x', expand=True)

# Login button
ttk.Button(signin, text="Login", command=login_clicked).pack(fill='x', expand=True, pady=10)


root.mainloop()
