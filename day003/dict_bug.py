person = {"name": "Tom", "age": 20}
key = input("key: ")
if key in person:
    print(person[key])
else:
    print("键不存在")