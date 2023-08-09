tasks = []
time=[]
def add_task():
    task = input("Enter a new task: ")
    clock = input("Enter time: ")
    tasks.append(task)
    time.append(clock)
    print(f"Task: '{task}': '{time}' added successfully.")
def display_tasks():
    if len(tasks) == 0:
        print("No tasks in the list.")
    else:
        print("\nCurrent tasks:")
        for i, task in enumerate(tasks, start=1):
                 print(f"{i}. '{task}': '{time}'\n")
def remove_task():
    display_tasks()
    if len(tasks) > 0:
        task_number = int(input("Enter the number of the task to remove: "))
        if task_number > 0 and task_number <= len(tasks):
            task = tasks.pop(task_number-1)
            print(f"\nTask '{task}': '{time}' removed successfully.\n")
        else:
            print("\nInvalid task number.")
    else:
        print("No tasks in the list.")
def show_menu():
    print("1. Add Task")
    print("2. Display Tasks")
    print("3. Remove Task")
    print("4. Quit")
    choice = input("Enter your choice: ")
    return choice
while True:
    choice = show_menu()
    if choice == "1":
        add_task()
    elif choice == "2":
        display_tasks()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")












