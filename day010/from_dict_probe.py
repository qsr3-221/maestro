class Task:
    def __init__(self, id, title, done=False):
        self.id = id
        self.title = title
        self.done = done
    def to_dict(self) -> dict:
        return {"id": self.id, "title": self.title, "done": self.done}
    @classmethod
    def from_dict(cls, data:dict) -> "Task":
        return cls(
            id = data["id"],
            title = data["title"],
            done = data.get("done", False)
        )
data = {"id": 1, "title": "a", "done": False}
t = Task.from_dict(data)
print(type(t))
print(t.to_dict())
data2 = {"id": 2, "title": "b"}
t2 = Task.from_dict(data2)
print(t2.done)
print(t2.to_dict())
t3 = Task(3, "c")
print(t3.to_dict())