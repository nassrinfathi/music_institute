from model.entity.person import Person
from tools.validator import Validator


class Student(Person):
    def __init__(self,id, name,family,national_id,phone,address, grade):
        super().__init__(id, name,family,national_id,phone,address)
        self.grade = grade

    @property
    def grade(self):
        return self._grade


    @grade.setter
    def grade(self,grade):
        self._grade = Validator.grade_validator(grade, "Invalid Grade")