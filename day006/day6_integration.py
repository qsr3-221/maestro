import json
class Task:
    def __init__(self,title,done):
        self.title = title
        self.done = done
class TaskManager:
    def __init__(self):
        self.tasks = []
    def add(self,title):
        if not title:
            raise ValueError("Title cannot be empty")
        task = Task(title, False)
        self.tasks.append(task)
    def remove(self, idx):
        if not 0 <= idx < len(self.tasks):
            return False
        self.tasks.pop(idx)
        return True
    def show(self):
        for task in self.tasks:
            print(task.title, task.done)
    def save_to_file(self, filename):
        data = [{"title": task.title,"done": task.done} for task in self.tasks]
        with open(filename, "w") as f:
            json.dump(data, f)
    def load_from_file(self, filename):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
        except (FileNotFoundError,json.JSONDecodeError):
            return []
        self.tasks = []
        for item in data:
            self.tasks.append(Task(item["title"], item["done"]))
if __name__ == "__main__":
    m = TaskManager()
    m.add("a")
    m.add("b")
    try:
        m.add("")
    except ValueError as e:
        print(e)
    m.save_to_file("tasks.json")
    m2 = TaskManager()
    m2.load_from_file("tasks.json")
    m2.show()