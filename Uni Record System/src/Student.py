from Courses import Course

class Student:
    def __init__(self, name = "John Doe"):
        self.name = name
        self.age = 0
        self.courses = []
        self.address = {"City":"","Zip-code":0}

    def set_name(self,name):
        self.name = name

    def get_name(self):
        return self.name

    def set_age(self, age):
        self.age = age

    def get_age(self):
        return self.age

    def add_course(self, course):
        course_to_lower = course.lower()
        if len(self.courses) == 0:
            for each_course in Course:
                if each_course.value == course_to_lower: self.courses.append(each_course)
        else:
            for registered_course in self.courses:
                if registered_course.value == course_to_lower: return
            for each_course in Course:
                if each_course.value == course_to_lower: self.courses.append(each_course)


    def get_courses(self):
        return [each_course.value for each_course in self.courses]

    def add_adress(self, address, zip_code):
        self.address["City"] = address
        self.address["Zip-code"] = zip_code

    def get_address(self):
        return self.address

    def remove_course(self, course):
        for registered_course in self.courses:
            if registered_course.value == course.lower(): self.courses.remove(registered_course)