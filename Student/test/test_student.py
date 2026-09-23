import unittest
from student import Student


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.student = Student("Seun")

    def test_that_when_student_is_created_student_can_introduce(self):
        self.assertEqual(self.student.introduce(), "Seun")

    def test_that_when_student_is_created_grade_level_is_one(self):
        self.assertEqual(self.student.grade_level, 1)

    def test_that_when_i_promote_once_student_grade_level_is_two(self):
        self.student.promote()
        self.assertEqual(self.student.grade_level, 2)

    def test_that_when_i_get_score_from_student_return_pass_if_score_is_50_above(self):
        self.assertEqual("PASS", self.student.has_passed(60))

    def test_that_when_i_get_score_from_student_return_fail_if_score_is_below_50(self):
        self.assertEqual("FAIL", self.student.has_passed(49))

    def test_that_when_i_update_name_student_name_changes(self):
        self.assertEqual("Seun", self.student.name)
        self.student.update_name("Balogun")
        self.assertEqual("Balogun", self.student.name)

    def test_that_grade_level_cannot_exceed_12(self):
        for _ in range(24): self.student.promote()
        self.assertEqual(self.student.grade_level, 12)

    def test_that_when_grade_level_is_12_returns_final_grade_level(self):
        for _ in range(12): self.student.promote()
        self.assertEqual("FINAL GRADE LEVEL", self.student.is_graduating())

    def test_that_when_i_promote_once_student_grade_level_is_one(self):
        self.student.promote()
        self.assertEqual("GRADE LEVEL 2", self.student.is_graduating())

if __name__ == '__main__':
    unittest.main()
