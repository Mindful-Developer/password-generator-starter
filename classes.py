"""Demo of classes and objects"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Person: {self.name} | {self.age} years old.'

    def greet(self):
        print(f'Hello, my name is {self.name} and I am {self.age} old.')


class Student(Person):
    def __init__(self, name, age, student_id, grades=None):
        super().__init__(name, age)

        self.student_id = student_id

        if isinstance(grades, list):
            self.grades = grades
        else:
            self.grades = []

    def __str__(self):
        return f'Student {self.name} | ID: {self.student_id} | {self.get_average()}% average'

    def get_average(self):
        return sum(self.grades) / len(self.grades)

    def greet(self):
        print(f"I'm a student!")




if __name__ == '__main__':
    my_person = Student("Fawzia", 20, 301115254)
    my_person.grades.extend([34, 56, 76, 99, 100])
    my_person2 = Student("Delany", 25, 301526545)

    print(my_person.grades)
    print(my_person2.grades)
