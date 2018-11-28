from base_class import *

working_student_1 = WorkingStudent('Ravi','SSSS',[2,4,6,8],250.00)

#now working student will still have the calculate_average ethod
print(working_student_1.calculate_average())

#invoking @property method
print(working_student_1.weekly_salary)