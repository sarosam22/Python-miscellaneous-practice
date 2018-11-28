class Student:

    def __init__(self, new_name, new_school,new_grades):
        #remember, self can have any name but it will always refer to class object as 
        #long as its in the first position of __init__
        self.name = new_name
        self.school = new_school
        self.grades = new_grades

    def __len__(self):
        return len(self.grades)

    def calculate_average(self):
        return sum(self.grades)/len(self.grades)

    def __getitem__(self, i):
        return self.grades[i]

    def __str__(self):
        return f'This is a Student class having name, school and grades of students'

    @classmethod
    def hi(cls):
        return 'This is a class method'



class WorkingStudent(Student):

    def __init__(self, new_name, new_school,new_grades, salary):
        super().__init__(new_name, new_school, new_grades)
        self.salary = salary
    ##this method only returns a calculated value
    #it would be better if we could invoke it like a property
    #for that we use @property decorator. This only works if the method has no argument
    @property
    def weekly_salary(self):
        return self.salary * 40



