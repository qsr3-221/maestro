import json
def save_tasks(tasks, filename):
    try:
        with open(filename, "w") as f:
            json.dump(tasks, f)
    except TypeError:
        print("保存失败：数据无法序列化")
def load_tasks(filename):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []
def show_tasks(tasks):
    task_index = 0
    if not tasks:
        print("暂无任务")
    for task in tasks:
        print(f"{task_index}: {task}")
        task_index += 1
def add_task(tasks):
    task = input("task: ")
    if task == "":
        print("输入不合法")
        return
    tasks.append(task)
    print("添加成功")
def delete_task(tasks):
    task_index = 0
    if not tasks:
        print("不能删除")
        return
    for task in tasks:
        print(f"{task_index}: {task}")
        task_index += 1
    idx = input("num: ")
    if idx.isdigit():
        idx = int(idx)
    else:
        print("非法输入")
        return
    if 0 <= idx < len(tasks):
        removed = tasks.pop(idx)
        print(f"{removed}删除成功")
    else:
        print("索引越界")
        return
def main():       
    tasks = load_tasks("tasks.json")
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
            add_task(tasks)
        elif choice == 2:
            show_tasks(tasks)
        elif choice == 3:
            if not tasks:
                print("任务数量: 0")
            else:
                print(f"任务数量: {len(tasks)}")
        elif choice == 4:
            delete_task(tasks)
        elif choice == 5:
            print("bye")
            save_tasks(tasks, "tasks.json")
            break
if __name__ == "__main__":
    main()