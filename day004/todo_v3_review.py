tasks = []
while True:
    print("1. 添加任务")
    print("2. 查看任务")
    print("3. 统计任务数")
    print("4. 删除任务")
    print("5. 退出")
    choice = input("choice: ")
    if choice.isdigit():
        choice = int(choice)
    else:
        print("输入不合法")
        continue
    if choice == 1:
        task = input("task: ")
        if task == "":
            print("输入不合法")
            continue
        tasks.append(task)
        print("添加成功")
    elif choice == 2:
        task_index = 0
        if not tasks:
            print("暂无任务")
        for task in tasks:
            print(f"{task_index}: {task}")
            task_index += 1
    elif choice == 3:
        if not tasks:
            print("任务数量: 0")
        else:
            print(f"任务数量: {len(tasks)}")
    elif choice == 4:
        task_index = 0
        if not tasks:
            print("不能删除")
            continue
        for task in tasks:
            print(f"{task_index}: {task}")
            task_index += 1
        idx = input("num: ")
        if idx.isdigit():
            idx = int(idx)
        else:
            print("非法输入")
            continue
        if 0 <= idx < len(tasks):
            removed = tasks.pop(idx)
            print(f"{removed}删除成功")
        else:
            print("索引越界")
            continue
    elif choice == 5:
        print("bye")
        break