#from todo_list import Task  # Replace with your actual module
from behave import given, when, then
#Descomentar el código
"""
Feature: ManageTasks

Scenario: Add tasks
Given the to-do list is empty
Then  the to_do list should be empty 


Scenario: List all pending tasks
    Given the to-do list contains tasks:
      | Task       |
      | Buy groceries |
      | Pay bills   |
    When the user lists all pending tasks
    Then the to-do list should display:
      | Task       |
      | Buy groceries |
      | Pay bills   |

  @markCompletedTask
  Scenario: Mark a task as completed
    Given the to-do list contains tasks:
      | Task | Status |
      | Buy groceries | Pending |
    When the user marks "Buy groceries" as completed
    Then the to-do list should contain:
      | Task | Status |
      | Buy groceries | Completed |

Scenario: Clearalltasks
Given the to_do_list contains tasks:
  | Task |
  | Buy groceries |
  | Pay bills |
When the user clears all tasks
Then the to_do_list should be empty

Scenario: DeleteTask
Given the to_do_list contains tasks:
  | Task |
  | Buy groceries |
  | Pay bills |
When the user delete one task
Then the to_do_list should be delete the task selectioned
  """