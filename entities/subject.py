from os.path import exists

class Subject:
    def __init__(self, code, name, has_practical:bool, grade_level, is_optional= False, teachers_list = None):
        if teachers_list is None:
            teachers_list = []
        self.code = code
        self.name = name
        self.has_practical = has_practical
        self.grade_level = grade_level
        self.is_optional = is_optional
        self.teachers = teachers_list


    def __repr__(self):
        return f"{self.code} {self.name} {self.grade_level} {self.teachers}"

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def print_subject_details(self):
        print(f"Code: {self.code}")
        print(f"Name: {self.name}")
        print(f"Grade Level: {self.grade_level}")
        print(f"IsOptional: {self.is_optional}")
        print(f"Lab: {self.has_practical}")
        if len(self.teachers) > 0:
            print("Taught By")
            for teacher in self.teachers:
                print(f"\tTeacher Name: {teacher.name}")
                print(f"\tTeacher Id: {teacher.teacher_id}")

    @staticmethod
    def get_subject_code_list(list_of_subjects):
        return [subject.code for subject in list_of_subjects]

    @staticmethod
    def save_all_subjects(subjects):
        with open("./data/subjects.csv", "w") as file:
            file.write("Code,Name,Practical,Grade,Optional\n")
            for subject in subjects:
                subject_data = subject.code + "," + subject.name + "," + (
                    "Y" if subject.has_practical else "N") + "," + subject.grade_level + "," + (
                                   "Y" if subject.is_optional else "N")
                file.write(subject_data + "\n")

    @staticmethod
    def load_all_subjects(school):
        if exists("./data/subjects.csv"):
            with open("./data/subjects.csv", "r") as file:
                file.readline()
                for line in file.readlines():
                    subject_data = line.split(",")
                    subject = Subject(subject_data[0], subject_data[1], subject_data[2] == 'Y', subject_data[3],
                                      subject_data[4] == 'Y')
                    school["subjects"][subject_data[0]] = subject