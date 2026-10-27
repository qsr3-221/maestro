class BaseTask:
    def __init__(self, title):
        self._title = title
        self.done = False
    @property
    def title(self):
        return self._title
    @property
    def status(self):
        if self.done:
            return "done"
        return "todo"
t = BaseTask("任务A")
print(t.title)
print(t.status)
t.done = True
print(t.status)