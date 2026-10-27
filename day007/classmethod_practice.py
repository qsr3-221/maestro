class BaseTask:
    def __init__(self, title):
        self._title = title
        self.done = False
    def get_title(self):
        return self._title   
    @classmethod
    def create_default(cls):
        return cls("默认任务")
    @classmethod
    def create_urgent(cls):
        return cls("紧急任务")
t1 = BaseTask.create_default()
print(t1.get_title())
t2 = BaseTask.create_urgent()
print(t2.get_title())
#cls指向类