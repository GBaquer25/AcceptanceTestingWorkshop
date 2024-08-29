import datetime
import time

class Task:
     def __init__(self, description, due_date, priority, project):
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.project = project
        self.completed = False

def add_task(tasks):
    description = input("Enter task description: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    priority = input("Enter priority (high, medium, low): ")
    project = input("Enter project: ")
    tasks.append(Task(description, due_date, priority, project))

"""def list_tasks(tasks):
    if not tasks:
        print("No tasks in the list.")
    else:
        for i, task in enumerate(tasks):
            status = "Completed" if task.completed else "Incomplete"
            print(f"{i+1}. {task.description} (due: {task.due_date}, priority: {task.priority}, project: {task.project}, status: {status})")"""
def list_tasks(tasks, filter_status=None):
    if not tasks:
        print("No hay tareas en la lista.")
        return

    for i, task in enumerate(tasks):
        if filter_status is not None and task.completed != filter_status:
            continue
        status = "Completada" if task.completed else "Incompleta"
        print(f"{i+1}. {task.description} (due: {task.due_date}, prioridad: {task.priority}, proyecto: {task.project}, estado: {status})")
def mark_task_completed(tasks):
    task_number = int(input("Enter task number to mark as completed: ")) - 1
    if 0 <= task_number < len(tasks):
        tasks[task_number].completed = True
    else:
        print("Invalid task number.")

def delete_task(tasks):
    task_number = int(input("Ingrese el número de tarea a eliminar: ")) - 1
    if 0 <= task_number < len(tasks):
        del tasks[task_number]
        print("Tarea eliminada.")
    else:
        print("Número de tarea inválido.")

def clear_tasks(tasks):
    tasks.clear()

def main():
    tasks = []
    while True:
        print("\nGestor de Tareas")
        print("1. Agregar tarea")
        print("2. Listar tareas")
        print("3. Marcar tarea como completada")
        print("4. Eliminar tarea")
        print("5. Limpiar tareas")
        print("6. Listar tareas completadas")
        print("7. Listar tareas incompletas")
        print("8. Salir")
        choice = input("Ingrese su opción: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            list_tasks(tasks)
        elif choice == '3':
            mark_task_completed(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            clear_tasks(tasks)
        elif choice == '6':
            list_tasks(tasks, True)
        elif choice == '7':
            list_tasks(tasks, False)
        elif choice == '8':
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
