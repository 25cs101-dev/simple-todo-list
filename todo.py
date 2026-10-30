# Simple To-Do List
# A beginner-friendly console project using only basic Python

# This list stores all the tasks while the program is running
tasks = []


def show_menu():
    # Print the menu on the screen
    print("\n===== TO-DO LIST MENU =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")


def add_task():
    # Ask the user for a task and add it to the list
    task = input("Task: ")

    # Do not allow an empty task
    if task.strip() == "":
        print("Task cannot be empty.")
    else:
        tasks.append(task)
        print("Task added successfully!")


def view_tasks():
    # Show all tasks with numbers starting from 1
    if len(tasks) == 0:
        print("\nNo tasks yet. Add one first!")
    else:
        print("\n===== YOUR TASKS =====\n")
        number = 1
        for task in tasks:
            print(str(number) + ". " + task)
            number = number + 1


def delete_task():
    # Delete a task using its number
    if len(tasks) == 0:
        print("\nThere are no tasks to delete.")
        return

    view_tasks()
    task_number = input("\nEnter task number to delete: ")

    # Check that the user typed a number
    if task_number.isdigit():
        task_number = int(task_number)

        # Check that the number is inside the list
        if task_number >= 1 and task_number <= len(tasks):
            # Lists start at 0, so we subtract 1
            tasks.pop(task_number - 1)
            print("Task deleted successfully!")
        else:
            print("Invalid task number.")
    else:
        print("Please enter a valid number.")


# Main program: keeps running until the user chooses Exit
while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("Goodbye! Thanks for using Simple To-Do List.")
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3 or 4.")
