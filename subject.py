from os.path import exists

class Subject:

    def __init__(self, code, name, has_practical:bool, grade_level, is_optional= False):
        self.code = code
        self.name = name
        self.has_practical = has_practical
        self.grade_level = grade_level
        self.is_optional = is_optional


    def __repr__(self):
        return f"{self.code} {self.name} {self.grade_level}"

    @staticmethod
    def get_subject_code_list(list_of_subjects):
        return [subject.code for subject in list_of_subjects]

    @staticmethod
    def save_all_subjects(subjects):
        with open("subjects.csv", "w") as file:
            file.write("Code,Name,Practical,Grade,Optional\n")
            for subject in subjects:
                subject_data = subject.code + "," + subject.name + "," + (
                    "Y" if subject.has_practical else "N") + "," + subject.grade_level + "," + (
                                   "Y" if subject.is_optional else "N")
                file.write(subject_data + "\n")

    @staticmethod
    def load_all_subjects(school):
        if exists("subjects.csv"):
            with open("subjects.csv", "r") as file:
                file.readline()
                for line in file.readlines():
                    subject_data = line.split(",")
                    subject = Subject(subject_data[0], subject_data[1], subject_data[2] == 'Y', subject_data[3],
                                      subject_data[4] == 'Y')
                    school["subjects"][subject_data[0]] = subject