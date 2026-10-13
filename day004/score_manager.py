import json
def save_scores(scores):
    with open("scores.json", "w") as f:
        json.dump(scores, f)
def load_scores():
    try:
        with open("scores.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
def add_score(scores):
    name = input("name: ")
    if name == "":
        print("非法输入")
        return
    score = input("score: ")    
    if score.isdigit():
        score = int(score)
    else:
        print("输入数字")
        return
    if not 0 <= score <= 100:
        print("超出范围")
        return
    if name in scores:
        scores[name] = score
        print("已修改")
    else:
        scores[name] = score
        print("已添加")
def show_scores(scores):
    if not scores:
        print("暂无成绩")
        return
    for k, v in scores.items():
        print(f"{k}: {v}")
def show_stats(scores):
    if not scores:
        print("暂无成绩")
        return
    num = 0
    total_score = 0
    for k, v in scores.items():
        num += 1
        total_score += v
    average_score = total_score / num
    print(f"人数:{num}")
    print(f"总分:{total_score}")
    print(f"平均分:{average_score}")
def delete_student(scores):
    if not scores:
        print("不能删除")
        return
    for k, v in scores.items():
        print(f"{k}: {v}")
    name = input("name: ")
    if not name in scores:
        print("学生不存在")
        return
    scores.pop(name)
    print("删除成功")
scores = load_scores()
while True:
    print("1. 添加 / 修改成绩")
    print("2. 查看所有成绩")
    print("3. 统计")
    print("4. 删除学生")
    print("5. 退出")
    choice = input("choice: ")
    if not choice.isdigit():
        print("非法输入")
        continue
    choice = int(choice)
    if choice == 1:
        add_score(scores)
    elif choice == 2:
        show_scores(scores)
    elif choice == 3:
        show_stats(scores)
    elif choice == 4:
        delete_student(scores)
    elif choice == 5:
        save_scores(scores)
        print("bye")
        break