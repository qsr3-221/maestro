class Task:
    def __init__(self,title,done):
        self.title = title
        self.done = done
class TaskManager:
    def __init__(self):
        self.tasks = []
    def add(self,title):
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
if __name__ == "__main__":
    m = TaskManager()
    m.add("a")
    m.add("b")
    m.add("c")
    m.show()
    m.remove(1)
    m.show()
    print(len(m.tasks))
    print(m.remove(10))
    print(len(m.tasks))