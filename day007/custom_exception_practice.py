class EmptyTitleError(Exception):
    pass
class BaseTask:
    def __init__(self, title):
        if not title:
            raise EmptyTitleError("title cannot be empty")
        self._title = title
    @property 
    def title(self):
        return self._title
t = BaseTask("任务A")
try:
    BaseTask("")
    print("创建成功")
except EmptyTitleError as e:
    print("捕获到：", e)
else:
        print("没有异常")