from standard import Standard
from student import Student
from subject import Subject
from teacher import Teacher
import uuid

school = {
    "teachers": {},
    "students": {},
    "standards": {},
    "subjects": {}
}

def add_subject_to_school():
    code = input("Code:")
    name = input("Name:")
    has_practical = input("Has Practical (Y/N):")
    grade_level = input("Grade Level:")
    is_optional = input("Is Optional (Y/N):")
    subject = Subject(code, name, has_practical=='Y', grade_level, is_optional=='Y')
    school["subjects"][code] = subject


def add_teacher_to_school():
    tid = input("Teacher ID:")
    name = input("Teacher Name:")
    dob = input("DOB:")
    contact = input("Contact Number:")
    subject_code = input("Subject Code:")
    designation = input("Designation:")
    teacher = Teacher(tid, name, dob, contact, designation)
    teacher.add_subject(school["subjects"][subject_code])
    school["teachers"][tid] = teacher

def add_standard_to_school():
    grade = input("Grade: ")
    section = input("Section: ")
    room = input("Room No: ")
    standard = Standard(grade, section, room)
    school["standards"][grade+section] = standard


def add_student_to_school():
    first_name = input("First Name")
    last_name = input("Last Name")
    date_of_birth = input("Date of Birth")
    parent_name = input("Parent Name")
    parent_contact = input("Parent Contact")
    student_contact = input("Student Contact")
    enrolment_number = str(uuid.uuid4())
    admission_date = input("Admission Date")
    standard = input("Standard (Can be empty or grade and section ex. 1A):")
    student = Student(first_name,last_name,date_of_birth,parent_name,parent_contact,student_contact,enrolment_number, admission_date)
    if standard != "":
        standard = school["standards"][standard]
        student.set_student_standard(standard)
    school["students"][enrolment_number] = student


def save_school_data():
    Teacher.save_all_teachers(school["teachers"].values())
    Subject.save_all_subjects(school["subjects"].values())
    Standard.save_all_standards(school["standards"].values())
    Student.save_all_students(school["students"].values())

def load_school_data():
    Subject.load_all_subjects(school)
    print(school['subjects'])
    Teacher.load_all_teachers(school)
    print(school['teachers'])
    Standard.load_all_standards(school)
    print(school['standards'])
    Student.load_all_students(school)
    print(school['students'])

def get_standard_by_id(standard_id):
    return school["standards"][standard_id]

def get_teacher_by_id(teacher_id):
    return school["teachers"][teacher_id]

def get_subject_by_id(subject_code):
    return school["subjects"][subject_code]

def get_student_by_id(student_code):
    return school["students"][student_code]
