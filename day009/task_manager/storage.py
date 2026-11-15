from .task import Task
import json
def save_tasks(tasks, filename):
    data = [t.to_dict() for t in tasks]
    with open(filename, "w") as f:
        json.dump(data, f)
def load_tasks(filename):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
