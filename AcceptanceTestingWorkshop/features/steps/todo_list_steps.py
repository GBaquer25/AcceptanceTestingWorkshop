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
from todo_list import Task  # Replace with your actual module
"""
@given('the to-do list is empty')
def empty_todo_list(context):
    context.todo_list = ToDoList()

@when('the user adds a task "{task}"')
def add_task(context, task):
    context.todo_list.add_task(task)

@then('the to-do list should contain "{task}"')
def check_task_in_list(context, task):
    assert task in context.todo_list.get_tasks(), f"Task '{task}' not found in to-do list"
"""
to_do_list = []

# Step 1: Given the to-do list is empty
@given('the to-do list is empty')
def step_impl(context):
  # Set the to-do list as an empty list
  global to_do_list
  to_do_list = []

# Step 2: When the user adds a task "{task}"
@when('the user adds a task "{task}"')
def step_impl(context, task):
  # Add the task to the to-do list
  global to_do_list
  to_do_list.append(task)

# Step 3: Then the to-do list should contain "{task}"
@then('the to-do list should contain "{task}"')
def step_impl(context, task):
  # Assert that the task is present in the to-do list
  assert task in to_do_list, f"Task '{task}' not found in the to-do list."

# Step 4: When the user marks a task "{task}" as complete
@when('the user marks a task "{task}" as complete')
def step_impl(context, task):
  # Find the index of the task
  try:
    task_index = to_do_list.index(task)
  except ValueError:
    raise Exception(f"Task '{task}' not found in the to-do list.")

  # Simulate marking the task as complete (implementation might vary based on your code)
  # This is a placeholder, replace with actual logic to mark a task complete
  # to_do_list[task_index].mark_completed()  # Assuming a mark_completed method

# Step 5: Then the task "{task}" should be marked as complete
@then('the task "{task}" should be marked as complete')
def step_impl(context, task):
  # Find the index of the task (same logic as step 4)
  try:
    task_index = to_do_list.index(task)
  except ValueError:
    raise Exception(f"Task '{task}' not found in the to-do list.")

  # Assert that the task is marked as complete (replace with actual logic)
  # is_completed = to_do_list[task_index].is_completed()  # Assuming an is_completed method
  # assert is_completed, f"Task '{task}' is not marked as complete."

# Step 6: When the user deletes a task "{task}"
@when('the user deletes a task "{task}"')
def step_impl(context, task):
  # Find the index of the task (same logic as step 4)
  try:
    task_index = to_do_list.index(task)
  except ValueError:
    raise Exception(f"Task '{task}' not found in the to-do list.")

  # Remove the task from the list
  del to_do_list[task_index]

# Step 7: Then the to-do list should not contain "{task}"
@then('the to-do list should not contain "{task}"')
def step_impl(context, task):
  # Assert that the task is not present in the to-do list
  assert task not in to_do_list, f"Task '{task}' still exists in the to-do list."
  
  # Step 8: When the user lists all tasks
@when('the user lists all tasks')
def step_impl(context):
  # Simular la acción de listar tareas (implementación real dependerá de tu código)
  # Por ejemplo, podrías imprimir la lista de tareas en la consola
  print(to_do_list)

# Step 9: Then the user should see all tasks in the list
@then('the user should see all tasks in the list')
def step_impl(context, captured_output):
    list_tasks(to_do_list)
  # Verificar que la lista impresa coincida con la lista interna
  # Esta verificación dependerá de cómo hayas implementado la impresión
  # Por ejemplo, si usas un mock para capturar la salida, puedes compararla
  # with self.captured_output:
  #   print(to_do_list)
  # assert self.captured_output == ...  # Comparar con la salida esperada
    expected_output = "\n".join(str(task) for task in to_do_list)
    assert expected_output in out, "La salida no coincide con la lista de tareas esperada"
"""
# Step 10: When the user lists completed tasks
@when('the user lists completed tasks')
def step_impl(context):
  # Simular la acción de listar tareas completadas (implementación real dependerá de tu código)
  # Por ejemplo, podrías filtrar la lista y mostrar solo las tareas completadas
  # completed_tasks = [task for task in to_do_list if task.completed]
  # print(completed_tasks)

# Step 11: Then the user should see only completed tasks in the list
# ... (similar a step 9, pero verificando solo las tareas completadas)
"""
# Step 12: When the user clears all tasks
@when('the user clears all tasks')
def step_impl(context):
  global to_do_list
  to_do_list.clear()

# Step 13: Then the to-do list should be empty
@then('the to-do list should be empty')
def step_impl(context):
  assert len(to_do_list) == 0, "The to-do list is not empty."