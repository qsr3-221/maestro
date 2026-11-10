from .book import Book
from .exceptions import EmptyTitleError,EmptyAuthorError
class BookManager:
    def __init__(self):
        self.books = []
    def add(self, title: str, author:str):
        if not title.strip():
            raise EmptyTitleError("标题为空")
        if not author.strip():
            raise EmptyAuthorError("作者为空")
        self.books.append(Book(title,author))
    def remove(self, idx:int):
        if not 0 <= idx < len(self.books):
            return False
        del self.books[idx]
        return True
    def show(self):
        for i, b in enumerate(self.books, start=1):
            print(f"{i}. {b.title} - {b.author}")
    def stats(self):
        return len(self.books)
