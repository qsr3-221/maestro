import unittest
from task_manager.manager import TaskManager
from task_manager.exceptions import EmptyTitleError
class TestTaskManager(unittest.TestCase):
    def test_add_task(self):
        tm = TaskManager()
        tm.add("买牛奶")
        self.assertEqual(len(tm.tasks),1)
    