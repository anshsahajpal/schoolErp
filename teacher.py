from os.path import exists
from subject import Subject

class Teacher:

    def __init__(self, teacher_id, name, date_of_birth, contact_number, designation, standard=""):
        self.teacher_id = teacher_id
        self.name = name
        self.date_of_birth = date_of_birth
        self.standard = standard
        self.contact_number = contact_number
        self.subjects = []
        self.designation = designation

    def __str__(self):
        return f"{self.teacher_id} {self.name}"

    def __repr__(self):
        return f"{self.teacher_id} {self.name}"

    def print_teacher_details(self):
        print(f"{self.teacher_id} {self.name}")

    def add_subject(self, subject):
        self.subjects.append(subject)



    @staticmethod
    def save_all_teachers(teachers):
        with open("teachers.csv", "w") as file:
            file.write("Id,Name,Date of Birth, Contact, Designation, Standard, Subject\n")
            for teacher in teachers:
                teacher_subjects = ":".join(Subject.get_subject_code_list(teacher.subjects))
                teacher_data = teacher.teacher_id + "," + teacher.name + "," + teacher.date_of_birth + "," + teacher.contact_number + "," + teacher.designation + "," + teacher.standard + "," + teacher_subjects
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
                                      teacher_data[4], teacher_data[5])
                    teacher.add_subject(school["subjects"][subject_code])
                    school["teachers"][teacher_data[0]] = teacher



