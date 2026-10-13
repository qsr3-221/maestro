def add_task(tasks):
    tasks.append("写代码")

def replace(tasks):
    tasks = ["新列表"]

tasks = ["买牛奶"]
add_task(tasks)
print("after add_task:", tasks)

tasks = ["买牛奶"]
replace(tasks)
print("after replace:", tasks)