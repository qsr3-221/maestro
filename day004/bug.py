import json

def save_tasks(tasks):
    with open("tasks.json", "w") as f:
        json.dump(f, tasks)

tasks = ["买牛奶"]
save_tasks(tasks)