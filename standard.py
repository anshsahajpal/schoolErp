from typing import List
from os.path import exists
from student import Student
from subject import Subject

class Standard:

    def __init__(self,grade, section, room_no, subjects=[], class_teacher="", students=[]):
        self.grade = grade
        self.section = section
        self.subjects = subjects
        self.class_teacher = class_teacher
        self.students = students
        self.room_no = room_no


    def __repr__(self):
        return f"{self.grade}-{self.section}-{self.room_no}"

    def add_subject(self, subject):
        self.subjects.append(subject)

    def set_class_teacher(self, teacher):
        self.class_teacher = teacher

    def add_student(self, student):
        self.students.append(student)

    def print_standard_details(self):
        print("Grade: ", self.grade)
        print("Section: ", self.section)
        print("Room No: ", self.room_no)
        if self.class_teacher == "":
            print("Class Teacher: Not Assigned")
        else:
            print("Class Teacher: ", self.class_teacher.teacher_id, " ", self.class_teacher.name)
        if len(self.subjects) > 0:
            print("Subjects:")
            for subject in self.subjects:
                print(subject.code," ",subject.name)
        else:
            print("No Subjects in class")
        if len(self.students) > 0:
            print("Students:")
            for student in self.students:
                print(student.enrolment_number," ",student.first_name," ",student.last_name)
        else:
            print("No Students in class")

    @staticmethod
    def save_all_standards(standards: List[Standard]):
        with open("standards.csv", "w") as file:
            file.write("Grade,Section,Class Teacher,Room No,Students, Subjects\n")
            for standard in standards:
                standard_subjects = ":".join(Subject.get_subject_code_list(standard.subjects))
                standard_students = ":".join(Student.get_list_of_enrolment_numbers_of_students(standard.students))
                standard_data = standard.grade + "," + standard.section + "," + ("" if standard.class_teacher == "" else standard.class_teacher.teacher_id) + "," + standard.room_no + "," + standard_students + "," + standard_subjects
                file.write(standard_data + "\n")

    @staticmethod
    def load_all_standards(school):
        if exists("standards.csv"):
            with open("standards.csv", "r") as file:
                file.readline()
                for line in file.readlines():
                    standard_data = line.split(",")
                    standard = Standard(standard_data[0], standard_data[1], standard_data[3])
                    if standard_data[2] != "":
                        standard.set_class_teacher(school['teachers'][standard_data[2]])
                    if standard_data[5] != "":
                        subject_code_list = standard_data[5].split(":")
                        for subject_code in subject_code_list:
                            standard.add_subject(school['subjects'][subject_code.replace("\n","")])
                    school['standards'][standard.grade+standard.section] = standard
