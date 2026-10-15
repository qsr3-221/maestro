import json
def safe_int(text):
    try:
        text = int(text)
        return text
    except ValueError:
        return None
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None
def get_score(scores, name):
    try:
        return scores[name]
    except KeyError:
        return 0
def set_age(age):
    if age < 0:
        raise ValueError("age 不能是负数")
    else:
        return age
        
def check_file(filename):
    try:
        with open(filename, "r") as f:
             return json.load(f)
    except FileNotFoundError:
        return "文件不存在"
    finally:
        print("检查完毕")
def demo_else_finally(text):
    try:
        n = int(text)
    except ValueError:
        print("转换失败")
    else:
        print("转换成功")
        print(n)
    finally:
        print("结束")
if __name__ == "__main__":
    print(safe_int("123"))
    print(safe_int("abc"))
    print(safe_divide(10, 2))
    print(safe_divide(10, 0))

    scores = {"Tom": 90}
    print(get_score(scores, "Tom"))
    print(get_score(scores, "Jerry"))

    print(set_age(18))
    try:
        print(set_age(-1))
    except ValueError as e:
        print("捕获：", e)

    print(check_file("no_such_file.json"))

    demo_else_finally("123")
    demo_else_finally("abc")