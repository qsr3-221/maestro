d = {"name":"Tom","age":20,"city":"kj"}
for k, v in d.items():
    print(f"{k} = {v}")
keys = ["name", "age", "city", "job"]
for k in keys:
    print(f"{k} = {d.get(k, "not found")}")