class Student:
    # all instances of the students
    all = []

    def __init__(self, name, reg):
        self.name = name
        self.reg = reg
        self._teacher = None
        Student.all.append(self)

    @property
    def teacher(self):
        return self._teacher

    @teacher.setter
    def teacher(self, teacher):
        # we have to ensure that teacher is an instance of Teacher
        if not isinstance(teacher, Teacher):
            raise TypeError("Must be an instance of a Teacher Class")
        self._teacher = teacher


class Teacher:
    def __init__(self, name):
        self.name = name

    def students(self):
        return [student for student in Student.all if student.teacher == self]

    def add_student(self, student):
        # check if student is an instance of Student
        if not isinstance(student, Student):
            raise TypeError("Instance passed must be of Student Class")
        student.teacher = self


_1028326 = Student("Eric Maranga", 1028326)
_1028325 = Student("Teresia Wangari", 1028325)
warui = Teacher("Bwana Warui")
warui.add_student(_1028326)


print(Student.all[0].teacher.name)
