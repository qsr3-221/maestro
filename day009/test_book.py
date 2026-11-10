import unittest
from book_manager.manager import BookManager
from book_manager.exceptions import EmptyTitleError, EmptyAuthorError
class BookError(unittest.TestCase):
    def test_add_book(self):
        bm = BookManager()
        bm.add("a","b")
        self.assertEqual(len(bm.books), 1)
    def test_empty_title(self):
        bm = BookManager()
        with self.assertRaises(EmptyTitleError):
            bm.add("", "作者")
    def test_empty_author(self):
        bm = BookManager()
        with self.assertRaises(EmptyAuthorError):
            bm.add("书名", " ")
    def test_remove_valid(self):
        bm = BookManager()
        bm.add("z","x")
        self.assertTrue(bm.remove(0))
    def test_remove_invalid(self):
        bm = BookManager()
        self.assertFalse(bm.remove(99))
