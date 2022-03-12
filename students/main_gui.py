from students.service.service import *
from students.ui.gui import *
from students.domain.entities import *


if __name__ == '__main__':
    students_repo = Repository()
    disciplines_repo = Repository()
    grades_repo = Grade_Repository()
    backwards_repo = Repository()
    forwards_repo = Repository()
    students_service = StudentsService(students_repo, disciplines_repo, grades_repo, backwards_repo, forwards_repo)
    students_service.setup()
    my_gui=gui(students_service,students_repo,disciplines_repo,grades_repo)
    my_gui.start()
