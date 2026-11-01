tasks = []
choice = 0
while choice != 3:
    print("1. 添加任务")
    print("2. 查看任务")
    print("3. 退出")
    choice = int(input("choice: "))
    if choice == 1:
        a = input("new task: ")
        tasks.append(a)
        print("任务已添加")
    elif choice == 2:
        if not tasks:
            print("暂无任务")
        else:
            for task in tasks:
                print(task)
    elif choice == 3:
        print("退出程序")
    else:
        print("无效输入")
print("程序结束")