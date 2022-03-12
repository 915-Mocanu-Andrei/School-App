from students.repository.repository import *
from students.domain.entities import *
from students.Validators.validators import *


class StudentsService:
    """
    Manage functionalities of the whole register
    """

    def __init__(self, students_repo, disciplines_repo, grades_repo, backwards_repo, forwards_repo):
        self._students_repo = students_repo
        self._disciplines_repo = disciplines_repo
        self._grades_repo = grades_repo
        self.backwards_repo = backwards_repo
        self.forwards_repo = forwards_repo

    def setup(self):
        """

        :return: sets up the default values
        """
        self._students_repo = Repository()
        self._disciplines_repo = Repository()
        self._grades_repo = Grade_Repository()
        student = Student(100, "George")
        self._students_repo.add(student)
        student = Student(200, "Georgica")
        self._students_repo.add(student)
        student = Student(300, "GeorgeJr")
        self._students_repo.add(student)
        student = Student(400, "Andrei")
        self._students_repo.add(student)
        student = Student(500, "Mihai")
        self._students_repo.add(student)
        discipline = Discipline(110, "Matematica")
        self._disciplines_repo.add(discipline)
        discipline = Discipline(210, "Informatica")
        self._disciplines_repo.add(discipline)
        discipline = Discipline(310, "Extramatica")
        self._disciplines_repo.add(discipline)
        discipline = Discipline(410, "Romana")
        self._disciplines_repo.add(discipline)
        discipline = Discipline(510, "Engleza")
        self._disciplines_repo.add(discipline)
        discipline = Discipline(610, "Fizica")
        self._disciplines_repo.add(discipline)
        grade = Grade(100, 110, 10)
        self._grades_repo.add(grade)
        grade = Grade(200, 210, 3)
        self._grades_repo.add(grade)
        grade = Grade(200, 210, 6)
        self._grades_repo.add(grade)
        grade = Grade(300, 310, 4)
        self._grades_repo.add(grade)
        grade = Grade(400, 410, 10)
        self._grades_repo.add(grade)
        grade = Grade(400, 510, 2)
        self._grades_repo.add(grade)
        grade = Grade(500, 510, 7)
        self._grades_repo.add(grade)

    def get_s_repo(self):
        """

        :return: the repository containg studenets
        """
        return self._students_repo.get_all()

    def get_d_repo(self):
        """

        :return: the repository containg disciplines
        """
        return self._disciplines_repo.get_all()

    def get_g_repo(self):
        """

        :return: the repository containg grades
        """
        return self._grades_repo.get_all()

    def get_b_repo(self):
        return self.backwards_repo.get_all()

    def get_f_repo(self):
        return self.forwards_repo.get_all()

    def add_student(self, id, name):
        """

        :param id: if of student
        :param name: name of student
        :return: adds a student to the repository
        """
        validator = StudentDisciplineValidator()
        try:
            validator.validate(id, name)
            student = Student(int(id), name)
            if self._students_repo.find(student.id) == -1:
                self._students_repo.add(student)
                addition = Add(student.id, "student", student.name)
                self.backwards_repo.add(addition)
            else:
                return -1
        except ValidationException as e:
            return -1

    def add_discipline(self, id, name):
        """

        :param id: if of discipline
        :param name: name of discipline
        :return: adds a student to the discipline
        """
        validator = StudentDisciplineValidator()
        try:
            validator.validate(id, name)
            discipline = Discipline(int(id), name)
            if self._disciplines_repo.find(discipline.id) == -1:
                self._disciplines_repo.add(discipline)
                addition = Add(discipline.id, "discipline", discipline.name)
                self.backwards_repo.add(addition)
            else:
                return -1
        except ValidationException as e:
            return -1

    def update_student(self, id, new_name):
        """

        :param id:
        :param new_name:
        :return: Updates data for student
        """
        if self._students_repo.find(id) != -1:
            s = self._students_repo.get(id)
            old_name = s.name
            self._students_repo.remove(id)
            self.add_student(id, new_name)
            self.backwards_repo.remove_last()
            update = Update(id, "student", new_name, old_name)
            self.backwards_repo.add(update)
        else:
            return -1

    def update_discipline(self, id, new_name):
        """

        :param id:
        :param new_name:
        :return: Updates data of a discipline
        """
        if self._disciplines_repo.find(id) != -1:
            d = self._disciplines_repo.get(id)
            old_name = d.name
            self._disciplines_repo.remove(id)
            self.add_discipline(id, new_name)
            self.backwards_repo.remove_last()
            update = Update(id, "discipline", new_name, old_name)
            self.backwards_repo.add(update)
        else:
            return -1

    def grade(self, student, discipline, grade_value):

        validator = GradeValidator()
        try:
            validator.validate(student, discipline, grade_value)
            grade = Grade(int(student), int(discipline), int(grade_value))
            self._grades_repo.add(grade)
            self.backwards_repo.add(grade)
        except ValidationException as e:
            return -1

        # grade=Grade(student,discipline,grade_value)
        # self._grades_repo.add(grade)

    def delete_student(self, id):
        if self._students_repo.find(int(id)) != -1:
            s = self._students_repo.get(id)
            removal = Remove(id, "student", s.name, [])
            self._students_repo.remove(id)
            grades_removed = self._grades_repo.remove_s(id)
            removal.grades_removed = grades_removed
            self.backwards_repo.add(removal)

    def delete_discipline(self, id):
        if self._disciplines_repo.find(int(id)) != -1:
            d = self._disciplines_repo.get(id)
            removal = Remove(id, "discipline", d.name, [])
            self._disciplines_repo.remove(id)
            grades_removed = self._grades_repo.remove_d(id)
            removal.grades_removed = grades_removed
            self.backwards_repo.add(removal)

    def filter_students_by_id(self, id_part):
        all_students = self._students_repo.get_all()
        matching_students = list(filter(lambda sd: str(id_part) in str(sd.id), all_students))
        return matching_students

    def filter_students_by_name(self, name_part):
        all_students = self._students_repo.get_all()
        matching_students = list(filter(lambda sd: name_part.lower() in sd.name.lower(), all_students))
        return matching_students

    def filter_disciplines_by_name(self, name_part):
        all_disciplines = self._disciplines_repo.get_all()
        matching_disciplines = list(filter(lambda sd: name_part.lower() in sd.name.lower(), all_disciplines))
        return matching_disciplines

    def filter_disciplines_by_id(self, id_part):
        all_disciplines = self._disciplines_repo.get_all()
        matching_disciplines = list(filter(lambda sd: str(id_part) in str(sd.id), all_disciplines))
        return matching_disciplines

    def failing_students(self):
        all_students = self._students_repo.get_all()
        all_disciplines = self._disciplines_repo.get_all()
        all_grades = self._grades_repo.get_all()
        dto_failing_students = []
        for i in all_students:
            for i2 in all_disciplines:
                grades_of_student = []
                for i3 in all_grades:
                    if i3.discipline == i2.id:
                        if i3.student == i.id:
                            grades_of_student.append(i3.grade)
                if len(grades_of_student) > 0:
                    average = sum(grades_of_student) / len(grades_of_student)
                    if average < 5:
                        dto_failing_students.append(i)
                        break
        return dto_failing_students

    def best_students(self):
        all_students = self._students_repo.get_all()
        all_grades = self._grades_repo.get_all()
        students_with_average = []
        for i in all_students:
            students_grades = []
            for i2 in all_grades:
                if i.id == i2.student:
                    students_grades.append(i2.grade)
            if len(students_grades) > 0:
                student_average = sum(students_grades) / len(students_grades)
                students_with_average.append((student_average, i))
        students_with_average.sort(reverse=True, key=lambda x: x[0])
        dto_sorted_students = []
        for i in students_with_average:
            dto_sorted_students.append(i[1])
        return dto_sorted_students

    def disciplines_by_average(self):
        "!!!Comment this!!!"
        all_disciplines = self._disciplines_repo.get_all()
        all_grades = self._grades_repo.get_all()
        disciplines_with_average = []
        for i in all_disciplines:
            discipline_grades = []
            for i2 in all_grades:
                if i.id == i2.discipline:
                    discipline_grades.append(i2.grade)
            if len(discipline_grades) > 0:
                discipline_average = sum(discipline_grades) / len(discipline_grades)
                disciplines_with_average.append((discipline_average, i))
        disciplines_with_average.sort(reverse=True, key=lambda x: x[0])
        dto_sorted_disciplines = []
        for i in disciplines_with_average:
            dto_sorted_disciplines.append(i[1])
        return dto_sorted_disciplines

    def undo(self):
        if len(self.backwards_repo.get_all()) > 0:
            command = self.backwards_repo.get_last()
            self.backwards_repo.remove_last()
            self.forwards_repo.add(command)
            if isinstance(command, Add):
                if command.type == "student":
                    self.delete_student(command.id)
                if command.type == "discipline":
                    self.delete_discipline(command.id)
                self.backwards_repo.remove_last()
            if isinstance(command, Remove):
                if command.type == "student":
                    self.add_student(command.id, command.name)
                    for i in command.grades_removed:
                        self._grades_repo.add(i)
                if command.type == "discipline":
                    self.add_discipline(command.id, command.name)
                    for i in command.grades_removed:
                        self._grades_repo.add(i)
                self.backwards_repo.remove_last()
            if isinstance(command, Update):
                if command.type == "student":
                    self.update_student(command.id, command.old_name)
                    self.backwards_repo.remove_last()
                if command.type == "discipline":
                    self.update_discipline(command.id, command.old_name)
                    self.backwards_repo.remove_last()
            if isinstance(command, Grade):
                self._grades_repo.remove_last()
        else:
            raise ValueError("No more undoes available!")

    def redo(self):
        if len(self.forwards_repo.get_all()) > 0:
            command = self.forwards_repo.get_last()
            self.forwards_repo.remove_last()
            self.backwards_repo.add(command)
            if isinstance(command, Add):
                if command.type == "student":
                    self.add_student(command.id, command.name)
                if command.type == "discipline":
                    self.add_discipline(command.id, command.name)
                self.backwards_repo.remove_last()
            if isinstance(command, Remove):
                if command.type == "student":
                    self.delete_student(command.id)
                if command.type == "discipline":
                    self.delete_discipline(command.id)
                self.backwards_repo.remove_last()
            if isinstance(command, Update):
                if command.type == "student":
                    self.update_student(command.id, command.name)
                if command.type == "discipline":
                    self.update_discipline(command.id, command.name)
                self.backwards_repo.remove_last()
            if isinstance(command, Grade):
                self.grade(command.student, command.discipline, command.grade)
                self.backwards_repo.remove_last()
        else:
            raise ValueError("No more redoes available!")
