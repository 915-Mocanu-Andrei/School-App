from students.Validators.validators import *
from students.service.service import *
from students.repository.repository import *
from students.exceptions.exceptions import *
from students.ui.console import *

import unittest


class AddUpdateDeleteTest(unittest.TestCase):

    def setUp(self):
        self.students_repo = Repository()#initial lenght = 5
        self.disciplines_repo = Repository()#inital leght = 6
        self.grades_repo = Grade_Repository()#initial lenght = 7
        self.backwards_repo = Repository()
        self.forwards_repo = Repository()
        self.student_service = StudentsService(self.students_repo, self.disciplines_repo, self.grades_repo,self.backwards_repo,self.backwards_repo)
        self.student_service.setup()
        self.console = Console(self.student_service,self.students_repo,self.disciplines_repo,self.grades_repo)

    def test_add_one_student(self):
        self.student_service.add_student("120","Mihai")
        self.assertEqual(len(self.student_service.get_s_repo()),6)

    def test_add_discipline(self):
        self.student_service.add_discipline("1050","Geografie")
        self.assertTrue(len(self.student_service.get_d_repo()) == 7)

    def test_add_two_students(self):
        self.student_service.add_student("120", "Mihai")
        self.student_service.add_student("160", "Petrica")
        self.assertTrue(len(self.student_service.get_s_repo()) == 7)

    def test_add_student(self):
        self.student_service.add_student("120","Mihai")
        l = self.student_service.get_s_repo()
        self.assertTrue(l[len(l)-1].id==120)
        self.assertTrue((l[len(l)-1].name == "Mihai"))

    def test_update_student(self):
        self.student_service.update_student(300,"Georgegica")
        l = self.student_service.get_s_repo()
        self.assertTrue(l[len(l)-1].name == "Georgegica")

    def test_update_discipline(self):
        self.student_service.update_discipline(310,"Megamatica")
        l = self.student_service.get_d_repo()
        self.assertTrue(l[len(l)-1].name == "Megamatica")

    def test_delete_student(self):
        self.assertTrue(self.student_service._students_repo.find(400) != -1)
        self.student_service.delete_student(400)
        self.assertTrue(self.student_service._students_repo.find(400) == -1)

    def test_delete_discipline(self):
        self.assertTrue(self.student_service._disciplines_repo.find(410) != -1)
        self.student_service.delete_discipline(410)
        self.assertTrue(self.student_service._disciplines_repo.find(410) == -1)

    def test_grade(self):
        self.assertTrue(len(self.student_service.get_g_repo()) == 7)
        self.student_service.grade("100","110","7")
        self.assertTrue(len(self.student_service.get_g_repo())==8)

    def test_student_validator(self):
        try:
            validator = StudentDisciplineValidator()
            validator.validate('', 'George', )
            assert False
        except ValidationException:
            self.assertTrue(True)

        try:
            validator = StudentDisciplineValidator()
            validator.validate('102', '', )
            assert False
        except ValidationException:
            self.assertTrue(True)



    def test_discipline_validator(self):
        try:
            validator = StudentDisciplineValidator()
            validator.validate('', 'George', )
            assert False
        except ValidationException:
            self.assertTrue(True)



    def test_grade_validator(self):
        try:
            validator = GradeValidator()
            validator.validate('', '200', '9')
            assert False
        except ValidationException:
            self.assertTrue(True)

        try:
            validator = GradeValidator()
            validator.validate('', '200', '13')
            assert False
        except ValidationException:
            self.assertTrue(True)

        try:
            validator = GradeValidator()
            validator.validate('124', '', '9')
            assert False
        except ValidationException:
            self.assertTrue(True)

    def test_undo_delete_disciplines(self):
        self.assertTrue(self.student_service._disciplines_repo.find(410) != -1)
        self.student_service.delete_discipline(410)
        self.assertTrue(self.student_service._disciplines_repo.find(410) == -1)
        self.student_service.undo()
        self.assertTrue(self.student_service._disciplines_repo.find(410)!=-1)

    def test_undo_delete_student(self):
        self.assertTrue(self.student_service._students_repo.find(400) != -1)
        self.student_service.delete_student(400)
        self.assertTrue(self.student_service._students_repo.find(400) == -1)
        self.student_service.undo()
        self.assertTrue(self.student_service._students_repo.find(400)!=-1)


    def test_undo_add_student(self):
        self.student_service.add_student("120", "Mihai")
        l = self.student_service.get_s_repo()
        self.assertTrue(l[len(l) - 1].id == 120)
        self.assertTrue((l[len(l) - 1].name == "Mihai"))
        self.student_service.undo()
        self.assertTrue(self.student_service._students_repo.find(120)== -1)

    def test_undo_add_discipline(self):
        self.student_service.add_discipline("120", "Materie")
        l = self.student_service.get_d_repo()
        self.assertTrue(l[len(l) - 1].id == 120)
        self.assertTrue((l[len(l) - 1].name == "Materie"))
        self.student_service.undo()
        self.assertTrue(self.student_service._students_repo.find(120) == -1)


    def test_undo_update_student(self):
        self.student_service.update_student(300, "Georgegica")
        l = self.student_service.get_s_repo()
        self.assertTrue(l[len(l) - 1].name == "Georgegica")
        self.student_service.undo()
        self.assertTrue(l[len(l) - 1].name == "GeorgeJr")


    def test_undo_update_discipline(self):
        self.student_service.update_discipline(310, "Megamatica")
        l = self.student_service.get_d_repo()
        self.assertTrue(l[len(l) - 1].name == "Megamatica")
        self.student_service.undo()
        self.assertTrue(l[len(l) - 1].name == "Extramatica")


    def test_redo_add__student(self):
        self.student_service.add_student("120", "Mihai")
        l = self.student_service.get_s_repo()
        self.assertTrue(l[len(l) - 1].id == 120)
        self.assertTrue((l[len(l) - 1].name == "Mihai"))
        self.student_service.undo()
        self.assertTrue(self.student_service._students_repo.find(120) == -1)
        self.student_service.redo()
        self.assertFalse(self.student_service._students_repo.find(120) == -1)

    def test_redo_add__discipline(self):
        self.student_service.add_discipline("120", "Materie")
        l = self.student_service.get_d_repo()
        self.assertTrue(l[len(l) - 1].id == 120)
        self.assertTrue((l[len(l) - 1].name == "Materie"))
        self.student_service.undo()
        self.assertTrue(self.student_service._disciplines_repo.find(120) == -1)
        self.student_service.redo()
        self.assertFalse(self.student_service._disciplines_repo.find(120) == -1)

    def test_redo_update_student(self):
        self.student_service.update_student(300, "Georgegica")
        l = self.student_service.get_s_repo()
        self.assertTrue(l[len(l) - 1].name == "Georgegica")
        self.student_service.undo()
        self.assertTrue(l[len(l) - 1].name == "GeorgeJr")
        self.student_service.redo()
        self.assertTrue(l[len(l) - 1].name == "Georgegica")

    def test_redo_update_discipline(self):
        self.student_service.update_discipline(310, "Georgematerie")
        l = self.student_service.get_d_repo()
        self.assertTrue(l[len(l) - 1].name == "Georgematerie")
        self.student_service.undo()
        self.student_service.redo()
        self.assertTrue(l[len(l) - 1].name == "Georgematerie")

    def test_redo_remove_student(self):
        self.student_service.delete_student(200)
        l= self.student_service.get_s_repo()
        self.assertTrue(len(l)==4)
        self.student_service.undo()
        self.assertTrue(len(l) == 5)
        self.student_service.redo()
        self.assertTrue(len(l) == 4)

    def test_redo_remove_discipline(self):
        self.student_service.delete_discipline(210)
        l= self.student_service.get_d_repo()
        self.assertTrue(len(l)==5)
        self.student_service.undo()
        self.assertTrue(len(l) == 6)
        self.student_service.redo()
        self.assertTrue(len(l) == 5)


    def test_filter_students_by_id(self):
        filtered = self.student_service.filter_students_by_id("1")
        for i in filtered:
            self.assertTrue(str("1") in str(i.id).lower())


    def test_filter_disciplines_by_id(self):
        filtered = self.student_service.filter_disciplines_by_id("1")
        for i in filtered:
            self.assertTrue(str("1") in str(i.id).lower())

    def test_filter_students_by_name(self):
        filtered = self.student_service.filter_students_by_name("geo")
        for i in filtered:
            self.assertTrue("geo" in str(i.name).lower())

    def test_filter_disciplines_by_name(self):
        filtered = self.student_service.filter_disciplines_by_name("atica")
        for i in filtered:
            self.assertTrue("atica" in str(i.name).lower())


    def test_failing_students(self):
        filtered = self.student_service.failing_students()
        all_disciplines = self.student_service._disciplines_repo.get_all()
        all_grades = self.student_service._grades_repo.get_all()
        for i in filtered:
            lowest_average = 10
            for i2 in all_disciplines:
                grades_of_student=[]
                for i3 in all_grades:
                    if i3.discipline == i2.id:
                        if i3.student == i.id:
                            grades_of_student.append(i3.grade)
                if len(grades_of_student)>0:
                    average = sum(grades_of_student)/len(grades_of_student)
                    if average < lowest_average:
                        lowest_average = average
            self.assertTrue(lowest_average < 5)

    def test_best_students(self):
        filtered = self.student_service.best_students()
        all_grades=self.student_service.get_g_repo()
        initial_average=1000
        for i in filtered:
            students_grades = []
            for i2 in all_grades:
                if i.id == i2.student:
                    students_grades.append(i2.grade)
            student_average = sum(students_grades) / len(students_grades)
            self.assertTrue( student_average <= initial_average)
            initial_average=student_average

    def test_disciplines_by_average(self):
        filtered = self.student_service.disciplines_by_average()
        all_grades = self.student_service.get_g_repo()
        initial_average = 10000
        for i in filtered:
            discipline_grades=[]
            for i2 in all_grades:
                if i.id == i2.discipline:
                    discipline_grades.append(i2.grade)
            discipline_average = sum(discipline_grades)/len(discipline_grades)
            self.assertTrue(discipline_average <= initial_average)
            initial_average = discipline_average

    def test_validation_exception(self):
        e=ValidationException([])
        e2=RegisterException([])
        self.assertTrue(e.messages==[])
        self.assertTrue(e.__str__()==str([]))


    def test_redo_empty(self):
        try:
            self.student_service.redo()
        except ValueError as e:
            self.assertTrue(str(e)=="No more redoes available!")

    def test_undo_empty(self):
        try:
            self.student_service.undo()
        except ValueError as e:
            self.assertTrue(str(e)=="No more undoes available!")

    def test_update_error1(self):
        a = self.student_service.update_student(100000,"da")
        self.assertTrue(a==-1)

    def test_update_error2(self):
        a = self.student_service.update_discipline(100000, "da")
        self.assertTrue(a == -1)

    def test_redo_grade(self):
        self.student_service.grade(8,8,8)
        self.student_service.undo()
        self.student_service.redo()
        self.assertTrue(Grade(8,8,8) in self.student_service.get_g_repo())

if __name__=="__main__":
    unittest.main()
