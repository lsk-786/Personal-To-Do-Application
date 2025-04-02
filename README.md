*Personal To-Do List Application*

*Overview*
This is a simple command-line Personal To-Do List application built with Python. It allows users to manage tasks by adding, viewing, marking as completed, and deleting tasks. Tasks are stored persistently in a JSON file.
Features

Add new tasks with title, description, and category
View all tasks
Mark tasks as completed
Delete tasks
Filter tasks by category
View completed tasks
Persistent storage using JSON

*Requirements*

Python 3.7+

*Installation*

Clone the repository
Ensure you have Python installed
Run the application using python todo.py

*Usage*
When you run the application, you'll see a menu with the following options:

Add Task: Create a new task with a title, description, and category
View Tasks: Display all current tasks
Mark Task Completed: Mark a specific task as done
Delete Task: Remove a task from the list
View Tasks by Category: Filter tasks by Work, Personal, or Urgent
View Completed Tasks: See all tasks that have been completed
Exit: Close the application

*Example Workflow*

Choose option 1 to add a task
Enter task details (title, description, category)
Use other options to manage your tasks
Tasks are automatically saved between sessions

*File Structure*

todo.py: Main application logic
tasks.json: Stores tasks between sessions


*License*
MIT License