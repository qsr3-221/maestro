class Book:
    def __init__(self, title:str, author:str):
        self.title = title
        self.author = author
    def to_dict(self):
        return {"title": self.title,"author": self.author}