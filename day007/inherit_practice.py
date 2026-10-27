class BaseTask:
    def __init__(self, title):
        self.title = title
        self.done = False
    def show(self):
        print(f"{self.title}-{self.done}")
class SubTask(BaseTask):
    pass
s = SubTask("继承任务")
s.show()
print(s.title, s.done)