import unittest
from Student import Student

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.student = Student()

    def test_that_student_can_set_name_and_name_is_set_correctly(self):
        self.student.set_name("Segun")
        self.assertEqual("Segun", self.student.get_name())

    def test_that_student_can_set_age_and_age_is_set_correctly(self):
        self.student.set_age(22)
        self.assertEqual(22, self.student.get_age())

    def test_that_student_can_add_course(self):
        self.student.add_course("Math")
        self.assertEqual(1,len(self.student.get_courses()))

    def test_that_student_cannot_add_course_not_in_department(self):
        self.student.add_course("programming")
        self.assertEqual(0,len(self.student.get_courses()))

    def test_that_student_cannot_add_course_has_already_been_added(self):
        self.student.add_course("Math")
        self.student.add_course("Math")
        self.assertEqual(1,len(self.student.get_courses()))

    def test_that_student_can_remove_added_course(self):
        self.student.add_course("Math")
        self.assertEqual(1,len(self.student.get_courses()))
        self.student.remove_course("Math")
        self.assertEqual(0,len(self.student.get_courses()))

    def test_that_student_can_add_address_and_zip_code(self):
        self.student.add_adress("2, Bolevard street, New York", 12344)
        self.assertEqual({"City":"2, Bolevard street, New York", "Zip-code": 12344}, self.student.get_address())


if __name__ == '__main__':
    unittest.main()
