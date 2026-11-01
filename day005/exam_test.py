import unittest
import exam_day5
class TestExam(unittest.TestCase):
    def test_count_words(self):
        result = exam_day5.count_words("a b a")
        self.assertEqual(result,{"a": 2, "b": 1})
    def test_count_words_empty(self):
        result = exam_day5.count_words("")
        self.assertEqual(result,{})
if __name__ == "__main__":
    unittest.main()