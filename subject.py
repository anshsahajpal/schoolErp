class Subject:

    def __init__(self, code, name, has_practical:bool, grade_level, is_optional= False):
        self.code = code
        self.name = name
        self.has_practical = has_practical
        self.grade_level = grade_level
        self.is_optional = is_optional


    def __repr__(self):
        return f"{self.code} {self.name} {self.grade_level}"
