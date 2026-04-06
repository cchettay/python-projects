import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("To-Do List")
window.geometry("400x500")

# Function to add task


def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        label_status.config(text="Please enter a task!")

# Function to delete task


def delete_task():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected)
        label_status.config(text="Task deleted!")
    else:
        label_status.config(text="Please select a task!")


# Title label
label_title = tk.Label(window, text="My To-Do List", font=("Arial", 20))
label_title.pack(pady=10)

# Entry box
entry = tk.Entry(window, width=30, font=("Arial", 14))
entry.pack(pady=10)

# Add button
button_add = tk.Button(window, text="Add Task",
                       font=("Arial", 12), command=add_task)
button_add.pack(pady=5)

# Listbox to show tasks
listbox = tk.Listbox(window, width=40, height=10, font=("Arial", 12))
listbox.pack(pady=10)

# Delete button
button_delete = tk.Button(window, text="Delete Task",
                          font=("Arial", 12), command=delete_task)
button_delete.pack(pady=5)

# Status label
label_status = tk.Label(window, text="", font=("Arial", 10))
label_status.pack(pady=5)

# Keep window open
window.mainloop()
