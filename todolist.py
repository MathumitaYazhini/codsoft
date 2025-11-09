to_do_list = []

def show_menu():
    print("\nTo-Do List Application")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        print("\nCurrent Tasks:")
        if not to_do_list:
            print("No tasks found.")
        else:
            for idx, task in enumerate(to_do_list):
                print(f"{idx+1}. {task}")
    elif choice == '2':
        task = input("Enter new task: ")
        to_do_list.append(task)
        print("Task added!")
    elif choice == '3':
        task_num = int(input("Enter task number to update: ")) - 1
        if 0 <= task_num < len(to_do_list):
            new_task = input("Enter new task description: ")
            to_do_list[task_num] = new_task
            print("Task updated!")
        else:
            print("Invalid task number.")
    elif choice == '4':
        task_num = int(input("Enter task number to delete: ")) - 1
        if 0 <= task_num < len(to_do_list):
            removed = to_do_list.pop(task_num)
            print(f"Task '{removed}' deleted!")
        else:
            print("Invalid task number.")
    elif choice == '5':
        print("Exiting To-Do List Application. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
