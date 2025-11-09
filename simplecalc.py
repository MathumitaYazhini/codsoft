import tkinter as tk
from tkinter import messagebox

def perform_calculation(op):
    try:
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())
        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            if num2 == 0:
                messagebox.showerror("Error", "Division by zero!")
                return
            result = num1 / num2
        result_var.set(f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Only valid numbers are allowed")

def clear_all():
    num1_entry.delete(0, tk.END)
    num2_entry.delete(0, tk.END)
    result_var.set("")

root = tk.Tk()
root.title("Functional Calculator")
root.geometry("350x250")

tk.Label(root, text="First Number:").grid(row=0, column=0, pady=5, padx=10)
num1_entry = tk.Entry(root)
num1_entry.grid(row=0, column=1, pady=5)

tk.Label(root, text="Second Number:").grid(row=1, column=0, pady=5, padx=10)
num2_entry = tk.Entry(root)
num2_entry.grid(row=1, column=1, pady=5)

btn_frame = tk.Frame(root)
btn_frame.grid(row=2, column=0, columnspan=2, pady=10)

ops = [('+', 0), ('-', 1), ('*', 2), ('/', 3)]
for symbol, col in ops:
    tk.Button(btn_frame, text=symbol, width=5, 
              command=lambda op=symbol: perform_calculation(op)).grid(row=0, column=col, padx=5)

result_var = tk.StringVar()
tk.Label(root, textvariable=result_var, font=('Arial', 13)).grid(row=3, column=0, columnspan=2, pady=15)

tk.Button(root, text="Clear", command=clear_all).grid(row=4, column=0, columnspan=2, pady=8)

root.mainloop()
