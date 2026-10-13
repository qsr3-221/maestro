try:
    with open("not_exist.txt", "r") as f:
        exist = f.read()
        print(exist)
except FileNotFoundError:
    print("文件不存在，使用空列表")
