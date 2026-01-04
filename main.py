from subject import Subject
from teacher import Teacher
from os.path import exists

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


def save_school_data():
    with open("teachers.csv", "w") as file:
        file.write("Id,Name,Date of Birth, Contact, Designation, Standard, Subject\n")
        for teacher in school["teachers"].values():
            teacher_subjects = ":".join(teacher.get_subject_code_list())
            teacher_data = teacher.teacher_id+","+teacher.name+","+teacher.date_of_birth+","+teacher.contact_number+","+teacher.designation+","+teacher.standard+","+teacher_subjects
            file.write(teacher_data+"\n")

    with open("subjects.csv", "w") as file:
        file.write("Code,Name,Practical,Grade,Optional\n")
        for subject in school["subjects"].values():
            subject_data = subject.code+","+subject.name+","+("Y" if subject.has_practical else "N")+","+subject.grade_level+","+("Y" if subject.is_optional else "N")
            file.write(subject_data+"\n")


def load_school_data():
    if exists("subjects.csv"):
        with open("subjects.csv", "r") as file:
            file.readline()
            for line in file.readlines():
                subject_data = line.split(",")
                subject = Subject(subject_data[0],subject_data[1], subject_data[2]=='Y', subject_data[3], subject_data[4]=='Y')
                school["subjects"][subject_data[0]] = subject

    print(school['subjects'])
    if exists("teachers.csv"):
        with open("teachers.csv", "r") as file:
            file.readline()
            for line in file.readlines():
                teacher_data = line.split(",")
                subject_code = teacher_data[6].replace("\n","")
                teacher = Teacher(teacher_data[0], teacher_data[1], teacher_data[2], teacher_data[3], teacher_data[4], teacher_data[5])
                teacher.add_subject(school["subjects"][subject_code])
                school["teachers"][teacher_data[0]] = teacher







load_school_data()
print(school)
print(school["teachers"]['T1'].subjects)
