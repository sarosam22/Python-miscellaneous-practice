from base_class import Student



##instantiating class and checking funtionality


student_1 = Student("Sarodik", [10,20,30,40])

print(student_1.__class__)  #gives class name


print(student_1.calculate_average())
#OR
print(Student.calculate_average(student_1))