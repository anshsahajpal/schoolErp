class Teacher:

    def __init__(self, teacher_id, name, date_of_birth, contact_number, designation, standard=None):
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


