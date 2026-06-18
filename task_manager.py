import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False)

tasks = load_tasks()

print("=== Менеджер задач ===\n")

while True:
    print("\n1. Добавить задачу\n2. Показать задачи\n3. Удалить задачу\n4. Выйти")
    choice = input("Выбери (1-4): ")
    
    if choice == "1":
        task = input("Введи задачу: ")
        tasks.append({"task": task, "done": False})
        save_tasks(tasks)
        print("Задача добавлена!")
    elif choice == "2":
        for i, t in enumerate(tasks):
            status = "✓" if t["done"] else " "
            print(f"{i+1}. [{status}] {t['task']}")
    elif choice == "3":
        try:
            num = int(input("Номер задачи для удаления: ")) - 1
            if 0 <= num < len(tasks):
                del tasks[num]
                save_tasks(tasks)
                print("Задача удалена!")
        except:
            print("Неверный номер.")
    elif choice == "4":
        print("До свидания!")
        break
        