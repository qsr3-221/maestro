choice = 0
while choice != 3:
    print("1. 添加任务")
    print("2. 查看任务")
    print("3. 退出")
    choice = int(input("choice: "))
    if choice == 1:
        print("添加任务")
    elif choice == 2:
        print("查看任务")
    elif choice == 3:
        print("退出")
    else:
        print("无效输入")
print("程序结束")