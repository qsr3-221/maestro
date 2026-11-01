class BaseTask:
    def __init__(self, title):
        self.title = title
        self.done = False

    def show(self):
        print(self.title)


class SubTask(BaseTask):
    def __init__(self, title, priority):
        super().__init__(title)
        self.title = title
        self.priority = priority


t = SubTask("任务A", 1)
t.show()
print(t.priority)
print(t.done)