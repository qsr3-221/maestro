import json

tasks = ["a", "b"]

with open("debug_tmp.json", "w") as f:
    json.dump(f, tasks)      # 故意写反