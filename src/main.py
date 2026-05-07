import json
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from utils.helpers import format_task, validate_task_name

DATA_FILE = os.path.join(os.path.dirname(__file__), '..', 'config', 'tasks.json')

def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_tasks(tasks):
    with open(DATA_FILE, 'w') as f:
        json.dump(tasks, f, indent=2, ensure_ascii=False)

def add_task(name):
    if not validate_task_name(name):
        print("Erro: nome da tarefa inválido (mínimo 3 caracteres).")
        return
    tasks = load_tasks()
    task = {"id": len(tasks) + 1, "name": name, "done": False}
    tasks.append(task)
    save_tasks(tasks)
    print(f"Tarefa adicionada: {name}")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("Nenhuma tarefa encontrada.")
        return
    for t in tasks:
        print(format_task(t))

def complete_task(task_id):
    tasks = load_tasks()
    for t in tasks:
        if t["id"] == int(task_id):
            t["done"] = True
            save_tasks(tasks)
            print(f"Tarefa #{task_id} concluída!")
            return
    print("Tarefa não encontrada.")

def remove_task(task_id):
    tasks = load_tasks()
    tasks = [t for t in tasks if t["id"] != int(task_id)]
    save_tasks(tasks)
    print(f"Tarefa #{task_id} removida.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python main.py [add|list|done|remove] [args]")
        sys.exit(1)
    cmd = sys.argv[1]
    if cmd == "add":
        add_task(" ".join(sys.argv[2:]))
    elif cmd == "list":
        list_tasks()
    elif cmd == "done":
        complete_task(sys.argv[2])
    elif cmd == "remove":
        remove_task(sys.argv[2])
    else:
        print("Comando desconhecido.")
