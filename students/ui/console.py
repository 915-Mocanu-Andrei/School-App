"""
    UI class.

    Calls between program modules
    ui -> service -> entity
    ui -> entity
"""
from students.domain.entities import *
from students.repository.repository import *
from students.service.service import *
from students.Validators.validators import *
from students.tests.tests import *


class Console:
    def __init__(self, students_service, students_repo, disciplines_repo, grades_repo):
        self.__students_service = students_service
        self.__students_repo = students_repo
        self.__disciplines_repo = disciplines_repo
        self.__grades_repo = grades_repo

    def run_console(self):
        x = 0
        print('Welcome to Students management.app!\n'
              'Choose one of the following commands:\n'
              '1.Add\n'
              '2.Remove\n'
              '3.Update\n'
              '4.List\n'
              '5.Grade student\n'
              '6.Exit\n'
              '7.Search\n'
              '8.Statistics\n'
              '9.Show grades repo\n'
              '10.Undo\n'
              '11.Redo\n'
              )
        while x != 6:
            print(self.__students_service.get_b_repo())
            print(self.__students_service.get_f_repo())
            try:
                x = int(input(''))
                if x not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]:
                    raise TypeError("Please choose one of the options!")
                if x == 1:
                    a = self.__students_service.forwards_repo.get_all()
                    a.clear()
                    what = int(input('What do you want to add?\n'
                                     '1.Student\n'
                                     '2.Discipline\n'))
                    if what not in [1, 2]:
                        raise TypeError("Please choose one of the options!")
                    if what == 1:
                        ret = self.__students_service.add_student(str(input('ID=')), str(input('Name=')))
                        if ret == -1:
                            print("ID already in repo!")
                    if what == 2:
                        ret = self.__students_service.add_discipline(str(input('ID=')), str(input('Name=')))
                        if ret == -1:
                            print("ID already in repo!")
                if x == 2:
                    a = self.__students_service.forwards_repo.get_all()
                    a.clear()
                    what = int(input('What do you want to remove?\n'
                                     '1.Student\n'
                                     '2.Discipline\n'))
                    if what not in [1, 2]:
                        raise TypeError("Please choose one of the options!")
                    if what == 1:
                        self.__students_service.delete_student(int(input('Students ID=')))
                    if what == 2:
                        self.__students_service.delete_discipline(int(input('Discipline ID=')))
                if x == 3:
                    a = self.__students_service.forwards_repo.get_all()
                    a.clear()
                    what = int(input('What do you want to update?\n'
                                     '1.Student\n'
                                     '2.Discipline\n'))
                    if what not in [1, 2]:
                        raise TypeError("Please choose one of the options!")
                    if what == 1:
                        self.__students_service.update_student(int(input('Stundents ID=')), str(input('New name=')))
                    if what == 2:
                        self.__students_service.update_discipline(int(input('Discipline ID=')), str(input('New name=')))
                if x == 4:
                    self.list_all()
                if x == 5:
                    a = self.__students_service.forwards_repo.get_all()
                    a.clear()
                    self.__students_service.grade(str(input('Student ID=')), str(input('Discipline ID=')),
                                                  str(input('Grade value=')))
                if x == 7:
                    print("What do you want to search for?\n"
                          "1.Students\n"
                          "2.Disciplines\n")
                    what = int(input(''))
                    if what not in [1, 2]:
                        raise TypeError("Please choose one of the options!")
                    print("By:\n"
                          "1.ID\n"
                          "2.Name\n")
                    if what == 1:
                        what = int(input(''))
                        if what not in [1, 2]:
                            raise TypeError("Please choose one of the options!")
                        if what == 1:
                            slist = self.__students_service.filter_students_by_id(str(input('ID part=')))
                            for i in slist:
                                print("ID=", i.id, " Name=", i.name, "\n")
                        elif what == 2:
                            slist = self.__students_service.filter_students_by_name(str(input('Name part=')))
                            for i in slist:
                                print("ID=", i.id, " Name=", i.name, "\n")
                    elif what == 2:
                        what = int(input(''))
                        if what == 1:
                            dlist = self.__students_service.filter_disciplines_by_id(str(input('ID part=')))
                            for i in dlist:
                                print("ID=", i.id, " Name=", i.name, "\n")
                        elif what == 2:
                            dlist = self.__students_service.filter_disciplines_by_name(str(input('Name part=')))
                            for i in dlist:
                                print("ID=", i.id, " Name=", i.name, "\n")
                if x == 8:
                    self.statistics_ui()
                if x == 9:
                    print(self.__students_service.get_g_repo())
                if x == 10:
                    try:
                        self.__students_service.undo()
                    except ValueError as e:
                        print(e)
                if x == 11:
                    try:
                        self.__students_service.redo()
                    except ValueError as e:
                        print(e)
            except TypeError as e:
                print(e)
            except ValueError:
                print("Invalid input!")

    def list_all(self):
        what = int(input('What do you want to list?\n'
                         '1.Students\n'
                         '2.Disciplines\n'))
        if what == 1:
            slist = self.__students_service.get_s_repo()
            print("Stundents:\n")
            for i in slist:
                print("ID=", i.id, " Name=", i.name, "\n")
        if what == 2:
            print("Disciplines\n")
            dlist = self.__students_service.get_d_repo()
            for i in dlist:
                print("ID=", i.id, " Name=", i.name, "\n")

    def statistics_ui(self):
        what = int(input('What static do you want to see?\n'
                         '1.All students failing at one or more disciplines\n'
                         '2.Students with the best school situation, sorted in descending order of their aggregated average\n'
                         '3.All disciplines at which there is at least one grade, sorted in descending order of the average grade received by all students enrolled at that discipline\n'))
        slist = []
        if what == 1:
            slist = self.__students_service.failing_students()
        elif what == 2:
            slist = self.__students_service.best_students()
        elif what == 3:
            slist = self.__students_service.disciplines_by_average()
        for i in slist:
            print("ID=", i.id, " Name=", i.name, "\n")


"""students_repo=Repository()
disciplines_repo=Repository()
grades_repo=Grade_Repository()
student = Student(100,"50")
students_repo.add(student)
student = Student(200,"50")
student.name="2"
students_repo.add(student)
print(students_repo.get_all())
print(students_repo.get_all())
grade=Grade(100,200,4)
grades_repo.add(grade)
grades_repo.add(grade)
grade=Grade(200,200,5)
grades_repo.add(grade)
print(grades_repo.get_all())
student_service=StudentsService(students_repo,disciplines_repo,grades_repo)
student_service.delete_student(100)
print(grades_repo.get_all())
"""

"""students_repo=Repository()
disciplines_repo=Repository()
grades_repo=Grade_Repository()
student_service=StudentsService(students_repo,disciplines_repo,grades_repo)
student_service.setup()
console=Console(student_service,students_repo,disciplines_repo,grades_repo)
console.run_console()"""
