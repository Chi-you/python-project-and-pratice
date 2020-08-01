class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def get_grade(self):
        return self.grade
class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
    def add_students(self, student): # student here is a class instance
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value/len(self.students)

s1 = Student("Tom", 19, 95)
s2 = Student("Jack", 19, 45)
s3 = Student("David", 19, 56)

course = Course("Science", 2)
print(course.add_students(s1))
print(course.add_students(s2))
for c in course.students:
    print([c])

print(course.add_students(s3))
