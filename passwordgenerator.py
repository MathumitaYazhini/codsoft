import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = length_var.get()
    chars = ''
    if upper_var.get():
        chars += string.ascii_uppercase
    if lower_var.get():
        chars += string.ascii_lowercase
    if digits_var.get():
        chars += string.digits
    if symbols_var.get():
        chars += string.punctuation
    if not chars:
        messagebox.showerror("Error", "Select at least one character type.")
        return
    password = ''.join(random.choice(chars) for _ in range(length))
    password_var.set(password)

def copy_password():
    pwd = password_var.get()
    if pwd:
        root.clipboard_clear()
        root.clipboard_append(pwd)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showerror("Error", "No password to copy.")

root = tk.Tk()
root.title("Simple Password Generator")
root.geometry("400x340")

tk.Label(root, text="Password Length:").pack(pady=5)
length_var = tk.IntVar(value=12)
tk.Spinbox(root, from_=8, to=32, textvariable=length_var, width=10).pack()

tk.Label(root, text="Include:").pack(pady=6)
upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=False)
tk.Checkbutton(root, text="Uppercase", variable=upper_var).pack(anchor="w", padx=60)
tk.Checkbutton(root, text="Lowercase", variable=lower_var).pack(anchor="w", padx=60)
tk.Checkbutton(root, text="Digits", variable=digits_var).pack(anchor="w", padx=60)
tk.Checkbutton(root, text="Symbols", variable=symbols_var).pack(anchor="w", padx=60)

tk.Button(root, text="Generate Password", command=generate_password, width=20).pack(pady=15)
password_var = tk.StringVar()
tk.Entry(root, textvariable=password_var, font=("Arial", 14), justify="center").pack(fill='x', padx=30, ipady=5)
tk.Button(root, text="Copy to Clipboard", command=copy_password, width=20).pack(pady=10)

root.mainloop()


