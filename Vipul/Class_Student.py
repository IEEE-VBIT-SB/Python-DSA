class Student:
    College = "CBIT"
    def __init__(self,roll,name,depart,Attendance,CGPA):
        self.roll = roll
        self.name = name
        self.depart = depart
        self.Attendance = Attendance
        self.CGPA = CGPA
    
    def disp(self):
        print("COLLEGE : ",Student.College)
        print("Roll Number : ",self.roll)
        print("Name : ",self.name)
        print("Department : ",self.depart)
        print("Attendance : "+str(self.Attendance)+"%")
        print("CGPA : ",self.CGPA)

Stu1 = Student(102,"Ravi","CSE",65.3,7.9)
Stu2 = Student(104,"Adarsh","IT",90.3,8.5)
Stu1.disp()
Stu2.disp()
