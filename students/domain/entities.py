from dataclasses import dataclass


@dataclass
class Student:
    """
    Student class with attributes/properties id and name
    """
    __id: int
    __name: str

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,newname):
        self.__name = newname


@dataclass
class Discipline:
    """
    Discipline class with attributes/properties id and name
    """
    __id: int
    __name: str

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, newdiscipline):
        self.__name = newdiscipline

@dataclass
class Grade:
    """
    Grade class with attributes/properties student id, discipline id and its value(grade value)
    """
    __student_id: int
    __discipline_id: int
    __grade_value: int

    @property
    def student(self):
        return self.__student_id

    @property
    def discipline(self):
        return self.__discipline_id

    @property
    def grade(self):
        return self.__grade_value

@dataclass
class Add:
    __id: int
    __type: str
    __name: str

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def type(self):
        return self.__type


@dataclass
class Update:
    __id: int
    __type: str
    __name: str
    __old_name: str

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def type(self):
        return self.__type

    @property
    def old_name(self):
        return self.__old_name


@dataclass
class Remove:
    __id: int
    __type: str
    __name: str
    __grades_removed: list

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def type(self):
        return self.__type

    @property
    def grades_removed(self):
        return self.__grades_removed

    @grades_removed.setter
    def grades_removed(self,grades_removed):
        self.__grades_removed = grades_removed