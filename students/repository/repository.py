"The repository"

from students.domain.entities import *

class Repository:
    def __init__(self):
        self._data = []


    def add(self, item):
        """
        Store a new item into Repository
        """
        self._data.append(item)


    def remove(self, id_):
        """
        Delete item with given ID from repository
        """
        index = self.find(id_)
        del self._data[index]

    def remove_last(self):
        del self._data[len(self._data)-1]

    def get_last(self):
        return self._data[len(self._data)-1]

    def find(self, id_):
        """
        Find item having given ID
        """
        for i in range(len(self._data)):
            if self._data[i].id == id_:
                return i
        return -1

    def get(self,id_):
        j=self.find(id_)
        return self._data[j]

  #  def __str__(self):
   #     result = "Repository:\n"
    #    for entity in self._data:
     #       result += str(entity)
     #       result += '\n'
      #  return result

   # def __len__(self):
    #    return len(self._data)

    def get_all(self):
        """

        :return: the list stored in the repository
        """
        return self._data


class Grade_Repository:
    def __init__(self):
        self._data = []


    def add(self, item):
        """
        Store a new item into Repository
        """
        self._data.append(item)


    def remove_s(self, id_):
        """
        Delete item with given ID from repository
        """
        grades_removed=[]
        index = self.find_g_student(id_)
        while index!=-1:
            grades_removed.append(self._data[index])
            del self._data[index]
            index = self.find_g_student(id_)
        return grades_removed

    def remove_d(self, id_):
        """
        Delete item with given ID from repository
        """
        grades_removed=[]
        index = self.find_g_discipline(id_)
        while index != -1:
            grades_removed.append(self._data[index])
            del self._data[index]
            index = self.find_g_discipline(id_)
        return grades_removed

    def find_g_student(self, id_):
        """
        Find grade having given student
        """
        for i in range(len(self._data)):
            if self._data[i].student == id_:
                return i
        return -1

    def find_g_discipline(self, id_):
        """
        Find discipline having given discipline
        """
        for i in range(len(self._data)):
            if self._data[i].discipline == id_:
                return i
        return -1

    def remove_last(self):
        del self._data[len(self._data)-1]


    """def __str__(self):
        result = "Repository:\n"
        for entity in self._data:
            result += str(entity)
            result += '\n'
        return result

    def __len__(self):
        return len(self._data)"""

    def get_all(self):
        return self._data
