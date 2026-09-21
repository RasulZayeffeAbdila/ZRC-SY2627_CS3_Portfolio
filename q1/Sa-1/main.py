class AssignmentSubmission:
    def __init__(self, student_name, student_id, assignment_title, due_date):
        self.student_name = student_name
        self.student_id = student_id
        self._assignment_title = assignment_title
        self._due_date = due_date
        self.__is_submitted = False
        self.__grade = 0.00
        self.__submitted_files = []

    def __validate_grade(self, score):
        if 1.00 <= score <= 5.00:
            return True
        else:
            return False

    def __check_submission_status(self):
        if self.__grade != 0.00:
            return True
        else:
            return False

    def __is_duplicate_submission(self, filename):
        return filename in self.__submitted_files

    def add_file(self, filename):
        if self.__check_submission_status():
            print(f"[ERROR] Cannot add files to a submitted assignment.")
        elif self.__is_duplicate_submission(filename):
            print(f"[WARNING] '{filename}' is already attached!")
            return
        else:
            self.__submitted_files.append(filename)
            print(f"[SUCCESS] {self.student_name} attached '{filename}'. Total files: {len(self.__submitted_files)}") 

    def remove_file(self, filename):
        if filename in self.__submitted_files:
            if self.__check_submission_status() == True:
                print(f"[WARNING] {self.student_name} cannot remove files. Assignment already graded.")
            else:
                self.__submitted_files.remove(filename)
                print(f"[SUCCESS] {self.student_name} removed '{filename}'.")
        else:
            print(f"[ERROR] File '{filename}' not found in the submission.")

    def assign_grade(self, score):
        if self.__validate_grade(score):
            if self.__submitted_files == []:
                print(f"[ERROR] Cannot grade. No files submitted for {self.student_name}.") 
            else:
                self.__grade = score
                print(f"[SUCCESS] Grade  {self.__grade} officially assigned to {self.student_name}")
        else:
            print(f"[ERROR] Invalid grade. Please provide a valid score between 1.00 and 5.00.")

    def get_grade(self):
        if self.__grade == 0.00:
            return "Not Graded"
        else:
            return self.__grade

    def view_files(self):
        return self.__submitted_files

    def get_status_report(self):
        print(f"ID: {self.student_id},| Name: {self.student_name},| Status: Submitted({len(self.__submitted_files)} files),| Due Date: {self._due_date},| Grade: {self.get_grade()}")

print("--- INITIALIZING DROPBOX FOR STUDENTS ---")
student1 = AssignmentSubmission("Alex Gonzaga", "pshs-1090-x", "CS-101", "2026-10-01")
student2 = AssignmentSubmission("Adelle", "pshs-1920-x", "CS-103", "2026-10-01")
student3 = AssignmentSubmission("Mayris", "pshs-0010-x", "CS-102", "2026-09-30")
student4 = AssignmentSubmission("John Doe", "pshs-1940-x", "CS-106", "2026-10-02")
student5 = AssignmentSubmission("Reze Butter", "pshs-2000-x", "CS-104", "2026-10-11")
print()

print("--- TEST SCENARIO 1: Multiple Files via List---")
student1.add_file("main.py")
student1.add_file("report.pdf")
student1.assign_grade(1.75)
print(f"Alex's Files: {student1.view_files()}\n")

print("--- TEST SCENARIO 2: Removing Files from List---")
student2.add_file("wrong_homework.docx")
student2.remove_file("wrong_homework.docx")
student2.add_file("correct_project.py")
student2.assign_grade(2.25)
print(f"Adelle's Files: {student2.view_files()}\n")

print("--- TEST SCENARIO 3: Preventing Duplicate Files---")
student3.add_file("script.py")
student3.add_file("script.py") 
print(f"Mayris's Files: {student3.view_files()}\n")

print("--- TEST SCENARIO 4: Invalid Grade Assignment---")
student4.add_file("exam_answers.pdf")
student4.assign_grade(3.00)
student4.remove_file("exam_answers.pdf")
print()

print("--- TEST SCENARIO 5: Empty List Handling---")
student5.add_file("draft.txt")
student5.remove_file("draft.txt")
student5.assign_grade(1.50)
print()