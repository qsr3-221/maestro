class BaseTask:
    def __init__(self, title):
        self._title = title
        self.done = False
    def get_title(self):
        return self._title
    def set_title(self, new_title):
        if not new_title:
            raise ValueError("title cannot be empty")
        self._title = new_title
t = BaseTask("任务A")
print(t.get_title())
t.set_title("任务B")
print(t.get_title())
try:
    t.set_title("")
except ValueError as e:
    print(e)
t._title = ""
print(t.get_title())