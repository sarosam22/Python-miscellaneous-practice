from base_class import *

student_1 = Student('Ram','POIU',[20,50,79,90])

##invoking an instance method i.e on an instance of a class
print(student_1.calculate_average())

##use a class method when u don't need self reference
##but rather reference to the class it was called from

print(Student.hi())
#IT CAN ALSO BE CALLED WITH THE CLASS OBJECT
print(student_1.hi())