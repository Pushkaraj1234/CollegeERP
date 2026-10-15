import unittest
from app import add_student, get_student, list_students, students

class TestCollegeERP(unittest.TestCase):
    def setUp(self):
        students.clear()

    def test_add_student(self):
        self.assertTrue(add_student("101", "Asha", "Computer Engineering"))

    def test_duplicate_student_id_rejected(self):
        add_student("101", "Asha", "Computer Engineering")
        self.assertFalse(add_student("101", "Rahul", "Mechanical"))

    def test_get_student(self):
        add_student("102", "Riya", "IT")
        self.assertEqual(get_student("102")["name"], "Riya")

    def test_missing_student(self):
        self.assertIsNone(get_student("999"))

    def test_list_students(self):
        add_student("103", "Aman", "IT")
        self.assertEqual(len(list_students()), 1)

if __name__ == "__main__":
    unittest.main()

    def test_search_students(self):
        from app import search_students
        add_student("104", "Neha", "Computer Engineering")
        results = search_students("computer")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0][0], "104")

    def test_search_students(self):
        from app import search_students
        add_student("104", "Neha", "Computer Engineering")
        results = search_students("computer")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0][0], "104")
