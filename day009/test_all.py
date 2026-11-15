from task_manager.manager import TaskManager

tm = TaskManager()
tm.add("买牛奶")

# 我们把盒子里的东西拿出来看看
t = tm.tasks[0]
print("t 是什么类型？", type(t))
print("t 是什么样子？", t)
print("t 的 title 是什么？", t.title)

# 对比一下字典和对象的区别
print("t 变成字典长啥样？", t.to_dict())