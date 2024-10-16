# Класс Task для управления задачами
class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.status = "не выполнено"  # По умолчанию задача не выполнена

    def mark_done(self):
        self.status = "выполнено"

    def __repr__(self):
        return f"Task('{self.description}', Deadline: {self.deadline}, Status: {self.status})"

# Функции для работы с задачами

# добавить задачу в список
def add_task(tasks, description, deadline):
    task = Task(description, deadline)
    tasks.append(task)

# получить список невыполненных задач
def get_current_tasks(tasks):
    return [task for task in tasks if task.status == "не выполнено"]

# вывести список всех задач в списке
def print_tasks(tasks):
    for task in tasks:
        print(task)

# Создаем список для хранения задач
tasks = []

# Добавляем несколько задач
add_task(tasks, "Купить продукты", "2024-10-18")
add_task(tasks, "Сходить на тренировку", "2024-10-19")
add_task(tasks, "Написать отчёт", "2024-10-20")
add_task(tasks, "Позвонить родителям", "2024-10-21")

# Выводим список всех текущих задач (все задачи не выполнены)
print("Текущие задачи:")
print_tasks(get_current_tasks(tasks))

# Отмечаем несколько задач как выполненные
tasks[0].mark_done()  # "Купить продукты" выполнено
tasks[2].mark_done()  # "Написать отчёт" выполнено

# Выводим обновленный список невыполненных задач
print("\nОбновленный список текущих задач:")
print_tasks(get_current_tasks(tasks))

# Выводим полный список всех задач, включая выполненные
print("\nПолный список всех задач:")
print_tasks(tasks)
