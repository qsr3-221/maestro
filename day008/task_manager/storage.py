import json
from .task import Task
def save_tasks(tasks: list[Task], filename:str) -> None:
    data = [t.to_dict() for t in tasks]
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
def load_tasks(filename:str) -> list[Task]:
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
            return [Task(item["title"]) for item in data]
    except (FileNotFoundError,json.JSONDecodeError):
        return []