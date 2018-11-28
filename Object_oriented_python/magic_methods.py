from base_class import *

#__class__
print([1,2].__class__)
print('Hi'.__class__)
print(Student('Rob','RSUP',[1,2,3,4]).__class__)

#__len__
student_1 = Student('Roy','RSUP',[9,10,11,12,7])
print(len(student_1))   #notice how we passed the class object to len and not exactly a list

#__getitem__
print(student_1[1])

##Matter of fact, we can now even iterate over the student_1 object

#__repr__
print(student_1.__repr__)

#__str__
print(student_1) ##__str__ is invoked