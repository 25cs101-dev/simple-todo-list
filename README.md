# Simple To-Do List

## Project Description

Simple To-Do List is a beginner-friendly, console-based Python project. It lets you add tasks, view them, and delete them from a menu in the terminal. It is built using only basic Python.

## Features

- Add a new task
- View all tasks with numbers
- Delete a task by its number
- Simple menu that keeps running until you exit
- Basic checks for empty tasks and invalid numbers

## Technologies Used

- Python 3 (no external libraries)

## How to Run

1. Make sure Python 3 is installed on your computer.
2. Download or clone this project.
3. Open a terminal in the `simple-todo-list` folder.
4. Run:

```
python todo.py
```

On some computers you may need to use `python3 todo.py` instead.

## Example Usage

1. Choose `1` to add a task and type your task.
2. Choose `2` to see all your tasks.
3. Choose `3` and enter a task number to delete it.
4. Choose `4` to exit the program.

## Example Output

```
===== TO-DO LIST MENU =====
1. Add Task
2. View Tasks
3. Delete Task
4. Exit
Enter your choice (1-4): 1
Task: Complete Python assignment
Task added successfully!

===== TO-DO LIST MENU =====
1. Add Task
2. View Tasks
3. Delete Task
4. Exit
Enter your choice (1-4): 2

===== YOUR TASKS =====

1. Complete Python assignment
2. Study Java
3. Complete GitHub project

===== TO-DO LIST MENU =====
1. Add Task
2. View Tasks
3. Delete Task
4. Exit
Enter your choice (1-4): 3

===== YOUR TASKS =====

1. Complete Python assignment
2. Study Java
3. Complete GitHub project

Enter task number to delete: 2
Task deleted successfully!

===== TO-DO LIST MENU =====
1. Add Task
2. View Tasks
3. Delete Task
4. Exit
Enter your choice (1-4): 4
Goodbye! Thanks for using Simple To-Do List.
```

## Note

Tasks are stored only while the program is running. When you exit, the list is cleared.
