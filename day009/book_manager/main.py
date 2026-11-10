from .manager import BookManager
from .storage import save_books,load_books
from .exceptions import EmptyTitleError,EmptyAuthorError
def main():
    bm = BookManager()
    while True:
        print("1.添加")
        print("2.查看 ")
        print("3.删除")
        print("4.统计")
        print("5.保存并退出")
        choice = input("输入选择")
        if choice == "1":
            title = input("输入书名")
            author = input("输入作者")
            try:
                bm.add(title, author)
            except EmptyTitleError as e:
                print(e)
            except EmptyAuthorError as e:
                print(e)
        elif choice == "2":
            bm.show()
        elif choice == "3":
            num = int(input("输入要删除的数字")) -1
            if bm.remove(num): 
                print("成功") 
            else: 
                print("失败")
        elif choice == "4":
            print(bm.stats())
        elif choice == "5":
            save_books(bm.books, "books.json")
            break
if __name__ == "__main__": 
    main()