import os
import argparse
import sys

# -a or --add to add tasks
# -l or --list to list all tasks
# -r or --remove to remove tasks using index
def my_parser():
    parser.argparser.ArgumentParser(description = "Todo list in command-line")
    parser.add_argument("-a", "--add", metavar="", help="Add a new task")
    parser.add_argument("-l", "--list", action="store_true", help="List all tasks")
    parser.add_argument("-r", "--remove", metavar="", help="Remove a task by index")
    return parser
def add_task(task):
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")
    
def list_tasks():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        for index, task in enumerate(tasks, start=1):
            print(f"{index}.{task.strip()}")
             #print(f"{index}. {task.strip()}")
    else:
        print("No tasks found.")    
def remove_task(index):
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        with open("tasks.txt", "w") as file:
            for i, task in enumerate(tasks, start=1):
                if i != index:
                    file.write(task)
        print("Task removed successfully.")
    else:
        print("No tasks found.")
def main():
    parser = my_parser()
    args = parser.parse_args()

    if args.add:
        add_task(args.add)
    elif args.list:
        list_tasks()
    elif args.remove:
        remove_task(int(args.remove))
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
