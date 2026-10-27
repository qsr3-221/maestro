class BaseTask:
    def __init__(self, title):
        self._title = title
        self.done = False
    def get_title(self):
        return self._title
    @classmethod
    def create_default(cls):
        return cls("默认任务")
    @staticmethod
    def is_valid_title(title):
        return bool(title)
t = BaseTask.create_default()
print(t.get_title())
print(BaseTask.is_valid_title("任务A"))
print(BaseTask.is_valid_title(""))