
# todo.py — simple terminal To-Do app (Python 3)
# This program lets you add, view, complete, and remove tasks.
# It also saves tasks to a file (todo.json) so you don’t lose them.

import json   # for saving and loading tasks in JSON format
import os     # to check if the file already exists

# File name where tasks will be stored
FILE = "todo.json"

# ---------------- FUNCTIONS ---------------- #


def load_tasks():
    """
    Load tasks from todo.json if it exists, otherwise return an empty list.
    """
    if os.path.exists(FILE):  # check if file exists
        try:
            with open(FILE, "r") as f:
                return json.load(f)  # read tasks from the file
        except Exception:
            return []  # if file is empty or broken, start fresh
    return []  # no file = no tasks yet


def save_tasks(tasks):
    """
    Save the list of tasks into todo.json (in JSON format).
    """
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=2)  # indent=2 makes it pretty


def list_tasks(tasks):
    """
    Show all tasks with numbers and [ ] or [x] to indicate status.
    """
    if not tasks:
        print("\nNo tasks yet.\n")
        return
    print()
    for i, t in enumerate(tasks, start=1):  # enumerate gives index + task
        status = "[x]" if t.get("done") else "[ ]"  # done? show x
        print(f"{i}. {status} {t.get('task')}")  # show number + status + text
    print()


def add_task(tasks):
    """
    Ask user to type a new task, then add it to the list.
    """
    text = input("Enter a new task: ").strip()  # strip removes extra spaces
    if text:
        tasks.append({"task": text, "done": False})  # new task is not done
        save_tasks(tasks)  # save after adding
        print('Task added.\n')
    else:
        print("No text entered. Task not added.\n")


def mark_done(tasks):
    """
    Let user choose a task number to mark as completed.
    """
    if not tasks:
        print("No tasks to mark.\n")
        return
    list_tasks(tasks)  # show tasks first
    try:
        idx = int(input("Enter task number to mark done: "))
        if 1 <= idx <= len(tasks):  # valid number
            tasks[idx-1]["done"] = True  # mark as done
            save_tasks(tasks)
            print("Task marked done.\n")
        else:
            print("Invalid number.\n")
    except ValueError:
        print("Please enter a valid number.\n")


def remove_task(tasks):
    """
    Let user choose a task number to remove completely.
    """
    if not tasks:
        print("No tasks to remove.\n")
        return
    list_tasks(tasks)
    try:
        idx = int(input("Enter task number to remove: "))
        if 1 <= idx <= len(tasks):
            removed = tasks.pop(idx-1)  # remove by index
            save_tasks(tasks)
            print(f"Removed: {removed.get('task')}\n")
        else:
            print("Invalid number.\n")
    except ValueError:
        print("Please enter a valid number.\n")


def clear_completed(tasks):
    """
    Remove all tasks that are already marked done.
    """
    before = len(tasks)  # count before
    tasks[:] = [t for t in tasks if not t.get("done")]  # keep only not done
    if len(tasks) != before:
        save_tasks(tasks)
        print("Cleared completed tasks.\n")
    else:
        print("No completed tasks to clear.\n")


def menu():
    """
    Main loop — shows menu, asks user for choice, calls functions.
    """
    tasks = load_tasks()  # start by loading saved tasks
    while True:
        # Show options
        print("=== Simple To-Do App ===")
        print("1. View tasks")
        print("2. Add task")
        print("3. Mark task done")
        print("4. Remove task")
        print("5. Clear completed tasks")
        print("0. Exit")
        choice = input("Choose an option: ").strip()

        # Handle choice
        if choice == "1":
            list_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            remove_task(tasks)
        elif choice == "5":
            clear_completed(tasks)
        elif choice == "0":
            print("Goodbye — your tasks are saved.")
            break  # exit loop = exit program
        else:
            print("Invalid choice, try again.\n")


# ---------------- MAIN ---------------- #

# Only run menu if this file is executed directly
if __name__ == "__main__":
    menu()
()
