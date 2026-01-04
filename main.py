from subject import Subject
from teacher import Teacher

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

add_subject_to_school()
add_teacher_to_school()

print(school["teachers"])
print(school["students"])
print(school["standards"])
print(school["subjects"])

print(school["teachers"]['t1'].subjects)