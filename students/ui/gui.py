from tkinter import *
from tkinter import filedialog, Text
from students.service.service import *
from tkinter import messagebox
from tkinter import simpledialog


class gui:

    def __init__(self, students_service, students_repo, disciplines_repo, grades_repo):
        self.students_service = students_service
        self.students_repo = students_repo
        self.disciplines_repo = disciplines_repo
        self.grades_repo = grades_repo
        self.frame = None
        self.tk = Tk()
        self.start_message()

    def start_message(self):
        messagebox.showinfo(title='Hello!', message='Welcome to Students management.app!\n'
                                                    'You can do the following:\n'
                                                    '1.Add/Remove/Update/List students and disciplines\n'
                                                    '2.Grade students\n'
                                                    '3.Search students and disciplines by name\n'
                                                    '4.See some statistics\n'
                                                    '5.Undo\n'
                                                    '6.Redo\n'
                            )

    def add_student(self):
        try:
            a = self.students_service.forwards_repo.get_all()
            a.clear()
            self.students_service.add_student(int(self.e_student_id.get()), self.e_name.get())

        except ValueError as e:
            pass

    def remove_student(self):
        try:
            a = self.students_service.forwards_repo.get_all()
            a.clear()
            self.students_service.delete_student(int(self.e_student_id.get()))
        except ValueError as e:
            pass

    def update_student(self):
        try:
            a = self.students_service.forwards_repo.get_all()
            a.clear()
            self.students_service.update_student(int(self.e_student_id.get()), self.e_name.get())
        except ValueError as e:
            pass

    def add_discipline(self):
        try:
            a = self.students_service.forwards_repo.get_all()
            a.clear()
            self.students_service.add_discipline(int(self.e_discipline_id.get()), self.e_name.get())
        except ValueError as e:
            pass

    def remove_discipline(self):
        try:
            a = self.students_service.forwards_repo.get_all()
            a.clear()
            self.students_service.delete_discipline(int(self.e_discipline_id.get()))
        except ValueError as e:
            pass

    def update_discipline(self):
        try:
            a = self.students_service.forwards_repo.get_all()
            a.clear()
            self.students_service.update_discipline(int(self.e_discipline_id.get()), self.e_name.get())
        except ValueError as e:
            pass

    def grade(self):
        try:
            a = self.students_service.forwards_repo.get_all()
            a.clear()
            self.students_service.grade(int(self.e_student_id.get()), int(self.e_discipline_id.get()),
                                        self.e_value.get())
        except ValueError as e:
            pass

    def undo(self):
        try:
            self.students_service.undo()
        except ValueError as e:
            pass

    def redo(self):
        try:
            self.students_service.redo()
        except ValueError as e:
            pass

    def search_students(self):
        if self.e_student_id.get() != '':
            list = self.students_service.filter_students_by_id(self.e_student_id.get())
        else:
            list = self.students_service.filter_students_by_name(self.e_name.get())
        list2 = []
        for i in list:
            string = "ID=" + str(i.id) + "  Name=" + i.name
            list2.append(string)
            stringu = str(list2)
            stringu.replace('', '[')
            stringu.replace(']', '')
        messagebox.showinfo("Matching students", "\n".join(list2))

    def search_disciplines(self):
        if self.e_discipline_id.get() != '':
            list = self.students_service.filter_disciplines_by_id(self.e_discipline_id.get())
        else:
            list = self.students_service.filter_disciplines_by_name(self.e_name.get())
        list2 = []
        for i in list:
            string = "ID=" + str(i.id) + "  Name=" + i.name
            list2.append(string)
            stringu = str(list2)
            stringu.replace('', '[')
            stringu.replace(']', '')
        messagebox.showinfo("Matching disciplines", "\n".join(list2))

    def best_students(self):
        list = self.students_service.best_students()
        list2 = []
        for i in list:
            string = "ID=" + str(i.id) + "  Name=" + i.name
            list2.append(string)
            stringu = str(list2)
            stringu.replace('', '[')
            stringu.replace(']', '')
        messagebox.showinfo("Best students", "\n".join(list2))

    def failing_students(self):
        list = self.students_service.failing_students()
        list2 = []
        for i in list:
            string = "ID=" + str(i.id) + "  Name=" + i.name
            list2.append(string)
            stringu = str(list2)
            stringu.replace('', '[')
            stringu.replace(']', '')
        messagebox.showinfo("Failing students", "\n".join(list2))

    def disciplines_ordered(self):
        list = self.students_service.disciplines_by_average()
        list2 = []
        for i in list:
            string = "ID=" + str(i.id) + "  Name=" + i.name
            list2.append(string)
            stringu = str(list2)
            stringu.replace('[', '')
            stringu.replace(']', '')
        messagebox.showinfo("Disciplines ordered by average", "\n".join(list2))

    def list_students(self):
        list = self.students_service.get_s_repo()
        list2 = []
        for i in list:
            string = "ID=" + str(i.id) + "  Name=" + i.name
            list2.append(string)
            stringu = str(list2)
            stringu.replace('', '[')
            stringu.replace(']', '')
        messagebox.showinfo("Students", "\n".join(list2))

    def list_disciplines(self):
        list = self.students_service.get_d_repo()
        list2 = []
        for i in list:
            string = "ID=" + str(i.id) + "  Name=" + i.name
            list2.append(string)
            stringu = str(list2)
            stringu.replace('[', '')
            stringu.replace(']', '')
        messagebox.showinfo("Disciplines", "\n".join(list2))

    def start(self):
        self.root = Tk()
        frame = Frame(self.root)
        # frame.pack()
        self.frame = frame
        # self.root = Tk()
        self.root.title("Students managment app")
        self.add_student_button = Button(self.frame, text="  add_student      ", padx=5, pady=5, fg="white",
                                         bg="purple", command=self.add_student)
        self.remove_student_button = Button(self.frame, text="  remove_student ", padx=5, pady=5, fg="white",
                                            bg="purple", command=self.remove_student)
        self.update_student_button = Button(self.frame, text="update_student       ", padx=5, pady=5, fg="white",
                                            bg="purple", command=self.update_student)

        self.add_discipline_button = Button(self.frame, text="add_discipline     ", padx=5, pady=5, fg="white",
                                            bg="purple", command=self.add_discipline)
        self.remove_discipline_button = Button(self.frame, text="remove_discipline", padx=5, pady=5, fg="white",
                                               bg="purple", command=self.remove_discipline)
        self.update_discipline_button = Button(self.frame, text="update_discipline    ", padx=5, pady=5, fg="white",
                                               bg="purple", command=self.update_discipline)

        self.grade_button = Button(self.frame, text=" grade_student ", padx=5, pady=5, fg="white", bg="purple",
                                   command=self.grade)
        self.undo_button = Button(self.frame, text="         Undo         ", padx=5, pady=5, fg="white", bg="purple",
                                  command=self.undo)
        self.redo_button = Button(self.frame, text="          Redo         ", padx=5, pady=5, fg="white", bg="purple",
                                  command=self.redo)

        self.best_students_button = Button(self.frame, text="   Best students    ", padx=5, pady=5, fg="white",
                                           bg="purple", command=self.best_students)
        self.failing_students_button = Button(self.frame, text="  Failing students  ", padx=5, pady=5, fg="white",
                                              bg="purple", command=self.failing_students)
        self.disciplines_ordered_button = Button(self.frame, text="Discipliens ordered  ", padx=5, pady=5, fg="white",
                                                 bg="purple", command=self.disciplines_ordered)

        self.search_students_button = Button(self.frame, text=" Search students ", padx=5, pady=5, fg="white",
                                             bg="purple", command=self.search_students)
        self.search_disciplines_button = Button(self.frame, text="Search disciplines", padx=5, pady=5, fg="white",
                                                bg="purple", command=self.search_disciplines)
        self.list_students_button = Button(self.frame, text="  List students  ", padx=5, pady=5, fg="white",
                                           bg="purple", command=self.list_students)
        self.list_disciplines_button = Button(self.frame, text="List disciplines", padx=5, pady=5, fg="white",
                                              bg="purple", command=self.list_disciplines)

        self.add_student_button.grid(column=1, row=1, sticky='w')
        self.remove_student_button.grid(column=2, row=1, sticky='w')
        self.update_student_button.grid(column=3, row=1, sticky='w')

        self.add_discipline_button.grid(column=1, row=2, sticky='w')
        self.remove_discipline_button.grid(column=2, row=2, sticky='w')
        self.update_discipline_button.grid(column=3, row=2, sticky='w')

        self.grade_button.grid(column=4, row=1, sticky='w')
        self.undo_button.grid(column=4, row=2, sticky='w')
        self.redo_button.grid(column=4, row=3, sticky='w')

        self.best_students_button.grid(column=1, row=3, sticky='w')
        self.failing_students_button.grid(column=2, row=3, sticky='w')
        self.disciplines_ordered_button.grid(column=3, row=3, sticky='w')

        self.e_student_id = Entry(self.frame, width=20)
        self.e_name = Entry(self.frame, width=20)
        self.e_discipline_id = Entry(self.frame, width=20)
        self.e_student_id.grid(column=2, row=4, sticky='w')
        self.e_discipline_id.grid(column=2, row=5)
        self.e_name.grid(column=2, row=6, sticky='w')
        self.e_value = Entry(self.frame, width=20)
        self.e_value.grid(column=2, row=7, sticky='w')

        self.l_student_id = Label(self.frame, text="Student ID")
        self.l_student_id.grid(column=1, row=4)
        self.l_discipline_id = Label(self.frame, text="Discipline ID")
        self.l_discipline_id.grid(column=1, row=5)
        self.l_name = Label(self.frame, text="Name")
        self.l_name.grid(column=1, row=6)

        self.l_grade = Label(self.frame, text="Grade")
        self.l_grade.grid(column=1, row=7)
        self.search_students_button.grid(column=4, row=5, sticky='w')
        self.search_disciplines_button.grid(column=4, row=4, sticky='w')
        self.list_students_button.grid(column=3, row=5, sticky='e')
        self.list_disciplines_button.grid(column=3, row=4, sticky='e')
        self.frame.pack()
        self.tk.mainloop()
