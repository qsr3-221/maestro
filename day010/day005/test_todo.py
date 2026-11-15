import unittest
import todo_v5
from unittest.mock import patch
class TestTodo(unittest.TestCase):
    def test_load_missing_file(self):
        result = todo_v5.load_tasks("a.json")
        self.assertEqual(result, [])
    def test_save_and_load(self):
        todo_v5.save_tasks(["a","b"],"b.json")
        result = todo_v5.load_tasks("b.json")
        self.assertEqual(result, ["a","b"])
    def test_add_task_empty(self):
        with patch("builtins.input", return_value=""):
            tasks = []
            todo_v5.add_task(tasks)
            self.assertEqual(tasks,[])
    def test_add_task_normal(self):
        with patch("builtins.input", return_value="hello"):
            tasks = []
            todo_v5.add_task(tasks)
            self.assertEqual(tasks,["hello"])
    def test_delete_task_out_of_range(self):
        with patch("builtins.input", return_value="100"):
            tasks = ["a"]
            todo_v5.delete_task(tasks)
            self.assertEqual(tasks,["a"])        
if __name__ == "__main__":
    unittest.main()