"""
import pytest
from todo_list.tasks import ToDoList, Task

def test_add_task():
    todo_list = ToDoList()
    todo_list.add_task("Buy milk")
    assert len(todo_list.tasks) == 1

def test_list_tasks():
    todo_list = ToDoList()
    todo_list.add_task("Buy milk")
    todo_list.add_task("Walk the dog")
    assert str(todo_list.tasks[0]) == "Buy milk (medium, due: None, status: pending)"

def test_mark_complete_valid_index():
    todo_list = ToDoList()
    todo_list.add_task("Buy milk")
    todo_list.add_task("Walk the dog")

    todo_list.mark_complete(1)

    assert todo_list.tasks[0].status == "completed"

def test_mark_complete_invalid_index():
    todo_list = ToDoList()
    todo_list.add_task("Buy milk")

    with pytest.raises(ValueError):
        todo_list.mark_complete(2)
"""
from behave import given, when, then
from todo_list import ToDoList  # Replace with your actual module

@given('the to-do list is empty')
def empty_todo_list(context):
    context.todo_list = ToDoList()

@when('the user adds a task "{task}"')
def add_task(context, task):
    context.todo_list.add_task(task)

@then('the to-do list should contain "{task}"')
def check_task_in_list(context, task):
    assert task in context.todo_list.get_tasks(), f"Task '{task}' not found in to-do list"
