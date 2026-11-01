class BaseTask:
    def __init__(self, title):
        self._title = title

    def get_title(self):
        return self._title

    @staticmethod
    def is_valid_title(title):
        return title.upper()


t = BaseTask("任务A")
print(BaseTask.is_valid_title("任务B"))