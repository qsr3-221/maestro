tasks = ["a", "b", "c"]
if "d" in tasks:
    tasks.remove("d")
    print(tasks)
else:
    print("任务不存在，无法删除")