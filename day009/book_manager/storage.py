import json
from .book import Book
def save_books(books,filename):
    data = [b.to_dict() for b in books]
    with open(filename, "w") as f:
        json.dump(data, f)
def load_books(filename):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []