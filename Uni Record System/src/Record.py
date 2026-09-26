
class Record:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        name = student.get_name()
        id = "" + name[0].upper() + name[1].upper()
        self.students.append({id: student})


    def get_students(self):
        return self.students

    def get_student_record(self, id):
        for student in self.students:
            for student_id in student.keys():
                if student_id == id: return student[id]

    def get_courses_of(self, id):
        for student in self.students:
            for student_id in student.keys():
                if student_id == id: return student[student_id].get_courses()

    def get_city_of(self, id):
        for student in self.students:
            for student_id in student.keys():
                if student_id == id: return student[student_id].get_address()["City"]

    def get_zip_code_of(self, id):
        for student in self.students:
            for student_id in student.keys():
                if student_id == id: return student[student_id].get_address()["Zip-code"]

    def get_total_count_of_students(self):
        return len(self.students)
