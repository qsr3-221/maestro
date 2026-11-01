tasks = []
while True:
    print("1 添加任务")
    print("2 查看任务")
    print("3 删除任务")
    print("4 退出")
    print("5 统计任务数")
    choice = int(input("choice: "))
    if choice == 1:
        task = input("task: ")
        tasks.append(task)
    elif choice == 2:
        i = 0
        for task in tasks:
            i += 1
            print(f"{i}.{task}")
    elif choice == 3:
        num = input("num: ")
        if num.isdigit():
            num = int(num) - 1
        else:
            print("请输入数字")
            continue
        if not tasks:
            print("任务列表为空，无法删除")
        elif not 0 <= num < len(tasks):
            print("任务不存在，无法删除")
        else:
            d = tasks.pop(num)
            print(f"已删除{d}")
    elif choice == 4:
        print("bye")
        break
    elif choice == 5:
        if not tasks:
            print("任务数为 0")
        else:
            print(f"任务数为{len(tasks)}")
    else:
        print("Invalid enter")