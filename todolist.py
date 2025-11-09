import json
import os
from datetime import datetime
import tkinter as tk
from tkinter import ttk, messagebox

FILENAME = "todo.json"

def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, 'r') as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(FILENAME, 'w') as f:
        json.dump(tasks, f, indent=4)

def add_task(description, priority, due_date):
    tasks = load_tasks()
    task = {
        "id": len(tasks) + 1,
        "description": description,
        "priority": priority,
        "due_date": due_date,
        "completed": False,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    tasks.append(task)
    save_tasks(tasks)

def update_task_ids(tasks):
    for idx, task in enumerate(tasks, 1):
        task["id"] = idx
    return tasks

def mark_complete(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
    save_tasks(tasks)

def delete_task(task_id):
    tasks = load_tasks()
    tasks = [task for task in tasks if task["id"] != task_id]
    tasks = update_task_ids(tasks)
    save_tasks(tasks)

def clear_completed():
    tasks = load_tasks()
    tasks = [task for task in tasks if not task["completed"]]
    tasks = update_task_ids(tasks)
    save_tasks(tasks)

def get_tasks(show_completed=False):
    tasks = load_tasks()
    if not show_completed:
        return [task for task in tasks if not task["completed"]]
    return tasks

def refresh(tree, show_completed_var):
    for item in tree.get_children():
        tree.delete(item)
    show_completed = bool(show_completed_var.get())
    for task in get_tasks(show_completed):
        status = "Completed" if task["completed"] else "Pending"
        tree.insert("", "end", values=(task["id"], task["description"],
                                       task["priority"], task["due_date"] or "", status))

def main():
    root = tk.Tk()
    root.title("Functional To-Do List")
    root.geometry("750x500")
    ui = {}

    add_frame = tk.LabelFrame(root, text="Add New Task")
    add_frame.pack(fill="x", padx=10, pady=5)
    tk.Label(add_frame, text="Description:").grid(row=0, column=0)
    ui['desc_entry'] = tk.Entry(add_frame, width=40)
    ui['desc_entry'].grid(row=0, column=1)
    tk.Label(add_frame, text="Priority:").grid(row=1, column=0)
    ui['priority'] = tk.StringVar(value="medium")
    tk.OptionMenu(add_frame, ui['priority'], "low", "medium", "high").grid(row=1, column=1)
    tk.Label(add_frame, text="Due Date (YYYY-MM-DD):").grid(row=2, column=0)
    ui['date_entry'] = tk.Entry(add_frame, width=20)
    ui['date_entry'].grid(row=2, column=1)
    tk.Button(add_frame, text="Add Task", command=
        lambda: (
            add_task(ui['desc_entry'].get(), ui['priority'].get(), ui['date_entry'].get() or None),
            ui['desc_entry'].delete(0, tk.END),
            ui['date_entry'].delete(0, tk.END),
            refresh(ui['tree'], ui['show_completed'])
        )
    ).grid(row=3, column=1, sticky="w", padx=5, pady=5)

    list_frame = tk.LabelFrame(root, text="Task List")
    list_frame.pack(fill="both", expand=True, padx=10, pady=5)
    columns = ("id", "description", "priority", "due_date", "status")
    ui['tree'] = ttk.Treeview(list_frame, columns=columns, show="headings")
    for col in columns:
        ui['tree'].heading(col, text=col.capitalize())
        ui['tree'].column(col, width=150)
    ui['tree'].pack(fill="both", expand=True)
    scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=ui['tree'].yview)
    ui['tree'].configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

    action_frame = tk.Frame(root)
    action_frame.pack(fill="x", padx=10, pady=5)
    tk.Button(action_frame, text="Mark Complete", command=
        lambda: (
            mark_complete(int(ui['tree'].item(ui['tree'].selection())["values"][0])) if ui['tree'].selection()
            else messagebox.showerror("Error", "Select a task!"),
            refresh(ui['tree'], ui['show_completed'])
        )
    ).pack(side="left", padx=5)
    tk.Button(action_frame, text="Delete Task", command=
        lambda: (
            delete_task(int(ui['tree'].item(ui['tree'].selection())["values"][0])) if ui['tree'].selection()
            else messagebox.showerror("Error", "Select a task!"),
            refresh(ui['tree'], ui['show_completed'])
        )
    ).pack(side="left", padx=5)
    tk.Button(action_frame, text="Clear Completed", command=lambda: (clear_completed(), refresh(ui['tree'], ui['show_completed']))).pack(side="left", padx=5)
    ui['show_completed'] = tk.IntVar()
    tk.Checkbutton(action_frame, text="Show Completed", variable=ui['show_completed'], command=lambda: refresh(ui['tree'], ui['show_completed'])).pack(side="right", padx=5)

    refresh(ui['tree'], ui['show_completed'])
    root.mainloop()

if __name__ == "__main__":
    main()
