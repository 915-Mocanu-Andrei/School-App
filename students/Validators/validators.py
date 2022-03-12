from students.domain.entities import *
from students.repository.repository import *
from students.exceptions.exceptions import *

class StudentDisciplineValidator:

    @staticmethod
    def validate(id,name):
        """if len(id) == 0:
            raise ValueError("Invalid id, empty value provided")
        if len(name)== 0:
            raise ValueError("Invalid name, empty value provided")"""

        error_messages = []
        if id == "":
            error_messages.append("ID can not be empty")
        if name == "":
            error_messages.append("Name can not be empty")
        if len(error_messages) > 0:
            raise ValidationException(error_messages)


class GradeValidator:

    @staticmethod
    def validate(student,discipline,grade):
        """if len(student) == 0:
            raise ValueError("Invalid ID, empty value provided")

        if len(discipline) == 0:
            raise ValueError("Invalid name, empty value provided")

        if len(grade) == 0:
            raise ValueError("Invalid ID, empty value provided")"""
        error_messages = []
        if student == "":
            error_messages.append("Student ID can not be empty")
        if discipline == "":
            error_messages.append("Discipline ID can not be empty")
        if grade == "":
            error_messages.append("Grade value can not be empty")
        if int(grade)>10 or int(grade)<1:
            error_messages.append("Grade value cant be bigger then 10 or smaller then 1")
        if len(error_messages) > 0:
            raise ValidationException(error_messages)
