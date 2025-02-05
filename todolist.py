import json
import os

class ToDoListApp:
    def __init__(self):
        self.tasks = {}
        self.load_tasks()

    def save_tasks(self):
        with open("tasks.json", "w") as file:
            json.dump(self.tasks, file)

    def load_tasks(self):
        if os.path.exists("tasks.json"):
            with open("tasks.json", "r") as file:
                self.tasks = json.load(file)

    def display_tasks(self):
        print("\n📌 To-Do List:")
        if not self.tasks:
            print("No tasks available. Add a new task!")
            return
        print("=" * 30)
        for task_id, task in sorted(self.tasks.items()):
            status = "[✅]" if task["done"] else "[ ]"
            print(f"{task_id}. {status} {task['name']}")
        print("=" * 30)

    def add_task(self):
        task_name = input("Enter task name: ").strip()
        if not task_name:
            print("⚠️ Task name cannot be empty!")
            return
        task_id = max(map(int, self.tasks.keys()), default=0) + 1
        self.tasks[str(task_id)] = {"name": task_name, "done": False}
        self.save_tasks()
        print(f"✅ Task '{task_name}' added successfully!")

    def delete_task(self):
        self.display_tasks()
        task_id = input("Enter task number to delete: ").strip()
        if task_id in self.tasks:
            del self.tasks[task_id]
            self.save_tasks()
            print("🗑️ Task deleted successfully!")
        else:
            print("⚠️ Invalid task number!")

    def mark_done(self):
        self.display_tasks()
        task_id = input("Enter task number to mark as done/undo: ").strip()
        if task_id in self.tasks:
            self.tasks[task_id]["done"] = not self.tasks[task_id]["done"]
            self.save_tasks()
            print("✔️ Task status updated!")
        else:
            print("⚠️ Invalid task number!")

    def clear_tasks(self):
        confirm = input("Are you sure you want to delete all tasks? (yes/no): ").strip().lower()
        if confirm == "yes":
            self.tasks.clear()
            self.save_tasks()
            print("🧹 All tasks cleared!")
        else:
            print("Action canceled.")

def main():
    app = ToDoListApp()
    while True:
        print("\n📋 To-Do List App")
        print("1️⃣ Display Tasks")
        print("2️⃣ Add Task")
        print("3️⃣ Delete Task")
        print("4️⃣ Mark Task as Done/Undo")
        print("5️⃣ Clear All Tasks")
        print("6️⃣ Exit")
        choice = input("Choose an option: ").strip()
        
        if choice == "1":
            app.display_tasks()
        elif choice == "2":
            app.add_task()
        elif choice == "3":
            app.delete_task()
        elif choice == "4":
            app.mark_done()
        elif choice == "5":
            app.clear_tasks()
        elif choice == "6":
            print("👋 Exiting app. Goodbye!")
            break
        else:
            print("⚠️ Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
