d = {"name": "Tom", "age": 20}
key = input("key: ")
if key in d:
    del d[key]
    print(d)
else:
    print("键不存在，无法删除")