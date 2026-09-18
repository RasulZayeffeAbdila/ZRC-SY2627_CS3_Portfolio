class Course:
    def __init__(self, courseName):
        self.course = courseName
        self.students = []

    def name(self):
        return self.course

    def addStudent(self, student):
        self.students.append(student)

    def removeStudent(self, student):
        if student in self.students:
            self.students.remove(student)
        else:
            print(student.name, "(", student.studentID, ") is not enrolled in", self.course)


class Student:
    def __init__(self, studentID, name, grade):
        self.studentID = studentID
        self.name = name
        self.grade = grade

    def getGrade(self):
        return self.grade

    def enroll(self, course):
      course.addStudent(self)
      print(self.name, "(", self.studentID, ") has been added to", course.name())

    def remove(self, course):
      course.removeStudent(self)
      print(self.name, "(", self.studentID, ") has been removed from", course.name())


course = Course("CS3-NA")

student1 = Student("2024-001", "John Zenin", 1.00)
student2 = Student("2024-053", "Estes", 1.75)

print(course.name())

student1.enroll(course)
student2.enroll(course)

print([student.name for student in course.students])

student1.remove(course)
