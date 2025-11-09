import tkinter as tk
from tkinter import ttk, messagebox
import json
import os

DATA_FILE = "contacts.json"

def load_contacts():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_contacts(contacts):
    with open(DATA_FILE, "w") as f:
        json.dump(contacts, f, indent=2)

def update_contact_list(tree, contacts):
    tree.delete(*tree.get_children())
    for contact in contacts:
        tree.insert('', 'end', values=(contact['name'], contact['phone']))

def display_contact_details(event):
    selected = contact_tree.selection()
    if selected:
        index = contact_tree.index(selected[0])
        contact = contacts[index]
        for field, var in entry_vars.items():
            var.set(contact.get(field, ""))

def add_contact():
    contact = {field: var.get().strip() for field, var in entry_vars.items()}
    if not contact['name']:
        messagebox.showerror("Error", "Name is required!")
        return
    contacts.append(contact)
    save_contacts(contacts)
    update_contact_list(contact_tree, contacts)
    clear_form()
    messagebox.showinfo("Success", "Contact added successfully!")

def update_contact():
    selected = contact_tree.selection()
    if not selected:
        messagebox.showerror("Error", "Please select a contact to update!")
        return
    index = contact_tree.index(selected[0])
    contact = {field: var.get().strip() for field, var in entry_vars.items()}
    if not contact['name']:
        messagebox.showerror("Error", "Name is required!")
        return
    contacts[index] = contact
    save_contacts(contacts)
    update_contact_list(contact_tree, contacts)
    messagebox.showinfo("Success", "Contact updated successfully!")

def delete_contact():
    selected = contact_tree.selection()
    if not selected:
        messagebox.showerror("Error", "Please select a contact to delete!")
        return
    if messagebox.askyesno("Confirm", "Delete this contact?"):
        index = contact_tree.index(selected[0])
        del contacts[index]
        save_contacts(contacts)
        update_contact_list(contact_tree, contacts)
        clear_form()
        messagebox.showinfo("Success", "Contact deleted successfully!")

def search_contact():
    query = search_var.get().lower()
    if not query:
        update_contact_list(contact_tree, contacts)
        return
    results = []
    for contact in contacts:
        if query in contact['name'].lower() or query in contact['phone'].lower():
            results.append(contact)
    update_contact_list(contact_tree, results)

def clear_form():
    for var in entry_vars.values():
        var.set('')

root = tk.Tk()
root.title("Simple Contact Book")
root.geometry("820x500")

contacts = load_contacts()
entry_vars = {}
labels = ['Name', 'Phone', 'Email', 'Address']

main_frame = tk.Frame(root)
main_frame.pack(fill='both', expand=True, padx=10, pady=10)

# List Frame
list_frame = tk.Frame(main_frame)
list_frame.pack(side='left', fill='y', padx=(0, 10))
tk.Label(list_frame, text="Contacts", font=('Arial', 14, 'bold')).pack(pady=7)
contact_tree = ttk.Treeview(list_frame, columns=('name', 'phone'), show='headings', height=18)
contact_tree.heading('name', text='Name')
contact_tree.heading('phone', text='Phone')
contact_tree.column('name', width=110)
contact_tree.column('phone', width=110)
contact_tree.pack(padx=5, pady=5)
contact_tree.bind('<<TreeviewSelect>>', display_contact_details)
scrollbar = ttk.Scrollbar(list_frame, orient='vertical', command=contact_tree.yview)
contact_tree.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side='right', fill='y')

# Details Frame
detail_frame = tk.Frame(main_frame)
detail_frame.pack(side='right', fill='both', expand=True)

search_var = tk.StringVar()
tk.Entry(detail_frame, textvariable=search_var, font=('Arial', 11), width=25).pack(side='left', padx=(0, 5), pady=7)
tk.Button(detail_frame, text="Search", command=search_contact).pack(side='left', pady=7)

form_frame = tk.LabelFrame(detail_frame, text="Contact Details", font=('Arial', 12, 'bold'))
form_frame.pack(fill='x', padx=7, pady=18)
for i, label in enumerate(labels):
    tk.Label(form_frame, text=label+":").grid(row=i, column=0, sticky='e', padx=6, pady=5)
    entry_vars[label.lower()] = tk.StringVar()
    tk.Entry(form_frame, textvariable=entry_vars[label.lower()], width=26).grid(row=i, column=1, sticky='w', padx=6, pady=5)

button_frame = tk.Frame(detail_frame)
button_frame.pack(fill='x', pady=12)
tk.Button(button_frame, text="Add", command=add_contact, width=12).pack(side='left', padx=3)
tk.Button(button_frame, text="Update", command=update_contact, width=12).pack(side='left', padx=3)
tk.Button(button_frame, text="Delete", command=delete_contact, width=12).pack(side='left', padx=3)
tk.Button(button_frame, text="Clear", command=clear_form, width=12).pack(side='left', padx=3)

update_contact_list(contact_tree, contacts)
root.mainloop()
