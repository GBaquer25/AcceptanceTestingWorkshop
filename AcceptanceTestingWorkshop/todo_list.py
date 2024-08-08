"""import datetime

class Task:
    def __init__(self, description, priority="medium", due_date=None, status="pending"):
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.status = status

    def __str__(self):
        return f"{self.description} ({self.priority}, due: {self.due_date}, status: {self.status})"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, priority="medium", due_date=None):
        task = Task(description, priority, due_date)
        self.tasks.append(task)

    def list_tasks(self):
        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. {task}")

    def mark_complete(self, index):
        if 1 <= index <= len(self.tasks):
            self.tasks[index - 1].status = "completed"
        else:
            print("Invalid task index")

    def clear_list(self):
        self.tasks = []

    
"""

class Task:
    def __init__(self, description, status="pending"):
        self.description = description
        self.status = status

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        # Add logic to create and add a task
        pass

    def list_tasks(self):
        # Implement logic to display tasks
        pass

    def mark_task_completed(self, index):
        # Implement logic to mark a task as completed
        pass

    def clear_list(self):
        # Implement logic to clear the task list
        pass
