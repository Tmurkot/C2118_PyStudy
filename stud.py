class Student:

    def __init__(self, name, name2, subject, homework):
        self.name = name
        self.name2 = name2
        self.subject = subject
        self.homework = homework

    def desc(self):
        return (f"Студ.: {self.name} - {self.name2}\n"
                f"Пред.: {self.subject}\n"
                f"Домаш.: {self.homework}")
Stdu = Student(