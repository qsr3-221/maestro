try:
    with open("not_exist_file.txt", "r") as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print("文件不存在")