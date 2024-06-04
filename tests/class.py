class Student:
    def __init__(self, name, age, ID):
        self.name = name
        self.age = age
        self.id = ID

    def print_student(self):
        print(f"Name: {self.name}\nAge: {self.age}\nID: {self.id}")


student = Student("Salem", 21,44254187)
student.print_student()