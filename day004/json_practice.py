import json
tasks = ["买牛奶", "写代码"]
with open("tasks.json", "w") as f:
    json.dump(tasks, f)
try:
    with open("tasks.json", "r") as f:
        loaded = json.load(f)
except FileNotFoundError:
    loaded = []
print(loaded)