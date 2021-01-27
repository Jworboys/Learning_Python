"""Classes seem the same in python"""
"""Just use __init__ for the constructor""" 
class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades
    def average(self):
        return sum(self.grades) / len(self.grades)

student = Student("Bob", (90, 90, 97, 98, 67))
print(student.name)
print(student.grades)
print(student.name)
print(f"Student average : {student.average()}")

