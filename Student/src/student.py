
class Student:

    def __init__(self, name,grade_level = 1):
        self.name = name
        self.grade_level = grade_level

    def introduce(self): return self.name

    def promote(self):
        if self.grade_level < 12:
            self.grade_level += 1

    def has_passed(self, score):
        if score >= 50: return "PASS"
        else : return "FAIL"

    def update_name(self, new_name): self.name = new_name

    def is_graduating(self):
        if self.grade_level == 12: return"FINAL GRADE LEVEL"
        else : return "GRADE LEVEL " + str(self.grade_level)