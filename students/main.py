from students.ui.console import *


if __name__ == '__main__':
    students_repo = Repository()
    disciplines_repo = Repository()
    grades_repo = Grade_Repository()
    backwards_repo = Repository()
    forwards_repo = Repository()
    student_service = StudentsService(students_repo, disciplines_repo, grades_repo,backwards_repo, forwards_repo)
    student_service.setup()
    console = Console(student_service, students_repo, disciplines_repo, grades_repo)
    console.run_console()

