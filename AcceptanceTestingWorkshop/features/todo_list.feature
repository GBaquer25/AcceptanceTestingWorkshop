"""
import datetime

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

# Feature: Manage to-do list

Feature: Manage To-Do List

  Scenario: Add a task to the to-do list
    Given the to-do list is empty
    When the user adds a task "Buy groceries"
    Then the to-do list should contain "Buy groceries"   


  Scenario: List all tasks in the to-do list
    Given the to-do list contains tasks:
      | Task |
      | Buy groceries |
      | Pay bills |
    When the user lists all tasks
    Then the output should contain:
      | Task   
 |
      | Buy groceries |
      | Pay bills |

  Scenario: Mark a task as completed
    Given the to-do list contains tasks:
      | Task | Status |
      | Buy groceries | Pending |
    When the user marks "Buy groceries" as completed
    Then the to-do list should contain:
      | Task | Status |
      | Buy groceries | Completed |

  Scenario: Clear the entire to-do list
    Given the to-do list contains tasks:
      | Task |
      | Buy groceries |
      | Pay bills |
    When the user clears the to-do list
    Then the to-do list should be empty