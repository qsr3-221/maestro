from task_manager.manager import TaskManager
from task_manager.exceptions import EmptyTitleError

tm = TaskManager()

# 测试 1
tm.add("买牛奶")
print("现在有几个任务？", len(tm.tasks))

# 测试 2
try:
    tm.add("   ")
except EmptyTitleError as e:
    print("成功抓住了错误：", e)