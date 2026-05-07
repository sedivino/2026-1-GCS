def format_task(task):
    status = "✓" if task["done"] else "○"
    return f"[{status}] #{task['id']} - {task['name']}"

def validate_task_name(name):
    return bool(name and name.strip() and len(name.strip()) >= 3)
