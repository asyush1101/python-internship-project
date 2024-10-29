class ToDoList:
    def __init__(self):
        self.tasks = []

    def display_tasks(self):
        if not self.tasks:
            print("\nYour to-do list is empty.")
            return
        print("\nYour To-Do List:")
        for index, task in enumerate(self.tasks, start=1):
            status = "✓" if task['completed'] else "✗"
            print(f"{index}. {task['task']} [{status}]")

    def add_task(self, task_name):
        task = {"task": task_name, "completed": False}
        self.tasks.append(task)
        print(f"Task '{task_name}' has been added to your to-do list.")

    def mark_task_complete(self, task_index):
        try:
            self.tasks[task_index - 1]["completed"] = True
            print(f"Task '{self.tasks[task_index - 1]['task']}' marked as complete.")
        except IndexError:
            print("Invalid task number. Please try again.")

    def delete_task(self, task_index):
        try:
            removed_task = self.tasks.pop(task_index - 1)
            print(f"Task '{removed_task['task']}' has been deleted from your list.")
        except IndexError:
            print("Invalid task number. Please try again.")

    def run(self):
        print("Welcome to the To-Do List Application!")
        while True:
            print("\nMenu:")
            print("1. View To-Do List")
            print("2. Add Task")
            print("3. Mark Task as Complete")
            print("4. Delete Task")
            print("5. Exit")
            choice = input("Enter your choice (1-5): ")

            if choice == '1':
                self.display_tasks()
            elif choice == '2':
                task_name = input("Enter the task: ")
                self.add_task(task_name)
            elif choice == '3':
                self.display_tasks()
                try:
                    task_index = int(input("Enter the task number to mark as complete: "))
                    self.mark_task_complete(task_index)
                except ValueError:
                    print("Please enter a valid number.")
            elif choice == '4':
                self.display_tasks()
                try:
                    task_index = int(input("Enter the task number to delete: "))
                    self.delete_task(task_index)
                except ValueError:
                    print("Please enter a valid number.")
            elif choice == '5':
                print("Exiting the To-Do List Application. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

# Run the application
if __name__ == "__main__":
    todo_list = ToDoList()
    todo_list.run()