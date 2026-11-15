from .exceptions import EmptyTitleError
class Task:
    def __init__(self, title:str):
        if not title:
            raise EmptyTitleError("Title cannot be empty")
        self.title = title
    def to_dict(self) -> dict:
        return {"title": self.title}
    