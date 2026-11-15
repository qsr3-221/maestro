from .task import Task
from .exceptions import EmptyTitleError
class TaskManager:
    def __init__(self):
        self.tasks = []
    def add(self, title:str):
        if not title.strip():
            raise EmptyTitleError("标题不能为空")
        self.tasks.append(Task(title))        
    def remove(self, idx: int):
        if not 0 <= idx < len(self.tasks):
            return False
        del self.tasks[idx]
        return True
    def show(self):
        for i, t in enumerate(self.tasks, start=1):
            print(f"{i}.{t.title}")
    def stats(self):
        return len(self.tasks)