class Student:
    school = 'ABC'
    address = 'hyderabad' 
student1 = Student()
student2 = Student() 
student1.student_id = "111"
student1.student_name = "Dikshitha"
student2.student_id = "112"
student2.marks_language = 85
student2.marks_science = 93
student2.marks_math = 95 
students = [student1, student2]
for student in students:
    print('\n')
    for attr in student._dict_:
        print(f'{attr} -> {getattr(student, attr)}'