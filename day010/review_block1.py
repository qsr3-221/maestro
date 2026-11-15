class Task:
    def __init__(self, id, title, done=False):
        self.id = id
        self.title = title
        self.done = done
    def to_dict(self) -> dict:
        return {"id": self.id, "title": self.title, "done": self.done}
class MiniManager:
    def __init__(self) -> None:
        self.items:list[Task] = []
    def remove(self, idx) -> bool:
        if 0 <= idx < len(self.items):
            del self.items[idx]
            return True
        return False
def main():
    mi = MiniManager()
    mi.items.append(Task(1, "a"))
    mi.items.append(Task(2, "b"))
    ok = mi.remove(0)
    if ok:
        print("删除成功")
    else:
        print("删除失败")
    for t in mi.items:
        print(t.to_dict())
if __name__ == "__main__":
    main()
   