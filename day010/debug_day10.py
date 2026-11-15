from task_manager.task import Task

data = {"title": "a"}
t = Task.from_dict(data)
print(t.title)  