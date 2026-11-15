import os
import unittest
from task_manager.manager import TaskManager
from task_manager.exceptions import EmptyTitleError
from task_manager.task import Task
from task_manager.storage import save_tasks, load_tasks
class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.filename = "test_tasks.json"
        if os.path.exists(self.filename):
            os.remove(self.filename)
        self.tm = TaskManager()                        

    def tearDown(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)
   
    def test_add_task(self):
        self.tm.add("买牛奶")
        self.assertEqual(len(self.tm.tasks), 1)
    def test_add_empty_title(self):
        with self.assertRaises(EmptyTitleError):
            self.tm.add("")

    def test_add_normal(self):
        self.tm.add("test")
        self.assertEqual(len(self.tm.tasks), 1)

    def test_remove_out_of_range(self):
        self.assertFalse(self.tm.remove(99))

    def test_remove_normal(self):
        self.tm.add("a")
        self.assertTrue(self.tm.remove(0))
        self.assertEqual(len(self.tm.tasks), 0)

    def test_stats_count(self):
        self.tm.add("1")
        self.tm.add("2")
        self.tm.add("3")
        self.assertEqual(self.tm.stats(), 3)

    def test_save_load_roundtrip(self):
        self.tm.add("hello")
        save_tasks(self.tm.tasks, self.filename)
        loaded = load_tasks(self.filename)
        self.assertEqual(loaded[0].title, "hello")

    def test_load_is_task_instance(self):
        self.tm.add("obj")
        save_tasks(self.tm.tasks, self.filename)
        loaded = load_tasks(self.filename)
        self.assertIsInstance(loaded[0], Task)

    def test_load_not_exist_file(self):
        self.assertEqual(load_tasks("nonexistent_test_file.json"), [])
    