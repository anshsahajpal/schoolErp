from typing import List
from os.path import exists

class Student:

    def __init__(self, first_name, last_name, date_of_birth, parent_name, parent_contact, student_contact,
                 enrolment_number, admission_date, standard = ""):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.standard = standard
        self.parent_name = parent_name
        self.parent_contact = parent_contact
        self.student_contact = student_contact
        self.enrolment_number = enrolment_number
        self.admission_date = admission_date

    def __repr__(self):
        return f"{self.enrolment_number} {self.first_name} {self.last_name}"

    def set_student_standard(self, standard):
        self.standard = standard
        standard.add_student(self)

    def print_student_details(self):
        print("Enrolment number: " + str(self.enrolment_number))
        print("Roll No: "+ str((self.standard.students.index(self)+1)))
        print("Standard: "+ (self.standard.grade+self.standard.section))
        print("Name: " + (self.first_name)+" "+(self.last_name))
        print("Date of Birth: " + (self.date_of_birth))
        print("Parent Name: " + (self.parent_name))
        print("Parent Contact: " + (self.parent_contact))
        print("Student Contact: " + (self.student_contact))
        print("Admission Date: " + (self.admission_date))

    @staticmethod
    def get_list_of_enrolment_numbers_of_students(list_of_students):
        return [student.enrolment_number for student in list_of_students]

    @staticmethod
    def save_all_students(students: List[Student]):
        with open("students.csv", "w") as file:
            file.write("first_name, last_name, date_of_birth, parent_name, parent_contact, student_contact,enrolment_number, admission_date, standard\n")
            for student in students:
                student_data = student.first_name + "," + student.last_name + "," + student.date_of_birth + "," + student.parent_name + "," + student.parent_contact + "," + student.student_contact + "," +student.enrolment_number+ "," + student.admission_date + "," + ("" if student.standard == "" else student.standard.grade+student.standard.section)
                file.write(student_data + "\n")

    @staticmethod
    def load_all_students(school):
        if exists("students.csv"):
            with open("students.csv", "r") as file:
                file.readline()
                for line in file.readlines():
                    student_data = line.split(",")
                    student = Student(student_data[0], student_data[1], student_data[2], student_data[3], student_data[4], student_data[5], student_data[6], student_data[7])
                    if student_data[8]!="\n":
                        student.set_student_standard(school['standards'][student_data[8].replace("\n","")])
                    school['students'][student.enrolment_number] = student