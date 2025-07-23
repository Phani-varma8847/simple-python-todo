import os

# Define the file where tasks will be stored
TASKS_FILE = 'tasks.txt'

def load_tasks():
    """Loads tasks from the tasks.txt file."""
    tasks = []
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as f:
            for line in f:
                # Each line is expected to be in "status|task_description" format
                parts = line.strip().split('|')
                if len(parts) == 2:
                    status = parts[0] == 'True' # Convert string 'True'/'False' to boolean
                    description = parts[1]
                    tasks.append({'description': description, 'completed': status})
                else:
                    print(f"Warning: Skipping malformed line in {TASKS_FILE}: {line.strip()}")
    return tasks

def save_tasks(tasks):
    """Saves the current list of tasks to the tasks.txt file."""
    with open(TASKS_FILE, 'w') as f:
        for task in tasks:
            # Write tasks in "status|task_description" format
            f.write(f"{task['completed']}|{task['description']}\n")
    print("Tasks saved successfully!")

def display_tasks(tasks):
    """Displays all tasks with their status."""
    if not tasks:
        print("\nYour to-do list is empty! Add some tasks.\n")
        return

    print("\n--- Your To-Do List ---")
    for i, task in enumerate(tasks):
        status = "✓" if task['completed'] else " "
        print(f"{i + 1}. [{status}] {task['description']}")
    print("---------------------\n")

def add_task(tasks):
    """Adds a new task to the list."""
    description = input("Enter the new task description: ").strip()
    if description:
        tasks.append({'description': description, 'completed': False})
        print(f"Task '{description}' added.")
    else:
        print("Task description cannot be empty.")

def mark_task_complete(tasks):
    """Marks a task as complete."""
    display_tasks(tasks)
    if not tasks:
        return

    try:
        task_num = int(input("Enter the number of the task to mark as complete: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]['completed'] = True
            print(f"Task '{tasks[task_num - 1]['description']}' marked as complete.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def delete_task(tasks):
    """Deletes a task from the list."""
    display_tasks(tasks)
    if not tasks:
        return

    try:
        task_num = int(input("Enter the number of the task to delete: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1) # .pop() removes at index and returns item
            print(f"Task '{removed_task['description']}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    """Main function to run the To-Do List application."""
    tasks = load_tasks() # Load tasks when the app starts

    while True:
        print("To-Do List Manager")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task Complete")
        print("4. Delete Task")
        print("5. Save Tasks and Exit")
        print("6. Exit Without Saving")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_task_complete(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Exiting To-Do List Manager. Goodbye!")
            break # Exit the loop
        elif choice == '6':
            print("Exiting To-Do List Manager without saving changes. Goodbye!")
            break # Exit the loop
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
        input("\nPress Enter to continue...") # Pause for user to read output

if __name__ == "__main__":
    main()
