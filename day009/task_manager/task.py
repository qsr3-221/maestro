class Task:
    def __init__(self, title: str):
        self.title = title
    def to_dict(self) -> dict:
        return {"title": self.title}