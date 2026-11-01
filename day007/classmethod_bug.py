class BaseTask:
    def __init__(self, title):
        self._title = title

    def get_title(self):
        return self._title
    @classmethod
    def create_default(cls):
        return cls("默认任务")


t = BaseTask.create_default()
print(t.get_title())