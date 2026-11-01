class Task:
    def __init__(self, title):
        self.title = title
        self.done = False
    def show(self):
        print(f"{self.title}-{self.done}")
class TaskManager:
    def __init__(self):
        self.tasks = []
    def add_task(self, title):
        if not title:
            raise ValueError("no title")
        task = Task(title)
        self.tasks.append(task)
    def show_all(self):
        for task in self.tasks:
            task.show()
if __name__ == "__main__":
    m = TaskManager()
    m.add_task("学习Python")
    m.add_task("推送GitHub")
    m.show_all()

        