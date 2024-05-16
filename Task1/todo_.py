# todo.py
import sys

tasks = []

def show_menu():
    print("Todo App")
    print("1. Add task")
    print("2. Mark task as complete")
    print("3. Show tasks")
    print("4. Exit")

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added successfully!")

def mark_complete():
    if not tasks:
        print("No tasks to mark as complete.")
        return

    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

    index = int(input("Enter the task number to mark as complete: "))
    if index < 1 or index > len(tasks):
        print("Invalid task number.")
        return

    completed_task = tasks.pop(index - 1)
    print(f"Task '{completed_task}' marked as complete.")

def show_tasks():
    if not tasks:
        print("No tasks to show.")
        return

    print("Tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            mark_complete()
        elif choice == "3":
            show_tasks()
        elif choice == "4":
            print("Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
