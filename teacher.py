from os.path import exists
from subject import Subject
from standard import Standard

class Teacher:

    def __init__(self, teacher_id, name, date_of_birth, contact_number, designation, teaches_standard=[]):
        self.teacher_id = teacher_id
        self.name = name
        self.date_of_birth = date_of_birth
        self.teaches_standard = teaches_standard
        self.contact_number = contact_number
        self.subjects = []
        self.designation = designation

    def print_teacher_details(self):
        print(f"Teacher Id: {self.teacher_id}")
        print(f"Name: {self.name}")
        print(f"Date of Birth: {self.date_of_birth}")
        print(f"Contact Number: {self.contact_number}")
        print(f"Designation: {self.designation}")
        if len(self.subjects) > 0:
            print(f"Subjects:")
            for subject in self.subjects:
                print(f"\t{subject.code} {subject.name}")
        if len(self.teaches_standard)>0:
            print("Teaches:")
            for standard in self.teaches_standard:
                print(f"\t{standard.grade} {standard.section}")

    def __str__(self):
        return f"{self.teacher_id} {self.name}"

    def __repr__(self):
        return f"{self.teacher_id} {self.name}"

    def add_subject(self, subject):
        self.subjects.append(subject)
        subject.add_teacher(self)

    def add_standard(self, standard):
        self.teaches_standard.append(standard)

    @staticmethod
    def save_all_teachers(teachers):
        with open("teachers.csv", "w") as file:
            file.write("Id,Name,Date of Birth, Contact, Designation, Teaches Standard, Subject\n")
            for teacher in teachers:
                teacher_subjects = ":".join(Subject.get_subject_code_list(teacher.subjects))
                teaches_standard = ":".join(Standard.get_standard_id_list(teacher.teaches_standard))
                teacher_data = teacher.teacher_id + "," + teacher.name + "," + teacher.date_of_birth + "," + teacher.contact_number + "," + teacher.designation + "," + teaches_standard + "," + teacher_subjects
                file.write(teacher_data + "\n")

    @staticmethod
    def load_all_teachers(school):
        if exists("teachers.csv"):
            with open("teachers.csv", "r") as file:
                file.readline()
                for line in file.readlines():
                    teacher_data = line.split(",")
                    subject_code = teacher_data[6].replace("\n", "")
                    teacher = Teacher(teacher_data[0], teacher_data[1], teacher_data[2], teacher_data[3],
                                      teacher_data[4])
                    teacher.add_subject(school["subjects"][subject_code])
                    school["teachers"][teacher_data[0]] = teacher



