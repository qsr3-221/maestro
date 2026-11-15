from task_manager.task import Task
from task_manager.storage import save_tasks, load_tasks

tasks = [Task("a"), Task("b")]
save_tasks(tasks, "probe_tasks.json")
loaded = load_tasks("probe_tasks.json")
print(type(loaded))
print(type(loaded[0]))
print(loaded[0].title)
print([t.to_dict() for t in loaded])
print(load_tasks("不存在.json"))