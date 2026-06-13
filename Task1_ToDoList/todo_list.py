tasks = []

print("=== Welcome to My To-Do List ===")

while True:
    print("\nChoose an Option")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "2":
        if not tasks:
            print("Your task list is empty.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

    elif choice == "3":
        if not tasks:
            print("No tasks available to remove.")
        else:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

            remove = int(input("Enter task number to remove: "))
            if 1 <= remove <= len(tasks):
                deleted = tasks.pop(remove - 1)
                print(f"'{deleted}' removed successfully!")
            else:
                print("Invalid task number.")

    elif choice == "4":
        print("Thank you for using My To-Do List!")
        break

    else:
        print("Please enter a valid option.")