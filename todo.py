# todo.py
import json
import os

class Task:
    def __init__(self, title, description, category, completed=False):
        self.title = title
        self.description = description
        self.category = category
        self.completed = completed

    def mark_completed(self):
        self.completed = True

    def to_dict(self):
        return {
            'title': self.title,
            'description': self.description,
            'category': self.category,
            'completed': self.completed
        }

class TodoApp:
    def __init__(self, filename='tasks.json'):
        self.filename = filename
        self.tasks = self.load_tasks()

    def add_task(self, title, description, category):
        task = Task(title, description, category)
        self.tasks.append(task)
        self.save_tasks()
        print(f"Task '{title}' added successfully!")

    def view_tasks(self, filter_category=None, show_completed=False):
        if not self.tasks:
            print("No tasks found.")
            return

        filtered_tasks = self.tasks
        if filter_category:
            filtered_tasks = [task for task in filtered_tasks if task.category.lower() == filter_category.lower()]
        
        if not show_completed:
            filtered_tasks = [task for task in filtered_tasks if not task.completed]

        if not filtered_tasks:
            print("No tasks match the specified filter.")
            return

        print("\n--- Tasks ---")
        for idx, task in enumerate(filtered_tasks, 1):
            status = "✓" if task.completed else " "
            print(f"{idx}. [{status}] {task.title} (Category: {task.category})")
            print(f"   Description: {task.description}\n")

    def mark_task_completed(self, task_index):
        if 0 < task_index <= len(self.tasks):
            self.tasks[task_index - 1].mark_completed()
            self.save_tasks()
            print("Task marked as completed!")
        else:
            print("Invalid task number.")

    def delete_task(self, task_index):
        if 0 < task_index <= len(self.tasks):
            deleted_task = self.tasks.pop(task_index - 1)
            self.save_tasks()
            print(f"Task '{deleted_task.title}' deleted successfully!")
        else:
            print("Invalid task number.")

    def save_tasks(self):
        with open(self.filename, 'w') as f:
            json.dump([task.to_dict() for task in self.tasks], f, indent=4)

    def load_tasks(self):
        try:
            with open(self.filename, 'r') as f:
                task_data = json.load(f)
                return [Task(**data) for data in task_data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

def main():
    app = TodoApp()

    while True:
        print("\n--- Personal To-Do List ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Completed")
        print("4. Delete Task")
        print("5. View Tasks by Category")
        print("6. View Completed Tasks")
        print("7. Exit")

        choice = input("Choose an option (1-7): ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            category = input("Enter task category (Work/Personal/Urgent): ")
            app.add_task(title, description, category)

        elif choice == '2':
            app.view_tasks()

        elif choice == '3':
            app.view_tasks()
            task_num = int(input("Enter the task number to mark as completed: "))
            app.mark_task_completed(task_num)

        elif choice == '4':
            app.view_tasks()
            task_num = int(input("Enter the task number to delete: "))
            app.delete_task(task_num)

        elif choice == '5':
            category = input("Enter category to filter (Work/Personal/Urgent): ")
            app.view_tasks(filter_category=category)

        elif choice == '6':
            app.view_tasks(show_completed=True)

        elif choice == '7':
            print("Thank you for using Personal To-Do List!")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()