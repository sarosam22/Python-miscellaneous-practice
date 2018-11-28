from base_class import *

working_student_1 = WorkingStudent('Ravi','SSSS',[2,4,6,8],250.00)

#now working student will still have the calculate_average ethod
print(working_student_1.calculate_average())

print(working_student_1.__class__)
print(working_student_1.__class__.__base__) ##get parent class

#invoking @property method. Note how this method is not called
print(working_student_1.weekly_salary)