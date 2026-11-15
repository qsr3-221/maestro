from .manager import TaskManager 
from .storage import save_tasks, load_tasks
from .exceptions import EmptyTitleError
def main():
    tm = TaskManager()
    while True:
        print("1.添加")
        print("2.查看")
        print("3.删除")
        print("4.统计")
        print("5.退出")
        choice = input("请输入:")
        if choice == "1":
            title = input("请输入标题: ")
            try:
                tm.add(title)
                print("添加成功")
            except EmptyTitleError as e:
                print("错误：", e)
        elif choice == "2":
            tm.show()
        elif choice == "3":
            num = int(input("请输入要删除的编号: ")) - 1
            if tm.remove(num):
                print("删除成功")
            else:
                print("删除失败：编号越界")
        elif choice == "4":
            print(tm.stats())
        elif choice == "5":
            save_tasks(tm.tasks, "tasks.json")
            print("程序退出")
            break
if __name__ ==  "__main__":
    main()