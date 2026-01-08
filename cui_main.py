import school

school.load_school_data()

def main_menu():
    while True:
        print("1. Teachers")
        print("2. Subjects")
        print("3. Students")
        print("4. Standards")
        print("5. Save School Data")
        print("6. Load School Data")
        print("7. Show School Data")
        print("0. Exit")
        option = int(input("Option:"))
        if option == 1:
            teacher_menu()
        elif option == 2:
            subject_menu()
        elif option == 3:
            student_menu()
        elif option == 4:
            standard_menu()
        elif option == 5:
            school.save_school_data()
        elif option == 6:
            school.load_school_data()
        elif option == 7:
            print(school.school)
        elif option == 0:
            print("Goodbye")
            break
        else:
            print("Invalid Option")


def teacher_menu():
    while True:
        print("1. Add Teacher To School")
        print("2. Print Teacher Details")
        print("0. Back")
        option = int(input("Option:"))
        if option == 1:
            school.add_teacher_to_school()
        elif option == 2:
            teacher_id = input("Enter Teacher ID: ")
            teacher = school.get_teacher_by_id(teacher_id)
            teacher.print_teacher_details()
        elif option == 0:
            break

def subject_menu():
    while True:
        print("1. Add Subject To School")
        print("2. Print Subject Details")
        print("0. Back")
        option = int(input("Option:"))
        if option == 1:
            school.add_subject_to_school()
        elif option == 2:
            subject_id = input("Enter Subject ID: ")
            subject = school.get_subject_by_id(subject_id)
            subject.print_subject_details()
        elif option == 0:
            break

def student_menu():
    while True:
        print("1. Add Student To School")
        print("2. Assign Standard To Student")
        print("3. Show Student Details")
        print("0. Back")
        option = int(input("Option:"))
        if option == 1:
            school.add_student_to_school()
        elif option == 2:
            standard_id = input("Enter Standard Grade And Section(Ex. 1A): ")
            standard = school.get_standard_by_id(standard_id)
            student_id = input("Enter Student ID: ")
            student = school.get_student_by_id(student_id)
            student.set_student_standard(standard)
        elif option == 3:
            student_id = input("Enter Student ID: ")
            student = school.get_student_by_id(student_id)
            student.print_student_details()
        elif option == 0:
            break


def standard_menu():
    while True:
        print("1. Add Standard To School")
        print("2. Update Class Teacher of Standard")
        print("3. Show Standard Details")
        print("4. Add Subject To Standard")
        print("0. Back")
        option = int(input("Option:"))
        if option == 1:
            school.add_standard_to_school()
        elif option == 2:
            standard_id = input("Enter Standard Grade And Section(Ex. 1A): ")
            standard = school.get_standard_by_id(standard_id)
            if standard.class_teacher != "":
                print("Current Class Teacher: ", standard.class_teacher.name)
            new_teacher = input("Enter ID of new Class Teacher: ")
            teacher = school.get_teacher_by_id(new_teacher)
            standard.set_class_teacher(teacher)
        elif option == 3:
            standard_id = input("Enter Standard Grade And Section(Ex. 1A): ")
            standard = school.get_standard_by_id(standard_id)
            standard.print_standard_details()
        elif option == 4:
            standard_id = input("Enter Standard Grade And Section(Ex. 1A): ")
            standard = school.get_standard_by_id(standard_id)
            no_of_subjects_to_add = int(input("Enter No of Subjects to Add: "))
            for i in range(no_of_subjects_to_add):
                subject_code = input("Enter Subject Code: ")
                subject = school.get_subject_by_id(subject_code)
                standard.add_subject(subject)
        elif option == 0:
            break

main_menu()