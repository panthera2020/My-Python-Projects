import unittest

from Record import Record
from Student import Student


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.record = Record()
        self.new_student = Student()

    def test_that_records_can_add_students_with_unique_id(self):
        self.new_student.set_name("Seun")
        self.record.add_student(self.new_student)
        self.assertEqual(1, len(self.record.get_students()))

    def test_that_records_can_return_all_records_of_a_selected_student(self):
        self.new_student.set_name("Seun")
        self.new_student.set_age(22)
        self.new_student.add_course("Math")
        self.new_student.add_course("English")
        self.new_student.add_course("History")
        self.new_student.add_adress("New York",4443)
        self.record.add_student(self.new_student)
        self.student_records = self.record.get_student_record("SE")
        self.assertEqual("Seun", self.student_records.get_name())
        self.assertEqual(22, self.student_records.get_age())
        self.assertEqual("New York", self.student_records.get_address()["City"])
        self.assertEqual(4443, self.student_records.get_address()["Zip-code"])

    def test_that_records_can_return_list_of_courses_a_particular_student_is_offering(self):
        self.new_student.set_name("Seun")
        self.new_student.add_course("Math")
        self.new_student.add_course("English")
        self.new_student.add_course("History")
        self.new_student.add_course("Economics")
        self.record.add_student(self.new_student)
        self.assertEqual(["math","history","economics"], self.record.get_courses_of("SE"))

    def test_that_records_can_display_city_of_a_particular_student(self):
        self.new_student.set_name("Seun")
        self.new_student.add_adress("New York",4443)
        self.record.add_student(self.new_student)
        self.assertEqual("New York", self.record.get_city_of("SE"))

    def test_that_records_can_display_zip_code_of_a_particular_student(self):
        self.new_student.set_name("Seun")
        self.new_student.add_adress("New York",4443)
        self.record.add_student(self.new_student)
        self.assertEqual(4443, self.record.get_zip_code_of("SE"))

    def test_that_records_can_display_overall_number_of_students_in_system(self):
        self.new_student.set_name("Seun")
        student_two = Student()
        student_two.set_name("Bola")
        student_three = Student()
        student_three.set_name("Ola")
        student_four = Student()
        student_four.set_name("Balogun")
        self.record.add_student(student_two)
        self.record.add_student(student_three)
        self.record.add_student(student_four)
        self.record.add_student(self.new_student)
        self.assertEqual(4, self.record.get_total_count_of_students())


if __name__ == '__main__':
    unittest.main()
